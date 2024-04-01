n = int(input("Enter the n to calculate series: "))

sum = 0
for i in range(0, n+1, 2):
    sum += i

print(f"Result is: {sum}")