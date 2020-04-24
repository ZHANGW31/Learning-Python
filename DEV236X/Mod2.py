#This program requires a function be defined , created , and called. The call will send values based on user input. The function call must capture a return value that is used
#in the print output. The function will have parameters and return a string and should otherwise use code syntax covered in module 2.

# This is the end of module coding assignment.

#Program fishstore()

#Create and test fishstore()
#gather input for fish_entry and price_entry to use in calling fishstore()
fish_entry = input("Please enter the type or name of the fish: ")
price_entry = input("Please enter the price of the fish: ")


#fishstore() takes 2 string arguments: fish and price
def fishstore(fish, price):

    #fishtore returns a string in sentence form
    output = "Fish Type: "+ fish + " costs " + price 
    return output

#print the return value of fishstore()

print(fishstore(fish_entry, price_entry))
