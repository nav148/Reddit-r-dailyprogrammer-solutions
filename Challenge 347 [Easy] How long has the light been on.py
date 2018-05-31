#-------------------------------------------------------------------------------
# Name:        [2018-01-15] Challenge #347 [Easy] How long has the
#               light been on?
# Purpose:
#
# Author:      nav
# Link:        https://www.reddit.com/r/dailyprogrammer/comments/
#               7qn07r/20180115_challenge_347_easy_how_long_has_the/
# Created:     06/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##times = [(1,3),(2,3),(4,5)]
##times = [(2,4),(3,6),(1,3),(6,8)]
##times = [(6,8),(5,8),(8,9),(5,7),(4,7)]
##times = [(6,8),(5,8),(8,9),(5,7),(4,7)]
times = [(15,18),(13,16),(9,12),(3,4),(17,20),(9,11),(17,18),(4,5),(5,6),(4,5),(5,6),(13,16),(2,3),(15,17),(13,14)]
maximum = 0

for val in times:
    if val[1] > maximum:
        maximum = val[1]

timelist = [0]*(maximum + 1)

for val in times:
    for i in range(val[0]+1, val[1]+1):
        timelist[i] = 1
print(sum(timelist))

