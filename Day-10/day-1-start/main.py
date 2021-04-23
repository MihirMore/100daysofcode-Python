def format_name(first_name, last_name):
  if first_name == '' or last_name == '':
    return "Please enter first name or last name."
  return f"{first_name} {last_name}".title()

print(format_name(input("What's your first name? "), input("What's your last name?")))