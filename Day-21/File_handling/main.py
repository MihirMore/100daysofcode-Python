# with open("my_file.txt") as fhand:

#     contents = fhand.read()
#     print(contents)


with open("my_file.txt", mode = "a") as fhand:
    fhand.write("Hello! I'm appending")