import random

names = input("Give me everybody's names, seperated by a comma.").split(",")

rand_number = random.randint(0, len(names) - 1)

print(f"{names[rand_number]} is going to buy the meal today!")