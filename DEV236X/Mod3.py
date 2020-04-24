#set values for maximum and minimum order variables
#set value for price variable
#get order_amount input and cast to a number
#check order_amount and give message checking against
#over maximum
#under minimum
#else within maximum and minimum give message with calculated price

minimum_order = 1
maximum_order = 100
price = 7.99

order_amount = int(input("please enter the order amount: "))

if order_amount > 100:
    print(order_amount,"is more than currently in stock")
elif order_amount < 1:
    print(order_amount,"is below the minimum amount")
else:
    print(order_amount, "cost", "$",order_amount * price)



