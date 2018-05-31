#-------------------------------------------------------------------------------
# Name:        [2018-01-29] Challenge #349 [Easy] Change Calculator
# Purpose:
#
# Author:      nav
# Link:        https://www.reddit.com/r/dailyprogrammer/
#              comments/7ttiq5/20180129_challenge_349_easy_change_calculator/
# Created:     02/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def change_coins(ininvent):
    """ Returns the coins to give back to yield the correct change
    """
    import itertools
    ininvent_split = list(map(int, ininvent.split()))
    change_total = ininvent_split[0]    # Change required
    inventory = ininvent_split[1:]      # Coin inventory
    for i in range(1, len(inventory) + 1):
        combination = list(itertools.combinations(inventory, i))
        for val in combination:
            if sum(val) == change_total:
                return val
    return False

def change(ininvent):
    """ Print's the output
    """
    coins = change_coins(ininvent)
    if coins == False:
        print("Coins not available to supply correct change")
    else:
        print(*coins)

change('150 100 50 50 50 50')
change('130 100 20 18 12 5 5')
change('200 50 50 20 20 10')
change('150 100 50 50 50 50')
change('130 100 20 18 12 5 5')
