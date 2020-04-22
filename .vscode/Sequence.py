#Sequence refers to the order that code is processed. Objects in Python, such as variables and functions , are not available until they have been processed.

#Example

#in this case hat_color cannot be accessed since it is initialized after it is called at the bottom of the code.
have_hat = hat_available('green')

print('hat available is', have_hat)

def hat_avsailable(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)