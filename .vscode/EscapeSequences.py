#Formatting strings using escape sequences
#Escape Sequences
#escape sequences all start with a backslash (\)

#escape sequences can be used to display characters in python reserved for formatting

#\\   Backslash (\)
#\'   Single quote (')
#\"   Double quote (")
#escape sequences are part of special formatting characters

#\t   Tab
#\n   return or newline
#We use escape sequences in strings - usually with print() statements

#\n is equal to a newline
print('Hello World!\nI am formatting print ')

#\t creates tabs
student_age = 17
student_name = "Hiroto Yamaguchi"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t' + str(student_age))

# using \" and \' (escaped quotes)
print("\"quotes in quotes\"")
print("I\'ve said \"save your notebook,\" so let\'s do it!")

# using  \\ (escaped backslash)
print("for a newline use \\n")