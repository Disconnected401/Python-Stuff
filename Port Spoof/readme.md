# Port Spoof

This script is designed to open multiple ports on your machine for your "security". It uses threading to handle multiple ports simultaneously and includes a gradient banner display using the `colorama` library.

## Requirements

- Python 3.x
- `colorama` library

You can install the required library using pip:

```sh
pip install colorama
```

## Usage

1. **Clone the repository**:

    ```sh
    git clone <repository-url>
    cd Port-Spoof
    ```

2. **Create a `ports.txt` file**:

    Create a file named `ports.txt` in the same directory as the script. List the ports you want to open, one per line.

3. **Run the script**:

    ```sh
    python port_spoof.py
    ```

## Script Details

- **Banner Display**: The script displays a gradient banner using the `colorama` library.
- **Port Opening**: It reads the ports from `ports.txt` and opens each port in a separate thread.

## Example `ports.txt`

```
8080
9090
10000
```