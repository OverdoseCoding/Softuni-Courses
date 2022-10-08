username = input()
password = input()
password1 = input

while password1 != password:
    password1 = input()
    if password1 == password:
        print(f"Welcome {username}!")