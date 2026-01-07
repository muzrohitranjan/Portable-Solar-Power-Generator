"""
Hardware Configuration for Portable Solar Power Generator
MS Engineering College - Final Year Project

Hardware Components:
- Solar Panel: 12V, 50W Monocrystalline
- Battery: 12V, 20Ah Lithium-ion
- Charge Controller: PWM 10A
- Microcontroller: Arduino Uno / Raspberry Pi
- Relay Module: 4-channel 5V
- Voltage Sensor: 0-25V
- Current Sensor: ACS712 20A
- LCD Display: 16x2 I2C
- Bluetooth Module: HC-05
- LED Lights: 12V, 5W
- DC Fan: 12V, 10W
- USB Charging Ports: 5V, 2A
"""

# Pin Configuration for Arduino/Raspberry Pi
PIN_CONFIG = {
    # Analog Pins
    'SOLAR_VOLTAGE_PIN': 'A0',
    'BATTERY_VOLTAGE_PIN': 'A1', 
    'CURRENT_SENSOR_PIN': 'A2',
    
    # Digital Pins - Relay Control
    'LIGHT_RELAY_PIN': 2,
    'FAN_RELAY_PIN': 3,
    'CHARGER_RELAY_PIN': 4,
    'SYSTEM_RELAY_PIN': 5,
    
    # Communication Pins
    'BLUETOOTH_RX': 6,
    'BLUETOOTH_TX': 7,
    'LCD_SDA': 'A4',
    'LCD_SCL': 'A5',
    
    # Status LEDs
    'POWER_LED': 8,
    'CHARGING_LED': 9,
    'LOW_BATTERY_LED': 10
}

# Hardware Specifications
HARDWARE_SPECS = {
    'solar_panel': {
        'voltage': 12,  # Volts
        'power': 50,    # Watts
        'type': 'Monocrystalline'
    },
    'battery': {
        'voltage': 12,  # Volts
        'capacity': 20, # Amp-hours
        'type': 'Lithium-ion',
        'min_voltage': 10.5,
        'max_voltage': 14.4
    },
    'charge_controller': {
        'type': 'PWM',
        'current_rating': 10,  # Amps
        'voltage_rating': 12   # Volts
    },
    'loads': {
        'led_light': {
            'voltage': 12,
            'power': 5,     # Watts
            'current': 0.42 # Amps
        },
        'dc_fan': {
            'voltage': 12,
            'power': 10,    # Watts  
            'current': 0.83 # Amps
        },
        'usb_charger': {
            'voltage': 5,
            'power': 10,    # Watts
            'current': 2    # Amps
        }
    }
}

# Safety Thresholds
SAFETY_LIMITS = {
    'battery_low_voltage': 11.0,      # Volts
    'battery_critical_voltage': 10.5, # Volts
    'max_discharge_current': 15,      # Amps
    'over_temperature': 60,           # Celsius
    'max_solar_voltage': 20           # Volts
}

# Calibration Constants
CALIBRATION = {
    'voltage_divider_ratio': 5.0,     # For voltage sensing
    'current_sensor_sensitivity': 0.1, # V/A for ACS712
    'adc_reference_voltage': 5.0,     # Arduino ADC reference
    'adc_resolution': 1024            # 10-bit ADC
}

def calculate_power_consumption():
    """Calculate total power consumption of connected loads"""
    total_power = 0
    for load, specs in HARDWARE_SPECS['loads'].items():
        total_power += specs['power']
    return total_power

def calculate_battery_runtime(battery_capacity, load_power):
    """Calculate estimated battery runtime in hours"""
    battery_voltage = HARDWARE_SPECS['battery']['voltage']
    battery_wh = battery_capacity * battery_voltage  # Watt-hours
    runtime = battery_wh / load_power if load_power > 0 else float('inf')
    return runtime

def get_charging_time(solar_power, battery_capacity):
    """Calculate estimated charging time in hours"""
    battery_voltage = HARDWARE_SPECS['battery']['voltage']
    battery_wh = battery_capacity * battery_voltage
    charge_time = battery_wh / solar_power if solar_power > 0 else float('inf')
    return charge_time

# Example calculations
if __name__ == "__main__":
    print("Hardware Configuration Summary")
    print("=" * 40)
    print(f"Solar Panel: {HARDWARE_SPECS['solar_panel']['power']}W")
    print(f"Battery: {HARDWARE_SPECS['battery']['capacity']}Ah, {HARDWARE_SPECS['battery']['voltage']}V")
    print(f"Total Load Power: {calculate_power_consumption()}W")
    
    runtime = calculate_battery_runtime(
        HARDWARE_SPECS['battery']['capacity'], 
        calculate_power_consumption()
    )
    print(f"Estimated Runtime: {runtime:.1f} hours")
    
    charge_time = get_charging_time(
        HARDWARE_SPECS['solar_panel']['power'],
        HARDWARE_SPECS['battery']['capacity']
    )
    print(f"Estimated Charge Time: {charge_time:.1f} hours")