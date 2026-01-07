import keyboard
import time
import os
from solar_controller import generator

class RemoteControl:
    def __init__(self):
        self.running = True
        self.display_help()
        
    def display_help(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("    PORTABLE SOLAR GENERATOR REMOTE CONTROL")
        print("=" * 50)
        print("\nControls:")
        print("1 - Toggle Light")
        print("2 - Toggle Fan") 
        print("3 - Toggle Mobile Charger")
        print("S - Show Status")
        print("E - Emergency Shutdown")
        print("H - Show Help")
        print("Q - Quit")
        print("\nPress keys to control devices...")
        print("=" * 50)
        
    def show_status(self):
        status = generator.get_status()
        print(f"\n--- SYSTEM STATUS ---")
        print(f"Battery Level: {status['battery_level']}%")
        print(f"Solar Voltage: {status['solar_voltage']}V")
        print(f"Charging: {'Yes' if status['is_charging'] else 'No'}")
        print(f"Light: {'ON' if status['devices']['light'] else 'OFF'}")
        print(f"Fan: {'ON' if status['devices']['fan'] else 'OFF'}")
        print(f"Mobile Charger: {'ON' if status['devices']['mobile_charger'] else 'OFF'}")
        print(f"Time: {status['timestamp']}")
        print("-" * 20)
        
    def toggle_device(self, device):
        current_state = generator.devices[device]
        new_state = not current_state
        
        if generator.control_device(device, new_state):
            print(f"{device.replace('_', ' ').title()}: {'ON' if new_state else 'OFF'}")
        else:
            print(f"Cannot control {device} - Low battery!")
            
    def emergency_shutdown(self):
        generator.emergency_shutdown()
        print("EMERGENCY SHUTDOWN ACTIVATED!")
        print("All devices turned OFF")
        
    def run(self):
        print("\nRemote Control Active - Press keys to control...")
        
        while self.running:
            try:
                if keyboard.is_pressed('1'):
                    self.toggle_device('light')
                    time.sleep(0.3)  # Prevent multiple triggers
                    
                elif keyboard.is_pressed('2'):
                    self.toggle_device('fan')
                    time.sleep(0.3)
                    
                elif keyboard.is_pressed('3'):
                    self.toggle_device('mobile_charger')
                    time.sleep(0.3)
                    
                elif keyboard.is_pressed('s'):
                    self.show_status()
                    time.sleep(0.3)
                    
                elif keyboard.is_pressed('e'):
                    self.emergency_shutdown()
                    time.sleep(0.3)
                    
                elif keyboard.is_pressed('h'):
                    self.display_help()
                    time.sleep(0.3)
                    
                elif keyboard.is_pressed('q'):
                    print("Remote Control Disconnected")
                    self.running = False
                    
                time.sleep(0.1)  # Small delay to prevent high CPU usage
                
            except KeyboardInterrupt:
                print("\nRemote Control Disconnected")
                self.running = False

if __name__ == "__main__":
    remote = RemoteControl()
    remote.run()