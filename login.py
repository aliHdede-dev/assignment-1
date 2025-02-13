username = input("Enter username: ")
password = int(input("Enter password: "))

if username == "admin" and password == 123456:
    print("Login success")
else:
    print("Login failed")