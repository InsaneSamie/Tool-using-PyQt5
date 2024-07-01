# Tool-using-PyQt5


This project is a GUI application built using PyQt5, replicating a similar layout and functionality as a previously created Tkinter application. The application features a menu bar, two side-by-side frames, a profile icon in the top-right corner, and a console output area at the bottom.

https://github.com/InsaneSamie/Tool-using-PyQt5/assets/101932418/f4227770-c986-47f2-9fcf-4ddadfb5e0a7

## Features

- **Menu Bar:** Contains multiple menus including File, Edit, View, Generate, Export, and Help with various actions.
- **Profile Icon:** Displays a profile icon in the top-right corner of the window.
- **Console Output:** Displays messages in a console area at the bottom of the window.
- **Side-by-Side Frames:** Two frames are placed side by side with buttons to add messages to the console.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using pip:
    ```sh
    pip install PyQt5
    ```

## Usage

1. Ensure you have a profile image at the specified path in the code (`c:/Users/winne/Desktop/DID INTERN/CDAC/Project 2/Code/Python tkinter/Login/logo.png`). Update the path if necessary.
2. Run the application:
    ```sh
    python 3.py
    ```

## Code Overview

- **MainWindow Class:** 
  - Initializes the main window, sets up the menu bar, and creates the layout.
  - Contains methods for creating the menu and adding messages to the console.

- **create_menu Method:**
  - Sets up the menu bar with various actions for File, Edit, View, Generate, Export, and Help menus.

- **add_to_console Method:**
  - Adds messages to the console area.

## File Structure

- **3.py**: The main application script which sets up the GUI, menus, profile icon, console, and interactive buttons.
- **logo.png**: Contains the profile icon image.

## Conclusion

This application serves as a template for creating sophisticated GUI applications with `PyQt5`. It demonstrates key functionalities such as menu handling, image integration, and dynamic console output, providing a foundation for further development and customization.
