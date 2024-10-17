import socket
import pickle
import struct
import cv2
import numpy as np

def receive_screen(conn):
    data = b""
    payload_size = struct.calcsize("L")
    while len(data) < payload_size:
        packet = conn.recv(4096)
        if not packet:
            return None
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        packet = conn.recv(4096)
        if not packet:
            return None
        data += packet
    frame_data = data[:msg_size]
    frame = pickle.loads(frame_data)
    return frame

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        click_data = pickle.dumps((x, y))
        param.sendall(click_data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 2115))

    cv2.namedWindow("Screen")
    cv2.setMouseCallback("Screen", click_event, client_socket)

    while True:
        frame = receive_screen(client_socket)
        if frame is None:
            break
        frame = np.array(frame)
        cv2.imshow("Screen", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()