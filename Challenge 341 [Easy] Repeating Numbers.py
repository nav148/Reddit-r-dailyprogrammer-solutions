#-------------------------------------------------------------------------------
# Name:        [2017-11-21] Challenge #341 [Easy] Repeating Numbers
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7eh6k8/20171121_challenge_341_easy_repeating_numbers/
# Created:     12/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def repeating_num(strng):
    comb_dict = {}
    repeat_exist = False
    for i in range(len(strng), 1, -1):
        for j in range(len(strng)+ 1 - i):
            comb_dict[strng[j:j+i]] = comb_dict.get(strng[j:j+i],0) + 1
    for (k,v) in comb_dict.items():
        if v >= 2:
            print("{0}:{1}".format(k, v))
            repeat_exist = True
    if repeat_exist == False:
        print("0")

#repeating_num('82156821568221')
#repeating_num('11111011110111011')
#repeating_num('98778912332145')
#repeating_num('124489903108444899')

