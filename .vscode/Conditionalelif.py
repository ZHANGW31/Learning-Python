#Using conditional elif

#elif statement follows if, and means "else, if" another conditional exists do something else

#Examples

# WHAT TO WEAR
weather = input("Enter weather (sunny, rainy, snowy): ") 

if weather.lower() == "sunny":
    print("Wear a t-shirt")
elif weather.lower() == "rainy":
    print("Bring an umbrella and boots")
elif weather.lower() == "snowy":
    print("Wear a warm coat and hat")
else:
    print("Sorry, not sure what to suggest for", weather)

# SECRET NUMBER GUESS
secret_num = "2"

guess = input("Enter a guess for the secret number (1-3): ")

if guess.isdigit() == False:
    print("Invalid: guess should only use digits")
elif guess == "1":
    print("Guess is too low")
elif guess == secret_num:
    print("Guess is right")
elif guess == "3":
    print("Guess is too high")
else:
    print(guess, "is not a valid guess (1-3)")

shirt_size = input("What is your shirt size? Enter S for small, M for medium, and L for large: ")

if shirt_size == "S":
    print("Small shirts are $6")
elif shirt_size == "M":
    print("Medium shirts are $7")
elif shirt_size == "L":
    print("Large shirts are $8")