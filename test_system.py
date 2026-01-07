#!/usr/bin/env python3
"""
Test Script for Portable Solar Power Generator
Verifies all components are working correctly
"""

import sys
import os
import time

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_solar_controller():
    """Test the main solar controller functionality"""
    print("Testing Solar Controller...")
    try:
        from src.solar_controller import generator
        
        # Test status reading
        status = generator.get_status()
        print(f"✓ Status reading: Battery {status['battery_level']}%, Solar {status['solar_voltage']}V")
        
        # Test device control
        generator.control_device('light', True)
        print("✓ Light control: ON")
        
        generator.control_device('light', False)  
        print("✓ Light control: OFF")
        
        return True
    except Exception as e:
        print(f"✗ Solar Controller Error: {e}")
        return False

def test_hardware_config():
    """Test hardware configuration loading"""
    print("\nTesting Hardware Configuration...")
    try:
        from hardware.hardware_config import HARDWARE_SPECS, calculate_power_consumption
        
        power = calculate_power_consumption()
        print(f"✓ Hardware config loaded: Total power {power}W")
        
        battery_capacity = HARDWARE_SPECS['battery']['capacity']
        print(f"✓ Battery specs: {battery_capacity}Ah")
        
        return True
    except Exception as e:
        print(f"✗ Hardware Config Error: {e}")
        return False

def test_mobile_app():
    """Test mobile app components (without GUI)"""
    print("\nTesting Mobile App Components...")
    try:
        # Test if tkinter is available
        import tkinter as tk
        print("✓ Tkinter available for GUI")
        
        # Test app class import
        from mobile_app.solar_app import SolarGeneratorApp
        print("✓ Mobile app class loaded")
        
        return True
    except ImportError as e:
        print(f"✗ Mobile App Error: {e}")
        print("  Install tkinter if missing")
        return False
    except Exception as e:
        print(f"✗ Mobile App Error: {e}")
        return False

def test_remote_control():
    """Test remote control components"""
    print("\nTesting Remote Control Components...")
    try:
        # Test keyboard module
        import keyboard
        print("✓ Keyboard module available")
        
        # Test remote control class
        from src.remote_control import RemoteControl
        print("✓ Remote control class loaded")
        
        return True
    except ImportError as e:
        print(f"✗ Remote Control Error: {e}")
        print("  Install keyboard module: pip install keyboard")
        return False
    except Exception as e:
        print(f"✗ Remote Control Error: {e}")
        return False

def run_simulation():
    """Run a brief simulation of the system"""
    print("\nRunning System Simulation...")
    try:
        from src.solar_controller import generator
        
        print("Simulating solar charging and device usage...")
        
        # Simulate some operations
        for i in range(5):
            status = generator.get_status()
            print(f"Step {i+1}: Battery {status['battery_level']:.1f}%, "
                  f"Solar {status['solar_voltage']:.1f}V, "
                  f"Charging: {'Yes' if status['is_charging'] else 'No'}")
            
            # Toggle devices for testing
            if i == 2:
                generator.control_device('light', True)
                print("  → Light turned ON")
            elif i == 4:
                generator.control_device('light', False)
                print("  → Light turned OFF")
                
            time.sleep(1)
            
        print("✓ Simulation completed successfully")
        return True
        
    except Exception as e:
        print(f"✗ Simulation Error: {e}")
        return False

def main():
    print("=" * 50)
    print("  PORTABLE SOLAR GENERATOR - SYSTEM TEST")
    print("  MS Engineering College Final Year Project")
    print("=" * 50)
    
    tests = [
        test_solar_controller,
        test_hardware_config,
        test_mobile_app,
        test_remote_control,
        run_simulation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        time.sleep(0.5)  # Brief pause between tests
    
    print("\n" + "=" * 50)
    print(f"TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All systems operational!")
        print("✓ Ready to run main application: python main.py")
    else:
        print("⚠ Some components need attention")
        print("  Check error messages above and install missing dependencies")
    
    print("=" * 50)

if __name__ == "__main__":
    main()