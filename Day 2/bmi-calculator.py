height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2

print(f"Your bmi is: {round(bmi, 2)}")