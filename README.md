# 20-20-20 Eye Care

A simple GUI application built with Python and Tkinter to help users take breaks and care for their eyes while working on a computer.

## Features

- Reminds the user to look at an object 20 feet away for 20 seconds every 20 minutes.
- Displays a notification window with a moving object that the user can focus on.
- Provides a shortcut to launch the application on startup.

## Installation

### Windows

1. Download the executable file (`20-20-20_eye_care.exe`) from the [latest release](https://github.com/your-username/20-20-20-eye-care/releases/latest).
2. Create a shortcut for the executable file and place it in the `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` directory to launch the application on startup.

### Linux

1. Download the Python script (`20-20-20_eye_care.py`) from the [latest release](https://github.com/your-username/20-20-20-eye-care/releases/latest).
2. Install the required dependencies:
   - `sudo apt-get install python3 python3-tk`
3. Convert the Python script to a standalone executable using PyInstaller:
   - `pip install pyinstaller`
   - `pyinstaller --onefile 20-20-20_eye_care.py`
4. Create a shortcut for the executable file (located in the `dist` directory) and place it in the user's startup directory (e.g., `~/.config/autostart/`) to launch the application on startup.

## Usage

1. Launch the "20-20-20 Eye Care" application.
2. The application will display a notification window with a moving object every 20 minutes.
3. Look at the moving object for 20 seconds to give your eyes a break.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/eyuel-stack/20-20-20-Eye-care-timer).
