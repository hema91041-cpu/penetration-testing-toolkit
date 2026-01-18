import socket

def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))
        banner = sock.recv(1024)
        print("\nBanner Information:")
        print(banner.decode().strip())
        sock.close()
    except:
        print("Could not retrieve banner")
