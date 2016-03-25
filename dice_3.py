import random


class Dice(object):
    """ Creates a dice object with n-sides that we can roll
    and get dice values.
    """
    def __init__(self, sides):
        self.sides = 6
        self.min = 1

    def roll_dice(self):
        """Using the random module we call for a random integer
        representative of a dice roll by setting the min to 1
        and the max to the sided-ness of our dice
        """
        roll = random.randint(self.min, self.sides)
        print("\nYou rolled a %s\n" % roll)

    def side_change(self):
        """ To change the sided-ness of the dice we check to be
        sure the user has inputed an int value. If not they are
        asked to try again
        """
        while True:
            try:
                self.sides = int(input("How many sides on this dice?\n> "))
                break
            except ValueError:
                print("That was not a valid number. Try again.")


if __name__ == '__main__':
    my_dice = Dice(6)
    choice = ''

    # give the user the keyboard inputs available
    print("\n[r] Enter 'r' to roll a dice.")
    print("[c] Enter 'c' to change the number of sides.")
    print("[q] Enter 'q' to quit.")

    # run a loop to allow re-rolls, or changes in dice parameters
    while choice != 'q':
        choice = input("Enter your choice. (r, c, or q)> ")
        if choice == '':
            my_dice.roll_dice()
        elif choice.lower() == 'r':
            my_dice.roll_dice()
        elif choice.lower() == 'c':
            my_dice.side_change()
        elif choice.lower() == 'q':
            print("\n\nGood-bye\n")
        else:
            print("\n\nI did not understand that, try again.")
