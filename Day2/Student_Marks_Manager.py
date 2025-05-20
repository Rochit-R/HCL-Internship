import numpy as np

student_scores = np.array([
    [85, 90, 88],
    [78, 80, 72],
    [92, 89, 95],
    [70, 75, 68]
])

second_student = student_scores[1, :]
print("Second student's scores:", second_student)

english_scores = student_scores[:, 2]
print("English scores:", english_scores)

total_marks = np.sum(student_scores, axis=1)
print("Total marks:", total_marks)

subject_avg = np.mean(student_scores, axis=0)
print("Average marks per subject:", subject_avg)
