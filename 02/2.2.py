User_number = int(input("Enter 5-digit number: "))

first_number = User_number // 10000
number_4_digit = User_number % 10000
second_number = number_4_digit // 1000
number_3_digit = number_4_digit % 1000
third_number = number_3_digit // 100
number_2_digit = number_3_digit % 100
forth_number = number_2_digit // 10
fifth_number = number_2_digit % 10

print(fifth_number * 10000 + forth_number * 1000 + third_number * 100 + second_number * 10 + first_number)
