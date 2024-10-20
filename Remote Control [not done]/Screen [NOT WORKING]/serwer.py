import socket
import pyautogui
import pickle
import struct
import cv2
import numpy as np

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    resized_screenshot = cv2.resize(screenshot, (640, 480))  # Zmniejszenie rozdzielczości
    return resized_screenshot

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 2115))
    server_socket.listen(1)
    print("Server listening on port 2115")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        screenshot = capture_screen()
        data = pickle.dumps(screenshot)
        message_size = struct.pack("L", len(data))
        conn.sendall(message_size + data)

        click_data = conn.recv(1024)
        if click_data:
            x, y = pickle.loads(click_data)
            pyautogui.click(x, y)

if __name__ == "__main__":
    main()