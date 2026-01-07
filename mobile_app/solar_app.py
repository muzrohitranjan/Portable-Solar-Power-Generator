import tkinter as tk
from tkinter import ttk
import json
import threading
import time
from solar_controller import generator

class SolarGeneratorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Solar Power Generator Control")
        self.root.geometry("400x500")
        self.root.configure(bg='#2c3e50')
        
        self.setup_ui()
        self.update_display()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Portable Solar Generator", 
                        font=('Arial', 16, 'bold'), 
                        bg='#2c3e50', fg='white')
        title.pack(pady=10)
        
        # Battery Status Frame
        battery_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2)
        battery_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(battery_frame, text="Battery Status", 
                font=('Arial', 12, 'bold'), bg='#34495e', fg='white').pack(pady=5)
        
        self.battery_label = tk.Label(battery_frame, text="Battery: 0%", 
                                     font=('Arial', 11), bg='#34495e', fg='#2ecc71')
        self.battery_label.pack()
        
        self.solar_label = tk.Label(battery_frame, text="Solar: 0V", 
                                   font=('Arial', 11), bg='#34495e', fg='#f39c12')
        self.solar_label.pack()
        
        self.charging_label = tk.Label(battery_frame, text="Status: Not Charging", 
                                      font=('Arial', 11), bg='#34495e', fg='#e74c3c')
        self.charging_label.pack(pady=(0,10))
        
        # Device Control Frame
        control_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2)
        control_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(control_frame, text="Device Control", 
                font=('Arial', 12, 'bold'), bg='#34495e', fg='white').pack(pady=5)
        
        # Light Control
        light_frame = tk.Frame(control_frame, bg='#34495e')
        light_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(light_frame, text="Light:", font=('Arial', 10), 
                bg='#34495e', fg='white').pack(side='left')
        
        self.light_button = tk.Button(light_frame, text="OFF", 
                                     command=lambda: self.toggle_device('light'),
                                     bg='#e74c3c', fg='white', width=8)
        self.light_button.pack(side='right')
        
        # Fan Control
        fan_frame = tk.Frame(control_frame, bg='#34495e')
        fan_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(fan_frame, text="Fan:", font=('Arial', 10), 
                bg='#34495e', fg='white').pack(side='left')
        
        self.fan_button = tk.Button(fan_frame, text="OFF", 
                                   command=lambda: self.toggle_device('fan'),
                                   bg='#e74c3c', fg='white', width=8)
        self.fan_button.pack(side='right')
        
        # Mobile Charger Control
        charger_frame = tk.Frame(control_frame, bg='#34495e')
        charger_frame.pack(fill='x', padx=10, pady=(5,15))
        
        tk.Label(charger_frame, text="Mobile Charger:", font=('Arial', 10), 
                bg='#34495e', fg='white').pack(side='left')
        
        self.charger_button = tk.Button(charger_frame, text="OFF", 
                                       command=lambda: self.toggle_device('mobile_charger'),
                                       bg='#e74c3c', fg='white', width=8)
        self.charger_button.pack(side='right')
        
        # Emergency Button
        emergency_button = tk.Button(self.root, text="EMERGENCY SHUTDOWN", 
                                   command=self.emergency_shutdown,
                                   bg='#c0392b', fg='white', 
                                   font=('Arial', 12, 'bold'))
        emergency_button.pack(pady=20)
        
    def toggle_device(self, device):
        current_state = generator.devices[device]
        new_state = not current_state
        
        if generator.control_device(device, new_state):
            self.update_device_buttons()
        
    def emergency_shutdown(self):
        generator.emergency_shutdown()
        self.update_device_buttons()
        
    def update_device_buttons(self):
        # Update Light button
        if generator.devices['light']:
            self.light_button.config(text="ON", bg='#27ae60')
        else:
            self.light_button.config(text="OFF", bg='#e74c3c')
            
        # Update Fan button
        if generator.devices['fan']:
            self.fan_button.config(text="ON", bg='#27ae60')
        else:
            self.fan_button.config(text="OFF", bg='#e74c3c')
            
        # Update Charger button
        if generator.devices['mobile_charger']:
            self.charger_button.config(text="ON", bg='#27ae60')
        else:
            self.charger_button.config(text="OFF", bg='#e74c3c')
    
    def update_display(self):
        status = generator.get_status()
        
        # Update battery display
        battery_percent = status['battery_level']
        self.battery_label.config(text=f"Battery: {battery_percent}%")
        
        # Update solar display
        solar_voltage = status['solar_voltage']
        self.solar_label.config(text=f"Solar: {solar_voltage}V")
        
        # Update charging status
        if status['is_charging']:
            self.charging_label.config(text="Status: Charging", fg='#2ecc71')
        else:
            self.charging_label.config(text="Status: Not Charging", fg='#e74c3c')
            
        # Update device buttons
        self.update_device_buttons()
        
        # Schedule next update
        self.root.after(1000, self.update_display)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SolarGeneratorApp()
    app.run()