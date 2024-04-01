student_heights = input("Input a list of student heights: ").split(" ")

sum = 0
for h in student_heights:
    sum += int(h)

print(f"average is: {round(sum/len(student_heights), 2)}cm")