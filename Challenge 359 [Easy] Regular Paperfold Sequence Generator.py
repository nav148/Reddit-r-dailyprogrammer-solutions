#-------------------------------------------------------------------------------
# Name:        [2018-04-30] Challenge #359 [Easy] Regular Paperfold Sequence Generator
# Purpose:
#
# Author:      navin
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               8g0iil/20180430_challenge_359_easy_regular_paperfold/
# Created:     31/05/2018
# Copyright:   (c) navin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------



def updatesequence(lst):
    """
       Returns the next sequence given an input sequence
    """
    temp = []
    insert = "1"
    for val in lst:
        temp.append(insert)
        temp.append(val)
        if insert == "1":
            insert = "0"
        else:
            insert = "1"
    temp.append("0")
    return temp

def main(n):
    """
        Prints the nth cycle of the regular paper folding sequence
    """
    sequence = ["1"]
    for i in range(n):
       sequence = updatesequence(sequence)
    print(''.join(sequence))

main(2)

