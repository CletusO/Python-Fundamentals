# printing a Christmas tree.


# create a function


def christmas_tree():  # base is the base of the tree
    # get user to input how large they want the Christmas tree by giving the value of the base
    base = int(input("Please give me the number of leaves to be in your base: "))
    leaves = 0  # this is default number of leaves on the tree
    while leaves <= base:
        a = "*" * leaves  # number of leaves to be printed in each line
        print(a.center(70))
        leaves += 2  # increment by 2 to give the triangular shape of a tree
    else:
        # base of the tree
        print("|  |".center(70))
        print("|  |".center(70))


christmas_tree()

