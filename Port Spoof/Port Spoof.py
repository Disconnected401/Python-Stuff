from colorama import Fore
import threading
import socket
import time
import os

os.system('cls')
os.system('title [              Port Spoof              ]')

R = Fore.RED
G = Fore.GREEN
W = Fore.WHITE

logo = f"""









                                      ▄▄▄·      ▄▄▄  ▄▄▄▄▄    .▄▄ ·  ▄▄▄·            ·▄▄▄
                                     ▐█ ▄█▪     ▀▄ █·•██      ▐█ ▀. ▐█ ▄█▪     ▪     ▐▄▄·
                                      ██▀· ▄█▀▄ ▐▀▀▄  ▐█.▪    ▄▀▀▀█▄ ██▀· ▄█▀▄  ▄█▀▄ ██▪ 
                                     ▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·    ▐█▄▪▐█▐█▪·•▐█▌.▐▌▐█▌.▐▌██▌.
                                     .▀    ▀█▄▀▪.▀  ▀ ▀▀▀      ▀▀▀▀ .▀    ▀█▄▀▪ ▀█▄▀▪▀▀▀ 
                                                    BY > DISCONNECTED401
"""


def generate_banner(logo, color1, color2):
        gradient = ""
        for i in range(len(logo)):
            ratio = i / (len(logo) - 1)
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            gradient += f"\033[38;2;{r};{g};{b}m{logo[i]}"
        return gradient

color1 = (150, 150, 150)
color2 = (50, 50, 50)
banner_with_gradient = generate_banner(logo, color1, color2)
print(banner_with_gradient)
print(f"                                                         {G}ONLINE{W}")
print("""









""")

def open_port(port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            time.sleep(5)

        except Exception as e:
            pass
        finally:
            pass

def open_all_ports():
    with open(r'.\ports.txt', 'r') as file:
        ports = file.read().splitlines()

    threads = []
    for port in ports:
        thread = threading.Thread(target=open_port, args=(int(port),))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

open_all_ports()