import json
import os
import hashlib

FILE_NAME = "users.json"

# Create users file if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump({}, f)

def load_users():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)

# Hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    users = load_users()
    username = input("Enter username: ")

    if username in users:
        print("❌ Username already exists!")
        return

    password = input("Enter password: ")
    hashed_password = hash_password(password)

    users[username] = hashed_password
    save_users(users)

    print("✅ Registration successful!")

def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    if username in users and users[username] == hashed_password:
        print("🎉 Login successful! Welcome,", username)
    else:
        print("❌ Invalid username or password")

def menu():
    initialize_file()
    while True:
        print("\n===== Secure User Login System =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice")

menu()
