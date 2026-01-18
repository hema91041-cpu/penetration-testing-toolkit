import socket

def port_scanner():
    target = input("Enter target IP (example: 127.0.0.1): ")
    print("\nScanning ports...\n")

    for port in range(20, 100):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except:
            pass


def brute_force():
    print("\nStarting Brute Force Attack (Demo)\n")
    username = "admin"
    passwords = ["1234", "admin", "password", "admin123"]

    for pwd in passwords:
        print(f"Trying password: {pwd}")
        if pwd == "admin123":
            print("\n[+] Login Successful!")
            print("Username:", username)
            print("Password:", pwd)
            break


def banner_grabbing():
    target = input("Enter target IP: ")
    port = int(input("Enter port number: "))

    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024)
        print("\nBanner Info:")
        print(banner.decode())
        s.close()
    except:
        print("Banner not found")


# ---------- MAIN PROGRAM ----------
while True:
    print("\n===== PENETRATION TESTING TOOLKIT =====")
    print("1. Port Scanner")
    print("2. Brute Force Attack")
    print("3. Banner Grabbing")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        port_scanner()
    elif choice == "2":
        brute_force()
    elif choice == "3":
        banner_grabbing()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
