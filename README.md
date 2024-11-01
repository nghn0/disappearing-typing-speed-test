# Disappearing Typing Speed Test

## Description
A simple desktop application that allows users to test their typing speed with a unique "death timer" feature. If users do not press any keys within a specified time frame, the application notifies them that they took too long to type.

## Features
- **Typing Timer**: Users have a limited time to type before the application signals a timeout.
- **Real-time Key Tracking**: The application listens for key presses and updates the timer accordingly.
- **Notification System**: Users receive a notification if they exceed the allowed typing time.
- **User-Friendly Interface**: Designed with Tkinter for an intuitive experience.

## Technologies
- **Frontend**: Python with Tkinter for the graphical user interface.
- **Keyboard Monitoring**: Pynput library for tracking key presses and handling events.
- **Threading**: Utilizes Python's threading to manage background tasks effectively.

## Usage
1. Run the application in a Python environment with the necessary dependencies installed.
2. Click the "Start" button to begin the typing session.
3. Type in the provided text area, ensuring to press keys within the allowed time limit.
4. If you exceed the time without typing, a notification will alert you.

## Notes
This project showcases a unique approach to testing typing speed with a time constraint. It demonstrates the integration of real-time keyboard monitoring and GUI development in Python. It's an excellent resource for learning about event handling and multithreading in desktop applications.
