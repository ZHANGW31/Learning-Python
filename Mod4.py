#check if string is digits

#if digits: convert to int and check if greater than 99

#if greater than 99 print a message about a big number

#if not greater than 99 print message about small number

# check if string isalpha then 

#if isalpha print message about being all alpha

#if not is alpha print a message about being neither all alpha nor all digit

#call the function with a string from user input


#Defining the function that takes one arguement
def str_analysis(user_input):
    #checks if the user input is empty
    while user_input != "":
        #checks if user input contains is all digits, if true continue 
        if user_input.isdigit() == True:
            user_num = int(user_input)
            if user_num > 99:
                print("The number entered:",user_num,"is a big number")
            elif user_num < 99:
                print("The number entered:",user_num,"is a small number")
        #checks if user input is all alphabetic
        elif user_input.isalpha() == True:
            print("The input is all alphabetic")
        #If the user input is neither all alphabetic, not empty, or all digits, then return it has multiple character types.
        elif user_input.isalpha() == False:
            print("The input is neither all alpha nor all digits, it has multiple character types")

user_input = input("Please enter a string for analysis: ")

str_analysis(user_input)
