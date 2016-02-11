#! usr/bin/python3

# Tim's dice rolling simulator
import random


def dice_roll():
    dice_min = 1
    dice_max = 6
    print("Want to roll a {}-sided dice?".format(dice_max))
    answer = input("(y)es, (n)o, (c)hange, (s)ettings \n> ")
    while answer != "n":
        if answer == "y":
            print('\n', "-"*16, '\n')
            print(' Rolled a ', random.randint(dice_min, dice_max))
            print('\n', "-"*16, '\n')
            print("Want to roll a {}-sided dice?".format(dice_max))
            answer = input("(y)es, (n)o, (c)hange, (s)ettings \n> ")
        elif answer == "c":
            print("How many sides should this dice have?")
            dice_max = int(input('>'))
            print("Want to roll a {}-sided dice?".format(dice_max))
            answer = input("(y)es, (n)o, (c)hange, (s)ettings \n> ")
        elif answer == "s":
            print("====SETTINGS====")
            print("dice_min =", dice_min)
            print("dice_max =", dice_max)
            print("="*16, "\n")
            print("Want to roll a {}-sided dice?".format(dice_max))
            answer = input("(y)es, (n)o, (c)hange, (s)ettings \n> ")
        else:
            answer = input("Please use the 'y', 'n', or 'c' keys\n>")

dice_roll()
