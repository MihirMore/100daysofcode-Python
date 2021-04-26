# Before:
'''
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
'''

# Debugged Code

for number in range(1, 101):
  if number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")  
  else:
    print(number)