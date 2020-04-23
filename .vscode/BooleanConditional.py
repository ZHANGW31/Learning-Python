#In Python, Conditionals use True or False

#if , else, pass

#Examples

if True:
    print("True means do something")
else:
    print("Not True means do something else")

hot_tea = True

if hot_tea:
    print("enjoy some hot tea!")
else:
    print("enjoy some tea, and perhaps try hot tea next time.")

someone_i_know = False
if someone_i_know:
    print("how have you been?")
else:
    # use pass if there is no need to execute code 
    pass

# changed the value of someone_i_know
someone_i_know = True
if someone_i_know:
    print("how have you been?")
else:
    pass



sunny_today = True

if sunny_today:
    print("It is sunny today")
else:
    print("It is not sunny today")
