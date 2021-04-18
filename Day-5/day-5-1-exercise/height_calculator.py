# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height = 0
for students in student_heights:
  height += students

length = 0

for student_num in student_heights:
  length += 1

average_height = round((height/length))
print(average_height)