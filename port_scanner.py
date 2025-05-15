import socket
import threading
import time
from urllib.parse import urlparse

open_ports = []

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown service"
            print(f"Port {port} is open ({service})")
            open_ports.append(port)
        sock.close()
    except:
        pass

def loading_animation(duration=3):
    animation = "|/-\\"
    idx = 0
    print("Finishing scan ", end="")
    for _ in range(duration * 10):
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
    print(" " * 20, end="\r")  # Clear line

def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    loading_animation()

    if not open_ports:
        print("No open ports found in this range.")
    else:
        print(f"Scan complete. {len(open_ports)} open port(s) found.")

if __name__ == "__main__":
    user_input = input("Enter IP address or website URL (e.g. example.com or https://example.com): ")
    # Parse input to extract hostname
    parsed_url = urlparse(user_input)
    if parsed_url.scheme:
        hostname = parsed_url.hostname
    else:
        hostname = user_input

    try:
        target_ip = socket.gethostbyname(hostname)
        print(f"Resolved {hostname} to {target_ip}")
    except socket.gaierror:
        print("Could not resolve hostname. Please check the URL and try again.")
        exit(1)

    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    port_scanner(target_ip, start, end)