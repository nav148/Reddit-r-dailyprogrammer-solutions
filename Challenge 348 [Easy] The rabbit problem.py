#-------------------------------------------------------------------------------
# Name:        [2018-01-22] Challenge #348 [Easy] The rabbit problem
# Purpose:
#
# Author:      nav
# Link         https://www.reddit.com/r/dailyprogrammer/comments/
#              7s888w/20180122_challenge_348_easy_the_rabbit_problem/
# Created:     05/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def rabbit_pop(strng):
    strng_split = list(map(int,strng.split()))
    RABBIT_DEATH = 97   # Number of months till rabbits die

    male_pop  = [0]*RABBIT_DEATH
    fem_pop = [0]*RABBIT_DEATH
    male_pop[2] = strng_split[0]
    fem_pop[2] = strng_split[1]
    months_output = 0

    while sum(male_pop) + sum(fem_pop) < strng_split[2]:
        multi = sum(fem_pop[4:])
        fem_pop = [multi*9] + fem_pop[:-1]
        male_pop = [multi*5] + male_pop[:-1]
        months_output += 1
    print(months_output)

rabbit_pop('2 4 1000000000')
rabbit_pop('2 4 15000000000')
