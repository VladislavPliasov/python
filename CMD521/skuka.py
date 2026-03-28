while True:
    number = int(input("Введи число от 1 до 9: "))
    
    if number < 1 or number > 9:
        print("Введи число от 1 до 9 включительно")
    else:
        for i in range(1, 10):
            print(f"{i} x {number} = {i * number}")
        break