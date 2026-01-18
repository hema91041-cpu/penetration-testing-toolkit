import socket

def scan_ports(target):
    print(f"\nScanning target: {target}")
    print("Open ports:")

    for port in range(20, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is OPEN")

            sock.close()
        except:
            pass

        if __name__== "__main__": scan_ports("127.0.0.1")
