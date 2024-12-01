RelativeMouseCoords - Window-Relative Mouse Coordinate Tracker
===========================================================

Purpose:
--------
RelativeMouseCoords is a utility tool that tracks and displays mouse coordinates relative to the current window position. This is particularly useful for developers working on UI automation, testing, or anyone needing precise cursor positions within application windows.

Features:
---------
- Real-time coordinate tracking
- Window-relative positioning
- Dark mode interface
- Hotkey toggle (Alt+')
- Minimalistic floating display
- System tray integration

Use Cases:
----------
1. UI Automation Development:
   - Recording click positions for automated testing
   - Developing automation scripts
   - Debugging UI layouts

2. Design & Development:
   - Measuring UI element positions
   - Verifying element alignment
   - Layout troubleshooting

3. General Usage:
   - Precise cursor positioning
   - UI element mapping
   - Screen coordinate documentation

Installation:
------------
1. Ensure Python 3.6+ is installed
2. Clone the repository
3. Run requirements.py to install dependencies
   OR
   Run: pip install -r requirements.txt

Required Dependencies:
--------------------
- pyautogui
- keyboard
- pywin32
- pystray
- pillow

Usage:
------
1. Run mouse_tracker.py
2. The tool minimizes to system tray
3. Use Alt+' to toggle coordinate display
4. Coordinates appear near cursor position
5. Close main window to exit

Example Scenario:
---------------
A developer is creating an automation script for a desktop application. They need to know the exact coordinates of buttons and UI elements relative to the application window. Using RelativeMouseCoords, they can:

1. Open their target application
2. Run RelativeMouseCoords
3. Hover over UI elements
4. Record the displayed coordinates
5. Use these coordinates in their automation script

This saves time compared to manual coordinate calculation and ensures accuracy in UI interaction scripts.