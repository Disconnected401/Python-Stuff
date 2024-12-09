# IP Camera Connect

This Python script connects to an IP camera using the RTSP protocol, displays the video stream in a window, and detects motion with adjustable sensitivity. The window size can also be resized by a percentage value.

## How the Software Works

1. The script connects to the IP camera using the provided IP address and port.
2. It reads frames from the camera and performs motion detection using frame differencing.
3. The sensitivity of motion detection can be adjusted by changing the `sensitivity` parameter.
4. The window displaying the video stream can be resized by a percentage value using the `resize_factor` parameter.
5. The script will close if the 'q' key is pressed or if the window is closed using the window's close button.

## Requirements

- Python 3.x
- OpenCV

## Installation

To install the required packages, run the following command:

```sh
pip install opencv-python
```