#.isalpha()
#isalpha returns True if all characters in the string are alphabetical, otherwise returns false.

txt = "abc" 

x = txt.isalpha()

print(x)

#This prints out true.

#.isalnum()
#isalnum return True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
#example of characters that are not alphanumeric: (space)!#%&?

newTxt = "One23"

y = newTxt.isalnum()

print(y)

#This prints out true

newTxtX = "  !@#"

z = newTxtX.isalnum()

print(z)

#This prints out false


#.istitle()
#.isdigit()
#.islower()
#.isupper()
#.startswith()