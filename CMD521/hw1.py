exit = 1

while exit != 0:
    username = input("Придумай имя: ")

    if username == "":
        print("Имя пользователя не может быть пустым")
    else:
        password = 0
        while password < 1000:
            password = int(input("Придумай пароль (число): "))
            if password < 1000:
                print("Простой пароль")

        print(f"Зареган, {username}!")

        login_user = ""
        while login_user != username:
            login_user = input("\nИмя для входа: ")
            if login_user != username:
                print("Несуществующий пользователь")

        login_pass = 0
        while login_pass != password:
            login_pass = int(input("Пароль: "))
            if login_pass != password:
                print("Неправильный пароль")

        print("Логин успешен")
        exit = 0