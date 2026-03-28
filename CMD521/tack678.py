### bilet ###
name = input("Введи имя: ")
age = int(input("Введи возраст: "))

if age < 12:
    print(f"{name}, цена твоего билета 50грн")
elif age <= 60:
    print(f"{name}, цена твоего билета 100грн" )
else:
    print(f"{name}, цена твоего билета 70грн")


### calkulhator ###
a = int(input("Введи 1е число: "))
b = int(input("Введи 2е число: "))

if a > 0 and b > 0:
    print(f"Сумма: {a + b}")
elif a < 0 and b < 0:
    print(f"Помноженное: {a * b}")
else:
    print(f"Разница: {a - b}")


### podarok ###
zarplata = int(input("Введи свою зарплату: "))

if zarplata < 10000:
    tax = zarplata * 0.10
    print(f"Налог (10%): {tax} грн")
elif zarplata <= 20000:
    tax = zarplata * 0.15
    print(f"Налог (15%): {tax} грн")
else:
    tax = zarplata * 0.20
    print(f"Налог (20%): {tax} грн")