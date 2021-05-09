# Example of dictionary comprehension
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {name:random.randint(45, 100) for name in names}
# print(student_scores)

passed_scores = {student:score for student, score in student_scores.items() if score >= 50}
print(passed_scores)

