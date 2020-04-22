#get input for input_test variable

input_test = input("enter somethings eaten in last 24 hrs: ")

inputToLower = input_test.lower()

contains = False

#print "True" message if "dairy" is in the input or False message if not
if "dairy" in inputToLower:
    contains = True
    print("It is", contains, "that" , input_test ,"contains dairy")
elif contains == False:
    print("It is", contains, "that" , input_test, "contains dairy")
if "nuts" in inputToLower:
    contains = True
    print("It is", contains, "that" , input_test ,"contains nuts")
elif contains == False:
    print("It is", contains, "that" , input_test, "contains nuts")
if "seafood" in inputToLower:
    contains = True
    print("It is", contains, "that" , input_test ,"contains seafood")
elif contains == False:
    print("It is", contains, "that" , input_test, "contains seafood")
if "chocolate" in inputToLower:
    contains = True
    print("It is", contains, "that" , input_test ,"contains chocolate")
elif contains == False:
    print("It is", contains, "that" , input_test, "contains chocolate")