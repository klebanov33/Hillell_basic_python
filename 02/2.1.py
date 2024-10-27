User_number = int(input("Enter 4-digit number: "))

first_number = User_number // 1000
number_3_digit = User_number % 1000
second_number = number_3_digit // 100
number_2_digit = number_3_digit % 100
third_number = number_2_digit // 10
forth_number = number_2_digit % 10

print(first_number)
print(second_number)
print(third_number)
print(forth_number)