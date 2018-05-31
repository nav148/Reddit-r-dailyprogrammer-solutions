#-------------------------------------------------------------------------------
# Name:        [2018-03-07] Challenge #353 [Intermediate] Pancake Sorting Problem
# Purpose:
#
# Author:      navin
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               82pt3h/20180307_challenge_353_intermediate/
# Created:     15/03/2018
# Copyright:   (c) navin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def PSP (strng):
    lines = strng.split('\n')
    stack = list(map(int, lines[1].split()))

    for i in range(len(stack)):
        largest = 0
        for j in range(len(stack) - i):
            if stack[j] > largest:
                largest_index = j
        stack = largest_to_back(stack, i, largest_index)
    print(stack)

def largest_to_back(stack, i, j):
    """ Returns the new stack after sending the pancake at index j to the bottom
        of the stack
    """
    temp_stack = stack[:]
    temp_stack[:j+1] = temp_stack[:j+1][::-1]
    temp_stack[:len(stack)-i] = temp_stack[:len(stack)-i][::-1]
    return temp_stack


PSP("""3
1 3 2""")

PSP("""8
7 6 4 2 6 7 8 7""")

PSP("""8
11 5 12 3 10 3 2 5""")

PSP("""10
3 12 8 12 4 7 10 3 8 10""")