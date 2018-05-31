#-------------------------------------------------------------------------------
# Name:        [2018-02-07] Challenge #350 [Intermediate] Balancing My Spending
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7vx85p/20180207_challenge_350_intermediate_balancing_my/
# Created:     09/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
def balancing(strng):
    lines = strng.split('\n')
    transactions = list(map(int, lines[1].split()))
    solution = []
    for i in range(len(transactions)):
        left = 0
        right = 0
        if(i == 0):
            right = sum(transactions[1:])
        elif(i == len(transactions)-1):
            left = sum(transactions[:len(transactions)-1])
        else:
            left = sum(transactions[:i])
            right = sum(transactions[i+1:])
        if left == right:
            solution.append(i)
    return(solution)

def balance_ex(strng):
    lines = strng.split('\n')
    nums = list(map(int, lines[1].split()))
    left = 0
    right = sum(nums)
    b = []
    for i, n in enumerate(nums):
        right -= n
        if left == right:
            b.append(i)
        left += n
    return b

t0 = time.clock()
print(balancing("""8
0 -3 5 -4 -2 3 1 0"""))
print(balancing("""11
3 -2 2 0 3 4 -6 3 5 -4 8"""))
print(balancing("""11
9 0 -5 -4 1 4 -4 -9 0 -7 -1"""))
print(balancing("""11
9 -7 6 -8 3 -9 -5 3 -6 -8 5"""))
t1 = time.clock()
print("time taken = {0:.4f} seconds".format(t1-t0))

t0 = time.clock()
print(balance_ex("""8
0 -3 5 -4 -2 3 1 0"""))
print(balance_ex("""11
3 -2 2 0 3 4 -6 3 5 -4 8"""))
print(balance_ex("""11
9 0 -5 -4 1 4 -4 -9 0 -7 -1"""))
print(balance_ex("""11
9 -7 6 -8 3 -9 -5 3 -6 -8 5"""))
t1 = time.clock()
print("time taken = {0:.4f} seconds".format(t1-t0))