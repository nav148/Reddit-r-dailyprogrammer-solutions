#-------------------------------------------------------------------------------
# Name:        [2018-01-10] Challenge #346 [Intermediate] Fermat's little theorem
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7pmt9c/20180110_challenge_346_intermediate_fermats/
# Created:     16/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def Fermat(strng):
    lines = strng.split()
    num = int(lines[0])
    certainty = float(lines[1])
    rng = random.Random()
    isprime = True
    count = 0
    rand_list = []

    while 1-pow(0.5,count) < certainty:
        a = rng.randint(2,num)
        if a in rand_list:
            a = rng.randint(2,num)
        rand_list.append(a)
        if pow(a, num, num) != a:
            isprime = False
        count += 1
    print(isprime)
    return isprime

def Miller_Rabin(strng):
    lines = strng.split()
    num = int(lines[0])
    certainty = float(lines[1])
    a = 2
    s = 2
    d = (num-1)//pow(2,s)

    count = 0
    while 1-pow(3/4,count+1) < certainty:
        soln = pow(a,pow(2,count)*d,num)
        if soln == 1:
            print("False")
            return
        elif soln == num-1:
            print("True")
            return
        count += 1
    print("True")
    return


Fermat("29497513910652490397 0.9")
Fermat("29497513910652490399 0.9")
Fermat("95647806479275528135733781266203904794419584591201 0.99")
Fermat("95647806479275528135733781266203904794419563064407 0.99")
Fermat("2367495770217142995264827948666809233066409497699870112003149352380375124855230064891220101264893169 0.999")
Fermat("2367495770217142995264827948666809233066409497699870112003149352380375124855230068487109373226251983 0.999")

Miller_Rabin("2887 0.9")
Miller_Rabin("2821 0.9")