# Local Network Chat

This is a simple local network chat application that allows multiple clients to connect to a server and exchange messages. The server also filters out messages containing bad words and logs all messages.

## Requirements

- Python 3.x
- `colorama` library

You can install the required library using pip:

```sh
pip install colorama
```

## Usage

1. **Run the server**:

    ```sh
    python server.py
    ```

2. **Run the client**:

    ```sh
    python chat.py
    ```

## Script Details

- **Server**: The server script (`server.py`) handles multiple client connections using threading. It filters out messages containing bad words and logs all messages to `data/server_logs.txt`.
- **Client**: The client script (`chat.py`) connects to the server and allows the user to send and receive messages.

## Example `badwords.txt`

```
badword1
badword2
badword3
```

## Example `server_logs.txt`

```
2023-10-01 12:00:00  |  hostname - 192.168.100.108 - 5555 >>> connected
2023-10-01 12:01:00  |  hostname - 192.168.100.108 - 5555 >>> Hello, world!
2023-10-01 12:02:00  |  hostname - 192.168.100.108 - 5555 >>> Bad word detected: badword1
2023-10-01 12:03:00  |  hostname - 192.168.100.108 - 5555 >>> disconnected
```

## Notes

- Ensure that the server and client scripts are running on the same local network.
- Update the IP address and port number in the scripts if necessary.
