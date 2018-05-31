#-------------------------------------------------------------------------------
# Name:        [2018-01-08] Challenge #346 [Easy] Cryptarithmetic Solver
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7p5p2o/20180108_challenge_346_easy_cryptarithmetic_solver/
# Created:     06/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import itertools

def cryptarithm(strng_input):
    unique_letters = '' # String of all unique letters in the equation
    digit_list = list(range(10))
    strng_dict = {}

    equation = strng_input    # Input equation
    equation = equation.replace(" ", "")

    for val in equation:
        if val.isalpha() and unique_letters.find(val) == -1:
            unique_letters += val

    solution = equation.split('==')[1]  # Solution word
    add_list = (equation.split('==')[0]).split('+') # List of words to add


    combs = itertools.combinations(digit_list, len(unique_letters))
    for c in combs:
        perms = itertools.permutations(c)
        for p in perms:
            for (i, val) in enumerate(p):
                strng_dict[unique_letters[i]] = val

            total_add = 0   # Total integer value of the sum of all words in add_list
            for val in add_list:
                str_tmp = ''
                for letter in val:
                   str_tmp += str(strng_dict[letter])
                total_add += int(str_tmp)

            total_solution = 0 # Integer value of the solution word
            str_tmp = ''
            for letter in solution:
                str_tmp += str(strng_dict[letter])
            total_solution += int(str_tmp)

            if (total_add == total_solution):
                possible = True
                for word in add_list:
                    if strng_dict[word[0]] == 0:
                        possible = False
                if strng_dict[solution[0]] == 0:
                    possible = False
                if possible:
                    final = list(strng_dict.items())
                    final.sort()
                    print(final)


#cryptarithm("THIS + IS + HIS == CLAIM")
#cryptarithm("WHAT + WAS + THY == CAUSE")
#cryptarithm("HIS + HORSE + IS == SLAIN")
#cryptarithm("HERE + SHE == COMES")
#cryptarithm("FOR + LACK + OF == TREAD")
#cryptarithm("I + WILL + PAY + THE == THEFT")
