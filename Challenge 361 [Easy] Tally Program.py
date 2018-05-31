#-------------------------------------------------------------------------------
# Name:        [2018-05-14] Challenge #361 [Easy] Tally Program
# Purpose:
#
# Author:      navin
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/8jcffg
#               /20180514_challenge_361_easy_tally_program/
# Created:     27/04/2018
# Copyright:   (c) navin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import operator

def main(strng):
    scores = {}
    inputlist = list(strng)

    for val in inputlist:
        if val.isupper():
            increment = -1
        else:
            increment = 1
        scores[val.lower()] = scores.get(val.lower(), 0) + increment

    sorted_scores = (sorted(scores.items(), key=operator.itemgetter(1), reverse = True))
    print(sorted_scores)

main("abcde")
main("dbbaCEDbdAacCEAadcB")
main("EbAAdbBEaBaaBBdAccbeebaec")