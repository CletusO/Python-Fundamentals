import random
rand_num = random.randint(1, 15)

try:
    guess_num = int(input("Can you guess the number between 1 - 15: "))
    while guess_num in range(1, 15):
        while rand_num != guess_num:
            print("You are wrong, you have 4 more tries.")
            tries = 4
            for i in range(4):
                guess_num = int(input("Can you guess the number between 1 - 15 again: "))
                if guess_num == rand_num:
                    print(guess_num, "!!", "Your guess is right.")
                    exit()
                else:
                    tries -= 1
                    print("Wrong,", tries, "more tries")
                    if tries == 0:
                        print("You have exhausted your tries.")
                        exit()
    else:
        print(guess_num, "is out of range")
except ValueError:
    print("This is not valid, you need to input a number")
