import os
from art import logo
# Calculator
# add
def add (n1, n2):
  return n1 + n2

# subtract 
def subtract (n1, n2):
  return n1 - n2

def multiply (n1 , n2):
  return n1 * n2

# divide
def divide (n1 , n2):
  return n1 / n2    

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}     
def calculator():
  print(logo)    
  num1 = float(input("What's the first number? "))

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:    
    operation_symbol = input("Please pick an operation: ")
    num2 = float(input("What's the second number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1 , num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if (input("Type 'y' to continue with {answer}: or type 'n' to start a new calculation: ") == 'y'):
      num1 = answer
    else:
      should_continue = False  
      _ = os.system('cls')
      calculator()

calculator()      