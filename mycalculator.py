
def add_num(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def div_num(*numbers):
    try:
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
    except ZeroDivisionError:
        exit()
    return result


def mul_num(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def sub_num(*numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result


print("""A for addition,
B for subtraction
C for division
D for Multiplication
""")

alpha_cal = str(input("What kind of calculation do you want?> "))


def user_choice(a):
    if alpha_cal.lower() == 'a': print("\nYou want addition of numbers")
    if alpha_cal.lower() == 'b': print("\nYou want subtraction of numbers")
    if alpha_cal.lower() == 'c': print("\nYou want division of numbers")
    if alpha_cal.lower() == 'd': print("\nYou want multiplication of numbers")
    return


user_choice(alpha_cal)

print()

num = [int(x) for x in (input("Give numbers for calculation separated by spaces > ").split())]


calc: dict = {'a': add_num(*num),
              'b': sub_num(*num),
              'c': div_num(*num),
              'd': mul_num(*num)
              }

print(calc.get(alpha_cal, "You have valid operation"))


