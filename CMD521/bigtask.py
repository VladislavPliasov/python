apartments = []

while True:
    choice = int(input("\n1 - Добавить\n2 - Удалить\n3 - Редактировать\n4 - Показать все\n5 - Самая дешевая\n6 - Самая дорогая\n7 - От дешевой\n8 - От дорогой\n0 - Выход\n"))

    if choice == 0:
        break

    elif choice == 1:
        name = input("Название: ")
        price = int(input("Цена: "))
        apartments.append([name, price])
        print("Добавлено!")

    elif choice == 2:
        name = input("Какую удалить: ")
        for apt in apartments:
            if apt[0] == name:
                apartments.remove(apt)
                print("Удалено!")
                break
        else:
            print("Не найдено")

    elif choice == 3:
        name = input("Какую редактировать: ")
        for apt in apartments:
            if apt[0] == name:
                apt[0] = input("Новое название: ")
                apt[1] = int(input("Новая цена: "))
                print("Обновлено!")
                break
        else:
            print("Не найдено")

    elif choice == 4:
        for apt in apartments:
            print(f"{apt[0]} - {apt[1]}")

    elif choice == 5:
        cheap = min(apartments, key=lambda x: x[1])
        print(f"Самая дешевая: {cheap[0]} - {cheap[1]}")

    elif choice == 6:
        expensive = max(apartments, key=lambda x: x[1])
        print(f"Самая дорогая: {expensive[0]} - {expensive[1]}")

    elif choice == 7:
        for apt in sorted(apartments, key=lambda x: x[1]):
            print(f"{apt[0]} - {apt[1]}")

    elif choice == 8:
        for apt in sorted(apartments, key=lambda x: x[1], reverse=True):
            print(f"{apt[0]} - {apt[1]}")

    else:
        print("Неверный выбор")