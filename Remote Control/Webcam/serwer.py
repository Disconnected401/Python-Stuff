import socket
import cv2
import pickle
import struct

def start_server():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = "localhost"
    port = 2137

    socket_address = (host_ip, port)
    server_socket.bind(socket_address)
    server_socket.listen(5)
    print(f"Listening at: {socket_address}")

    while True:
        try:
            # Accept a connection
            client_socket, addr = server_socket.accept()
            print(f"Connection from: {addr}")

            # Capture video
            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Serialize frame
                data = pickle.dumps(frame)
                message_size = struct.pack("Q", len(data))

                # Send message size and data
                client_socket.sendall(message_size + data)

        except ConnectionResetError:
            print("Connection was reset by the client. Waiting for a new connection...")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cap.release()
            client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    start_server()