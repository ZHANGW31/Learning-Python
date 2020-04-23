#Comparison operators evaluate to Boolean True and False to direct the flow of if conditionals

x = 21
# > here is used to evaluate whether or not x is larger than 25.
if x > 25:
    print("x is already bigger than 25")
else:
    print("x was", x)
    x = 25
    print("now x is", x)

x = 18
test_value = 18
# the != evaluates to is not
if x != test_value:
    print('x is not', test_value)
else:
    print('x is', test_value)