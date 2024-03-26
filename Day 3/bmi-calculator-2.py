height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2

if bmi <= 18.5:
    print(f"Your bmi is {round(bmi,2)}, You are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your bmi is {round(bmi,2)}, You are normal weight.")
elif bmi > 25 and bmi <= 30:
    print(f"Your bmi is {round(bmi,2)}, You are overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your bmi is {round(bmi,2)}, You are obese.")
else:
    print(f"Your bmi is {round(bmi,2)}, You are clinically obese.")