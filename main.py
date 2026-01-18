import port_scanner
import brute_forcer
import banner_grabber

def menu():
    print("\n====== PENETRATION TESTING TOOLKIT ======")
    print("1. Port Scanner")
    print("2. Brute Force Attack (Demo)")
    print("3. Banner Grabbing")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        target = input("Enter target IP (e.g. 127.0.0.1): ")
        port_scanner.scan_ports(target)

    elif choice == "2":
        brute_forcer.brute_force()

    elif choice == "3":
        target = input("Enter target IP: ")
        port = int(input("Enter port number: "))
        banner_grabber.grab_banner(target, port)

    elif choice == "4":
        print("Exiting Toolkit...")
        break

    else:
        print("Invalid choice!")

