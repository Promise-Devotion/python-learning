# Python has to guess what datatype a variable should be

# since the input function returns a string, the variables it populates
# will hold string values
first_num = input('Enter first number ')
second_num = input('Enter second number ')

# Because first_num and second_num are string variables the + operator
# concatenates them just like concatenating first_name and last_name
print(first_num + second_num)

# Calculate the total of the two numbers added together
# their are three methods, iny, long, float
answer = float(first_num) + float(second_num) # float
# int
# answer = int(first_num) + int(second_num)

# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
print(first_num + ' + ' + second_num + ' = ' + str(answer))

# If you do not want the decimal places you could round the answer
print(first_num + ' + ' + second_num + ' = ' + str(round(answer)))