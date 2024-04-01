import random

print("Welcome to the PyPassword Generaotr!")
letters = int(input("How mant letters would you like in your password? ")) # ascii 65 - 122
symbols = int(input("Hom many symbols would you like? ")) # ascii 33 - 47
numbers = int(input("How many numbers would you like? "))

password = ""
for i in range(0, letters+1):
    pointer = random.randint(0, 2)
    if pointer == 0 and letters != 0:
        password += chr(random.randint(65, 122))
        letters -= 1
    elif pointer == 1 and symbols != 0:
        password += chr(random.randint(33, 47))
        symbols -= 1
    else:
        password += str(random.randint(0, 9))

print(f"Here is your password: {password}")
