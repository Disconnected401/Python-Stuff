# Remote Control

This folder contains scripts for remote control functionalities, including screen sharing and webcam streaming.

## Structure

- **Screen [NOT WORKING]/**
  - `controler.py`: Client script to receive and display the screen stream, and send click events.
  - `serwer.py`: Server script to capture the screen and send it to the client.

- **Webcam/**
  - `controler.py`: Client script to receive and display the webcam stream.
  - `serwer.py`: Server script to capture the webcam feed and send it to the client.

## Requirements

- Python 3.x
- `opencv-python` library
- `numpy` library
- `pyautogui` library (for screen sharing)

You can install the required libraries using pip:

```sh
pip install opencv-python numpy pyautogui