#Defining functions in Python

#In order to define a function in Python, you must use the def keyword, followed by the function name ex: func_name() and finally with a colon :

#Once you define the function, in the next line, it must be indented (4 spaces length)



def say_hello():
    print("Hello World!")
    print("and goodbye!")
#End of indentation means the end of the function


#Another example

def one_two():
    print(12)

#Calling functions via their name and parenthesis
one_two()
say_hello()

#Defining a function that prints the phrase with ! concatenated to the end

#Defined a variable called phrase for a short string
phrase = "What a great day it is to learn Python"


def yell_it():    
    print(phrase.upper(),"!") #utilizing the .upper method the string characters are all converted to uppercase, and concatenated with !

#Calling the function
yell_it()

#Defining Function Parameters

#Parameters are defined inside the parenthesis as part of a function def statement.

#Here the parameter of sentence is defined.
sentence = "The cake is a lie"
def say_this(sentence):
    print(sentence)

#Functions may also have default arguments, which is used when no argument is supplied

def say_that(phrase = "Hello from the other side"):
    print(phrase)

#In this case, if no argument was defined with the function when calling the function, it will have a default argument

#This method call returns the default argument of: Hello from the other side
say_that()
#This method call returns utlizes the "Goodbye" as an argument.
say_that("Goodbye")