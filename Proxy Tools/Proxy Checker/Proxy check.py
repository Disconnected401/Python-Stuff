import requests
import time

logo = """


            dMMMMb  dMMMMb  .aMMMb  dMP dMP dMP dMP        .aMMMb  dMP dMP dMMMMMP .aMMMb  dMP dMP dMMMMMP dMMMMb 
           dMP.dMP dMP.dMP dMP"dMP dMK.dMP dMP.dMP        dMP"VMP dMP dMP dMP     dMP"VMP dMP.dMP dMP     dMP.dMP 
          dMMMMP" dMMMMK" dMP dMP .dMMMK"  VMMMMP        dMP     dMMMMMP dMMMP   dMP     dMMMMK" dMMMP   dMMMMK"  
         dMP     dMP"AMF dMP.aMP dMP"AMF dA .dMP        dMP.aMP dMP dMP dMP     dMP.aMP dMP"AMF dMP     dMP"AMF   
        dMP     dMP dMP  VMMMP" dMP dMP  VMMMP"         VMMMP" dMP dMP dMMMMMP  VMMMP" dMP dMP dMMMMMP dMP dMP    
"""

def check_proxy(proxy, protocol):
    try:
        response = requests.get('http://www.google.com', proxies={protocol: proxy}, timeout=1)
        return response.status_code == 200
    except:
        return False

def main():
    print("Proxy Checker\n")
    print("1. Display proxies and save all to valid.txt")
    print("2. Display proxies and save separately to http-valid.txt and https-valid.txt")
    print("3. Remove duplicate proxies, sort by first part of IP, and save to unique.txt\n")
    option = input(">>>")

    with open('list.txt', 'r') as file:
        proxies = file.readlines()

    proxies = [proxy.strip() for proxy in proxies]
    unique_proxies = list(set(proxies))
    unique_proxies.sort(key=lambda x: int(x.split('.')[0]))

    if option == '3':
        with open('unique.txt', 'w') as unique_file:
            for proxy in unique_proxies:
                unique_file.write(proxy + '\n')
        print("Duplicates removed, proxies sorted by first part of IP, and saved to unique.txt")
        return

    num_proxies = len(unique_proxies)
    timeout = 1  # seconds
    estimated_time = num_proxies * timeout
    minutes, seconds = divmod(estimated_time, 60)

    print(f"Proxies: {num_proxies}")
    print(f"Timeout: {timeout} seconds")
    print(f"Estimated time: {minutes} minutes and {seconds} seconds\n")

    valid_proxies = []
    http_proxies = []
    https_proxies = []

    start_time = time.time()
    for proxy in unique_proxies:
        if check_proxy(proxy, 'http'):
            http_proxies.append(proxy)
            valid_proxies.append(proxy)
            print(f"Valid HTTP proxy: {proxy}")
            if option == '1':
                with open('valid.txt', 'a') as valid_file:
                    valid_file.write(proxy + '\n')
            elif option == '2':
                with open('http-valid.txt', 'a') as http_file:
                    http_file.write(proxy + '\n')
        elif check_proxy(proxy, 'https'):
            https_proxies.append(proxy)
            valid_proxies.append(proxy)
            print(f"Valid HTTPS proxy: {proxy}")
            if option == '1':
                with open('valid.txt', 'a') as valid_file:
                    valid_file.write(proxy + '\n')
            elif option == '2':
                with open('https-valid.txt', 'a') as https_file:
                    https_file.write(proxy + '\n')
        else:
            print(f"Invalid proxy: {proxy}")
    end_time = time.time()

    elapsed_time = end_time - start_time
    elapsed_minutes, elapsed_seconds = divmod(elapsed_time, 60)
    print(f"\nElapsed time: {int(elapsed_minutes)} minutes and {int(elapsed_seconds)} seconds")

if __name__ == "__main__":
    print(logo)
    while True:
        main()