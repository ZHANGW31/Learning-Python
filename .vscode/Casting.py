#Casting is the conversion form one data type to another Such as converting from str to int

#the int() function can convert strings that represent whole counting numbers into integers and strip decimals to convert float numbers to integers

#int("1") = 1 the string representing the integer character "1", cast to a number

#int(5.1) = 5 the decimal (float), 5.1, truncated into a non-decimal (integer)

#int("5.1") = ValueError "5.1" isn't a string representation of integer, int() can cast only strings representing integer values

weight1 = '60' # a string
weight2 = 170 # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)

#casting with int() & str()

str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result

totals = int(str_num_1) + int(str_num_2) + int_num_3
print(totals)