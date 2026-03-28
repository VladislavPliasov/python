correct_pin = 1234
exit = 1

while exit != 0:
    pin = int(input("Введите PIN: "))

    if pin == correct_pin:
        print("Доступ получен \nПроще не придумал?")
        balance = 1000

        while exit != 0:
            choice = int(input("\n1 - БАланс\n2 - Депозит\n3 - Снять\n0 - Свалить и не позорится\n"))

            if choice == 0:
                exit = 0
            elif choice == 1:
                print(f"Уровень нищеты: {balance}")
            elif choice == 2:
                amount = int(input("Скок надо?: "))
                balance += amount
            elif choice == 3:
                amount = int(input("Скок надо? "))
                if amount > balance:
                    print("Денег нет братан")
                else:
                    balance -= amount
            else:
                print("Ошибка")

    elif pin > correct_pin:
        print("PIN большой слишком")
    elif pin < correct_pin:
        print("PIN слишком маленький")
    else:
        print("Забыл?")