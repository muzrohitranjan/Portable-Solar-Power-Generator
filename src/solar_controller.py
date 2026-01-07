import time
import json
import logging
from datetime import datetime
import threading
from typing import Dict, Any, Optional

class SolarPowerGenerator:
    """Main controller for Portable Solar Power Generator"""
    
    def __init__(self):
        self.battery_level: float = 75.0  # Start with some charge
        self.solar_panel_voltage: float = 0.0
        self.battery_voltage: float = 12.0
        self.is_charging: bool = False
        self.system_temperature: float = 25.0
        
        self.devices: Dict[str, bool] = {
            'light': False,
            'fan': False,
            'mobile_charger': False
        }
        
        self.device_power_consumption: Dict[str, float] = {
            'light': 0.5,      # 0.5% per second
            'fan': 1.0,        # 1.0% per second  
            'mobile_charger': 0.8  # 0.8% per second
        }
        
        self.charge_controller_active: bool = True
        self.safety_mode: bool = False
        self.total_energy_generated: float = 0.0
        self.total_energy_consumed: float = 0.0
        
        # Setup logging
        self._setup_logging()
        
    def _setup_logging(self) -> None:
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/solar_generator.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def read_solar_panel(self) -> float:
        """Read solar panel voltage with realistic simulation"""
        import random
        current_hour = datetime.now().hour
        
        # Realistic solar generation based on time of day
        if 6 <= current_hour <= 18:  # Daylight hours
            # Peak generation between 10 AM - 2 PM
            if 10 <= current_hour <= 14:
                base_voltage = random.uniform(16.0, 18.5)
            elif 8 <= current_hour <= 16:
                base_voltage = random.uniform(14.0, 17.0)
            else:
                base_voltage = random.uniform(12.0, 15.0)
                
            # Add some weather variation
            weather_factor = random.uniform(0.7, 1.0)
            self.solar_panel_voltage = base_voltage * weather_factor
            self.is_charging = self.solar_panel_voltage > 13.0
        else:
            self.solar_panel_voltage = random.uniform(0.0, 2.0)
            self.is_charging = False
            
        return self.solar_panel_voltage
    
    def update_battery_level(self) -> None:
        """Update battery level with improved charging/discharging logic"""
        # Charging logic
        if self.is_charging and self.battery_level < 100:
            # More realistic charging curve
            if self.battery_level < 80:
                charge_rate = min(3.0, (self.solar_panel_voltage - 12) * 0.8)
            else:
                # Slower charging when battery is nearly full
                charge_rate = min(1.0, (self.solar_panel_voltage - 12) * 0.3)
                
            energy_added = max(0, charge_rate)
            self.battery_level = min(100, self.battery_level + energy_added)
            self.total_energy_generated += energy_added
        
        # Battery consumption with efficiency factors
        total_consumption = 0
        for device, is_on in self.devices.items():
            if is_on:
                consumption = self.device_power_consumption[device]
                # Add efficiency loss
                consumption *= 1.1  # 10% efficiency loss
                total_consumption += consumption
                
        # Apply consumption
        if total_consumption > 0:
            self.battery_level = max(0, self.battery_level - total_consumption)
            self.total_energy_consumed += total_consumption
            
        # Update battery voltage based on charge level
        self.battery_voltage = 10.5 + (self.battery_level / 100) * 3.9
        
    def control_device(self, device: str, state: bool) -> bool:
        """Enhanced device control with safety checks"""
        if device not in self.devices:
            self.logger.error(f"Unknown device: {device}")
            return False
            
        # Safety checks
        if state and self.battery_level < 15:
            self.logger.warning(f"Low battery! Cannot turn on {device}")
            return False
            
        if state and self.safety_mode:
            self.logger.warning(f"Safety mode active! Cannot turn on {device}")
            return False
            
        # Control device
        old_state = self.devices[device]
        self.devices[device] = state
        
        action = "ON" if state else "OFF"
        self.logger.info(f"Device {device} turned {action}")
        
        return True
    
    def get_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return {
            'battery_level': round(self.battery_level, 1),
            'battery_voltage': round(self.battery_voltage, 2),
            'solar_voltage': round(self.solar_panel_voltage, 1),
            'is_charging': self.is_charging,
            'system_temperature': round(self.system_temperature, 1),
            'devices': self.devices.copy(),
            'safety_mode': self.safety_mode,
            'total_energy_generated': round(self.total_energy_generated, 2),
            'total_energy_consumed': round(self.total_energy_consumed, 2),
            'efficiency': self._calculate_efficiency(),
            'estimated_runtime': self._calculate_runtime(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def _calculate_efficiency(self) -> float:
        """Calculate system efficiency"""
        if self.total_energy_generated == 0:
            return 0.0
        return round((self.total_energy_consumed / self.total_energy_generated) * 100, 1)
    
    def _calculate_runtime(self) -> float:
        """Calculate estimated runtime in hours"""
        active_consumption = sum(
            self.device_power_consumption[device] 
            for device, is_on in self.devices.items() 
            if is_on
        )
        
        if active_consumption == 0:
            return float('inf')
            
        # Convert to hours (consumption is per second, so * 3600)
        return round(self.battery_level / (active_consumption * 3600), 1)
    
    def emergency_shutdown(self) -> None:
        """Enhanced emergency shutdown with logging"""
        self.logger.critical("EMERGENCY SHUTDOWN INITIATED!")
        
        for device in self.devices:
            if self.devices[device]:
                self.devices[device] = False
                self.logger.info(f"Emergency shutdown: {device} turned OFF")
                
        self.safety_mode = True
        
    def reset_safety_mode(self) -> bool:
        """Reset safety mode if conditions are safe"""
        if self.battery_level > 20 and self.battery_voltage > 11.5:
            self.safety_mode = False
            self.logger.info("Safety mode reset - System operational")
            return True
        return False
    
    def save_data_log(self) -> None:
        """Save current status to data log"""
        try:
            status = self.get_status()
            log_entry = {
                'timestamp': status['timestamp'],
                'battery_level': status['battery_level'],
                'solar_voltage': status['solar_voltage'],
                'devices_active': sum(status['devices'].values()),
                'energy_generated': status['total_energy_generated'],
                'energy_consumed': status['total_energy_consumed']
            }
            
            with open('data/system_log.json', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
                
        except Exception as e:
            self.logger.error(f"Failed to save data log: {e}")

# Global generator instance
generator = SolarPowerGenerator()

def monitor_system():
    """Enhanced background monitoring with data logging"""
    log_counter = 0
    
    while True:
        try:
            generator.read_solar_panel()
            generator.update_battery_level()
            
            # Check for emergency conditions
            if generator.battery_level < 5:
                generator.emergency_shutdown()
            elif generator.safety_mode and generator.battery_level > 20:
                generator.reset_safety_mode()
                
            # Log data every 60 seconds
            log_counter += 1
            if log_counter >= 60:
                generator.save_data_log()
                log_counter = 0
                
        except Exception as e:
            generator.logger.error(f"Monitor system error: {e}")
            
        time.sleep(1)

# Start monitoring thread
monitor_thread = threading.Thread(target=monitor_system, daemon=True)
monitor_thread.start()