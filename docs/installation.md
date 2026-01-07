# Installation and Setup Guide
## Portable Solar Power Generator

### System Requirements
- Python 3.7 or higher
- Windows/Linux/macOS
- Minimum 100MB free space

### Installation Steps

#### 1. Clone/Download Project
```bash
# If using git
git clone <repository-url>
cd portable_solar_generator

# Or extract downloaded ZIP file
```

#### 2. Install Python Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Or install individually
pip install keyboard
pip install pyserial
```

#### 3. Hardware Setup (if using real hardware)
- Connect solar panel to charge controller
- Connect battery to charge controller
- Connect load devices (lights, fan, USB charger) through relays
- Connect microcontroller (Arduino/Raspberry Pi) to control relays
- Connect voltage/current sensors for monitoring

#### 4. Run the Application
```bash
# Start main application
python main.py

# Or run specific interfaces directly
python mobile_app/solar_app.py          # Mobile app interface
python src/remote_control.py            # Remote control
```

### Usage Instructions

#### Mobile App Interface
1. Select option 1 from main menu
2. Use GUI buttons to control devices
3. Monitor battery status in real-time
4. View solar panel charging status

#### Remote Control Interface  
1. Select option 2 from main menu
2. Use keyboard shortcuts:
   - Press '1' to toggle light
   - Press '2' to toggle fan
   - Press '3' to toggle mobile charger
   - Press 'S' to show status
   - Press 'E' for emergency shutdown
   - Press 'Q' to quit

#### Status Monitor
1. Select option 3 from main menu
2. View real-time system status
3. Press Ctrl+C to exit

### Troubleshooting

#### Common Issues
1. **Import Error for tkinter**
   - Solution: Install tkinter: `sudo apt-get install python3-tk` (Linux)

2. **Keyboard module not found**
   - Solution: Install keyboard: `pip install keyboard`

3. **Permission denied for keyboard access**
   - Solution: Run as administrator/sudo (for remote control)

#### Hardware Issues
1. **No voltage readings**
   - Check sensor connections
   - Verify pin configurations in hardware_config.py

2. **Devices not responding**
   - Check relay connections
   - Verify power supply to relays

### Project Structure
```
portable_solar_generator/
├── main.py                 # Main application launcher
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── docs/
│   └── installation.md    # This file
├── src/
│   ├── solar_controller.py    # Main controller logic
│   └── remote_control.py      # Remote control interface
├── mobile_app/
│   └── solar_app.py          # Mobile app GUI
└── hardware/
    └── hardware_config.py    # Hardware specifications
```

### Team Contact
- **Ritik Pandey** (Team Leader) - Code review, testing, hardware
- **Rohit Ranjan** - Main developer, innovation features  
- **Nikki Kumari Yadav** - Documentation, code review
- **Om Singh** - Research, information gathering

**College**: MS Engineering College  
**Affiliated to**: Visvesvaraya Technological University