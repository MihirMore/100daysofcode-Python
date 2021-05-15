# File Not Found Error

try:
    file = open("a_text.txt")
    # a_dictionary = {
    #     "key" : "value"
    # }
    # print(a_dictionary["aehdg"])
except FileNotFoundError:
    file = open("a_text.txt", "w")    
    file.write("Write Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")    
else:
    content = file.read()
    print(content)
# Your own custom exceptions    
finally:
    raise TypeError("This is an error I made up!")



