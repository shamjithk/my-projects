import random
lst = []
def luhn_algorithm():
    card_number = "400000" + str(random.randint(100000000, 999999999))
    card = []
    sum = 0
    temp = 0
    for i in card_number:
        card.append(int(i))
    for i in card[0::2]:
        card.remove(i)
        card.append(i * 2)
    for i in card:
        if i > 9:
            card.remove(i)
            card.append(i - 9)
    for i in card:
        if i > 9:
            card.remove(i)
            card.append(i - 9)
    for i in card:
        sum += i
        if sum % 10 != 0:
            temp = 10 - (sum % 10)
        else:
            temp = 0
    card_number += str(temp)
    return card_number
def create_account():
    card_number = luhn_algorithm()
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    card_pin = str(random.randint(1000, 9999))
    print(card_pin)
    lst.append(card_number)
    lst.append(card_pin)
    return lst

def log_in():
    user_input1 = input("Enter your card number:")
    user_input2 = input("Enter your PIN:")
    if user_input1 in lst:
        if user_input2 in lst:
            print("You have successfully logged in!")
            while True:
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                user_input3 = input()
                if user_input3 == "1":
                    print("Balance: 0")
                elif user_input3 == "2":
                    print("You have successfully logged out!")
                    break
                else:
                    print("Bye!")
                    exit()
        else:
            print("Wrong card number or PIN!")
    else:
        print("Wrong card number or PIN!")
while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    user_input = input()
    if user_input == "1":
        create_account()
    elif user_input == "2":
        log_in()
    else:
        print("Bye!")
        exit()
