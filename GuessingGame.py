import random

while True:
    flag = True
    while flag:
        num = input("Enter An Upper Bound:")
        if num.isdigit():
            print("Lets Play!..")
            num = int(num)
            flag = False
        else:
            print("Invalid Input Try Again!..")
    secret = random.randint(1, num)
    guess = 0
    count = 1
    while guess != secret:
        guess = input("Enter The Number Between 1 And " + str(num) + " :")
        if guess.isdigit():
            guess = int(guess)
        if secret == guess:
            print("You Got It!..")
        else:
            print("Try Again!..")
            count += 1
    print("You Taken " + str(count) + " Guesses!..")
