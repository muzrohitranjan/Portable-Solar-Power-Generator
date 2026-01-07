#!/usr/bin/env python3
"""
Portable Solar Power Generator - Main Application
MS Engineering College Final Year Project

Team Members:
- Ritik Pandey (Team Leader) - Code review, testing, hardware assistance  
- Rohit Ranjan - Main developer, code implementation, innovation features
- Nikki Kumari Yadav - Project documentation, code review
- Om Singh - Information gathering, research, project analysis

College: MS Engineering College
Affiliated to: Visvesvaraya Technological University
"""

import sys
import os
import threading
import time

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def show_banner():
    print("=" * 60)
    print("    PORTABLE SOLAR POWER GENERATOR")
    print("    MS Engineering College - Final Year Project")
    print("=" * 60)
    print("\nTeam Members:")
    print("• Ritik Pandey (Team Leader) - Code review, testing, hardware")
    print("• Rohit Ranjan - Main developer, innovation features")  
    print("• Nikki Kumari Yadav - Documentation, code review")
    print("• Om Singh - Research, information gathering")
    print("\nCollege: MS Engineering College")
    print("Affiliated to: Visvesvaraya Technological University")
    print("=" * 60)

def show_menu():
    print("\nSelect Interface:")
    print("1. Mobile App Interface (GUI)")
    print("2. Remote Control Interface")
    print("3. System Status Monitor")
    print("4. Hardware Configuration")
    print("5. Exit")
    print("-" * 30)

def run_mobile_app():
    try:
        print("Starting Mobile App Interface...")
        from mobile_app.solar_app import SolarGeneratorApp
        app = SolarGeneratorApp()
        app.run()
    except ImportError as e:
        print(f"Error: {e}")
        print("Make sure tkinter is installed: pip install tkinter")
    except Exception as e:
        print(f"Error starting mobile app: {e}")

def run_remote_control():
    try:
        print("Starting Remote Control Interface...")
        print("Note: Install 'keyboard' module if not available: pip install keyboard")
        from src.remote_control import RemoteControl
        remote = RemoteControl()
        remote.run()
    except ImportError as e:
        print(f"Error: {e}")
        print("Install required module: pip install keyboard")
    except Exception as e:
        print(f"Error starting remote control: {e}")

def run_status_monitor():
    try:
        from src.solar_controller import generator
        print("System Status Monitor - Press Ctrl+C to exit")
        print("-" * 40)
        
        while True:
            status = generator.get_status()
            print(f"\rBattery: {status['battery_level']}% | "
                  f"Solar: {status['solar_voltage']}V | "
                  f"Charging: {'Yes' if status['is_charging'] else 'No'} | "
                  f"Light: {'ON' if status['devices']['light'] else 'OFF'} | "
                  f"Fan: {'ON' if status['devices']['fan'] else 'OFF'} | "
                  f"Charger: {'ON' if status['devices']['mobile_charger'] else 'OFF'}", 
                  end='', flush=True)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStatus monitor stopped.")
    except Exception as e:
        print(f"Error in status monitor: {e}")

def show_hardware_config():
    try:
        from hardware.hardware_config import HARDWARE_SPECS, calculate_power_consumption
        print("\nHardware Configuration:")
        print("-" * 30)
        print(f"Solar Panel: {HARDWARE_SPECS['solar_panel']['power']}W, {HARDWARE_SPECS['solar_panel']['voltage']}V")
        print(f"Battery: {HARDWARE_SPECS['battery']['capacity']}Ah, {HARDWARE_SPECS['battery']['voltage']}V")
        print(f"Charge Controller: {HARDWARE_SPECS['charge_controller']['type']}, {HARDWARE_SPECS['charge_controller']['current_rating']}A")
        print(f"Total Load Power: {calculate_power_consumption()}W")
        print("\nConnected Devices:")
        for device, specs in HARDWARE_SPECS['loads'].items():
            print(f"• {device.replace('_', ' ').title()}: {specs['power']}W, {specs['voltage']}V")
    except Exception as e:
        print(f"Error loading hardware config: {e}")

def main():
    show_banner()
    
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                run_mobile_app()
            elif choice == '2':
                run_remote_control()
            elif choice == '3':
                run_status_monitor()
            elif choice == '4':
                show_hardware_config()
            elif choice == '5':
                print("Thank you for using Portable Solar Power Generator!")
                print("Project by MS Engineering College Team")
                break
            else:
                print("Invalid choice! Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()