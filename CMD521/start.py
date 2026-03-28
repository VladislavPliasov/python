print("Hello, what is your name?")
name = input("Enter your name: ")
print(f"Hello {name}")
print(type(name))

print("Enter 2 digits.")
first = int(input("Enter first digit: "))
scnd = int(input("Enter second digit: "))
sum = first + scnd
print(f"Result is {sum}")

if first > scnd:
    print(f"{first} > {scnd}")
elif first < scnd:
    print(f"{first} < {scnd}")
else:
    print(f"{first} = {scnd}")

### pervaya ###
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

### vtoraya ###
print(f"Difference: {first - scnd}")

### tretyaya + creativnost###
ageP1 = int(input("Enter age of 1st person: "))
ageP2 = int(input("Enter age of 2nd person: "))
if ageP1 > ageP2:
    print(f"1st person is older by {ageP1 - ageP2}")
elif ageP1 < ageP2:
    print(f"2nd person is older by {ageP2 - ageP1}")
else:
    print("The age is same")

### chetvertaya ###
num = int(input("Enter one number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Neutral")

### pyataya ###
if first > scnd:
    print(f"Sum: {first + scnd}")
elif first < scnd:
    print(f"Difference: {first - scnd}")
else:
    print("Numbers are equal")