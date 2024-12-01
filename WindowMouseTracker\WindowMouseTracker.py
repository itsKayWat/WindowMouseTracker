import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard
import win32gui
import win32api
from threading import Thread
import time
import os

class CoordinateTracker:
    def __init__(self):
        # Hide console window on Windows
        if os.name == 'nt':
            import win32con
            import win32gui
            console_window = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(console_window, win32con.SW_HIDE)
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Coordinate Tracker")
        self.root.geometry("300x200")
        
        # Configure dark theme
        self.root.configure(bg='#2b2b2b')
        style = ttk.Style()
        style.configure('Dark.TCheckbutton', 
                       background='#2b2b2b',
                       foreground='white')
        
        # Set window icon (shows in taskbar)
        self.root.iconify()  # Minimize to taskbar on start
        
        # Create tracking state variable
        self.tracking_enabled = tk.BooleanVar(value=True)
        
        # Setup keyboard shortcut
        keyboard.add_hotkey('alt+\'', self.toggle_tracking)
        
        # Create coordinate display window
        self.coord_window = tk.Toplevel(self.root)
        self.coord_window.withdraw()  # Hide initially
        self.coord_window.overrideredirect(True)  # Remove window decorations
        self.coord_label = tk.Label(self.coord_window,
                                  bg='black',
                                  fg='yellow',
                                  font=('Arial', 10))
        self.coord_label.pack()
        
        self.setup_ui()
        self.start_tracking_thread()
        
    def toggle_tracking(self):
        # Toggle the tracking state
        self.tracking_enabled.set(not self.tracking_enabled.get())
        
    def setup_ui(self):
        # Create and pack widgets
        title_label = tk.Label(self.root,
                             text="Coordinate Tracker",
                             bg='#2b2b2b',
                             fg='white',
                             font=('Arial', 14, 'bold'))
        title_label.pack(pady=(20,15))
        
        toggle_check = ttk.Checkbutton(self.root,
                                     text="Show Coordinates",
                                     style='Dark.TCheckbutton',
                                     variable=self.tracking_enabled)
        toggle_check.pack(pady=15)
        
        # Updated Instructions
        instructions = tk.Label(self.root,
                              text="Alt+' to toggle tracking\nClose window to exit",
                              bg='#2b2b2b',
                              fg='#888888')
        instructions.pack(pady=(10,20))
                
    def update_coordinates(self):
        while True:
            if self.tracking_enabled.get():
                # Get mouse position and window info
                x, y = pyautogui.position()
                window = win32gui.WindowFromPoint((x, y))
                rect = win32gui.GetWindowRect(window)
                
                # Calculate relative coordinates
                rel_x = x - rect[0]
                rel_y = y - rect[1]
                
                # Update coordinate display
                self.coord_label.configure(text=f"x: {rel_x}, y: {rel_y}")
                
                # Position coordinate window near cursor
                self.coord_window.geometry(f"+{x+20}+{y+20}")
                self.coord_window.deiconify()
                self.coord_window.lift()
            else:
                self.coord_window.withdraw()
                
            time.sleep(0.1)
    
    def start_tracking_thread(self):
        # Start coordinate tracking in separate thread
        tracking_thread = Thread(target=self.update_coordinates, daemon=True)
        tracking_thread.start()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CoordinateTracker()
    app.run()