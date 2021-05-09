with open("file1.txt") as first_input:
    file1_data = first_input.readlines()
    file1_new_data = [num.strip() for num in file1_data]
    print(file1_new_data)

with open("file2.txt") as second_input:
    file2_data = second_input.readlines()
    file2_new_data = [num.strip() for num in file2_data]
    print(file2_new_data)

result = [int(num) for num in file1_data if num in file2_data]
print(result)
