student_scores = input("Input a list of student scores: ").split(" ")

max_score = int(student_scores[0])
for score in student_scores:
    score = int(score)
    if max_score < score:
        max_score = score
    
print(f"highest score is: {max_score}")