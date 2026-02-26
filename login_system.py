users = {}

def register():
username = input("Enter username: ")
password = input("Enter password: ")
users[username] = password
print("User registered successfully!")

def login():
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")
def main():
while True:
choice = input("Register (r), Login (l), or Quit (q): ").lower()

    if choice == "r":
        register()
    elif choice == "l":
        login()
    elif choice == "q":
        break
    else:
        print("Invalid option.")
