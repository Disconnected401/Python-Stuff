import socket
import threading
import time
from colorama import Fore
import datetime

# Zmienne jako kolory 
W = Fore.WHITE
G = Fore.LIGHTGREEN_EX
R = Fore.LIGHTRED_EX


def print_gradient_text(text, start_color, end_color):
    num_steps = len(text)
    for i in range(num_steps):
        ratio = i / (num_steps - 1)
        color = (
            int(start_color[0] + (end_color[0] - start_color[0]) * ratio),
            int(start_color[1] + (end_color[1] - start_color[1]) * ratio),
            int(start_color[2] + (end_color[2] - start_color[2]) * ratio),
        )
        gradient_color = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
        print(f"{gradient_color}{text[i]}", end="", flush=True)
        time.sleep(0.0001)
    print("\033[0m")


# Więcej kolorów
start_color = (255, 0, 0)
end_color = (255, 111, 0)

logo_text = r"""
______ _            _      _    _       _ _   _____                          
| ___ \ |          | |    | |  | |     | | | /  ___|                         
| |_/ / | __ _  ___| | __ | |  | | __ _| | | \ `--.  ___ _ ____   _____ _ __ 
| ___ \ |/ _` |/ __| |/ / | |/\| |/ _` | | |  `--. \/ _ \ '__\ \ / / _ \ '__|
| |_/ / | (_| | (__|   <  \  /\  / (_| | | | /\__/ /  __/ |   \ V /  __/ |   
\____/|_|\__,_|\___|_|\_\  \/  \/ \__,_|_|_| \____/ \___|_|    \_/ \___|_|
"""

print_gradient_text(logo_text, start_color, end_color)

active_connections = []

with open('data/badwords.txt', 'r') as f:
    badwords = [word.lower() for word in f.read().splitlines()]

def log_message(message):
    with open('data/server_logs.txt', 'a', encoding='utf-8') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp}  |  {message}\n")

def handle_client(client_socket, addr):
    try:
        hostname = socket.gethostbyaddr(addr[0])[0]
        print(f"{hostname} - {addr[1]} >>> {G}connected{W}")
        log_message(f"{hostname} - {addr[0]} - {addr[1]} >>> connected")
        active_connections.append(client_socket)
        
        while True:
            data = client_socket.recv(1024).decode('utf-8').strip()
            if not data:
                break
            
            if any(badword in data.lower() for badword in badwords):
                message = data.split(">>> ")[1]
                print(f"{hostname} - {addr[1]} >>> {R}{message}{W}")
                log_message(f"{hostname} - {addr[0]} - {addr[1]} >>> Bad word detected: {message}")
                continue
            
            for connection in active_connections:
                if connection != client_socket:
                    connection.send(f"{hostname} >>> {data}\n".encode('utf-8'))

            message = data.split(">>> ")[1] if ">>> " in data else " "
            log_message(f"{hostname} - {addr[0]} - {addr[1]} >>> {message}")

    except Exception as e:
        pass
    finally:
        print(f"{hostname} - {addr[1]} >>> {R}disconnected{W}")
        log_message(f"{hostname} - {addr[0]} - {addr[1]} >>> disconnected")
        active_connections.remove(client_socket)

def start_server():
    host = 'localhost' # Enter your local host IP address here or leave it as is
    port = 5555 # Enter the port number here or leave it as is

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    try:
        while True:
            client_socket, addr = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        server_socket.close()

if __name__ == "__main__":
    start_server()