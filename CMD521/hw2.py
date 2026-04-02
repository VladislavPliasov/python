while True:
    username = input("Придумай имя: ")

    if username == "":
        print("Username cannot be empty")
        continue

    password = 0
    while password < 1000:
        password = int(input("Придумай пароль (число): "))
        if password < 1000:
            print("Weak password")

    print(f"Зареган, {username}!")

    login_user = ""
    while login_user != username:
        login_user = input("\nИмя для входа: ")
        if login_user != username:
            print("User not found")

    login_pass = 0
    while login_pass != password:
        login_pass = int(input("Пароль: "))
        if login_pass > password:
            print("Password too large")
        elif login_pass < password:
            print("Password too small")

    print("Login successful")
    break