# 20-20-20 Eye Care Timer

**Version:** 2025  
**Platform:** Windows, Linux, macOS

---

## Description

20-20-20 Eye Care Timer is a simple app that reminds you to rest your eyes every 20 minutes. Even if you close the main window, the app continues running in the background and triggers a **full-screen 20-second break** to protect your eyes.

---

## Features

- Automatic **20-minute reminders**
- Full-screen **20-second break** for eye rest
- Runs in the background even when the window is closed
- Three main buttons in the UI:
  - **Exit:** Completely closes the app (stops background running)
  - **Pause:** Temporarily pauses the countdown timer
  - **Resume:** Resumes the countdown if paused

---

## Installation & Setup

### Windows Users

1. **Download the app**
   - Download & Extract zip
   - open the dist folder
   - Place `dist/20_20_20.exe` in a folder of your choice (e.g., `C:\Apps\20_20_20`).

2. **Create Startup Shortcut (For AutoStart)**

   - Press `Win + R`, type `shell:startup`, and press Enter
   - Copy a **shortcut** of `20_20_20.exe` into this Startup folder
   - The app will now **start automatically when Windows boots**

---

### Linux & macOS Users

1. **Download the Python version**

   - Place `src/20_20_20.py` in a folder you prefer

2. **Run with Python 3**
   ```bash
   python3 /path/to/20_20_20.py
   ```

3. **Auto-start the app at login**

### Linux (using `.config/autostart`)

1. Create a file `~/.config/autostart/20_20_20.desktop` with the following content:

   ```ini
   [Desktop Entry]
   Type=Application
   Exec=python3 /path/to/20_20_20.py
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   Name=20-20-20 Eye Care Timer
   Comment=Automatically starts the Eye Care Timer at login
2. Save the file. The app will start automatically on login.

### macOS (using Login Items or Automator)

1. Open System Preferences → Users & Groups → Login Items
2. Click + and select your `src/20_20_20.py` or a Python launcher script
3. The app will now start automatically on login.