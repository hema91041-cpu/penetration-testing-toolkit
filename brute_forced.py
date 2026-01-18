def brute_force():
    username = "admin"
    password_list = ["1234", "admin", "password", "admin123"]

    print("\nStarting Brute Force Attack (Demo)")
    
    for password in password_list:
        print(f"Trying password: {password}")

        if password == "admin123":
            print("\n[+] Login Successful!")
            print(f"Username: {username}")
            print(f"Password: {password}")
            break
    else:
        print("\n[-] passward not found")

        if __name__=="__main__": brute_force()
