#type() returns an object type
#type can be called with a float the return value can be stored in a variable

#Example

object_type = type(2.33)

#use the return keyword in a function to return a value after exitiing the functon

def msg_double(phrase):
    double = phrase + " " + phrase
    return double

#save the return value in a variable

msg_2x = msg_double("let's go")
print(msg_2x)