# Simple HTTP Server

This is a simple HTTP server script written in Python. It uses the `http.server` module to serve files from a directory and logs requests to a file.

## Features

- Serves files from the `web` directory.
- Logs HTTP requests to `server.log`.
- Configurable port (default is 80).
- Everyone can connect to your website (if they have access to your localhost)

## Requirements

- Python 3.x

## Usage

1. Place the files you want to serve in a directory named `web`.
2. Run the script:

    ```sh
    python serwer.py
    ```

3. Open your web browser and navigate to `http://localhost:80`.

## Logging

All HTTP requests are logged to `server.log` with timestamps.

## Customization

- To change the port, modify the `port` variable in the script.
- To change the directory being served, modify the `directory` parameter in the `CustomHTTPRequestHandler` class.