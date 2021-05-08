numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# List Comprehension

new_list2 = [n+1 for n in numbers]
print(new_list2)

name = "Mihir"
new_list1 = [letter for letter in name]
print(new_list1)

new_range = [num*2 for num in range(1, 5)]
print(new_range)

name_list = ["Alex", "Caroline", "Eleanor", "Max", "Beth"]
new_name_list = [name for name in name_list if len(name)<5]
print(new_name_list)