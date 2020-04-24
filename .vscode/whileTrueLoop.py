#Using the while True: statement results in a loop that continues to run forever or , until the loop is interrupted , such as with a break statement.

# this example never loops because the break has no conditions
while True:
    print('write forever, unless there is a "break"')
    break

number_guess = "0"
secret_number = "5"

#this while loop executes until the number is guessed correctly
while True:
    number_guess = input("guess the number 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess,"is correct!\n")
        break
    else:
        print(number_guess,"is incorrect\n")

