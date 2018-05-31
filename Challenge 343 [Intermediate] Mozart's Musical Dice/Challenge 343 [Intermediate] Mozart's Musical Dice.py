#-------------------------------------------------------------------------------
# Name:        [2017-12-06] Challenge #343 [Intermediate] Mozart's Musical Dice
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7i1ib1/20171206_challenge_343_intermediate_mozarts/
# Created:     21/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def Mozart_mus_dice():
    start_comp_list = [0]
    start_txt = open("mozart-dice-starting.txt", "r")
    line = start_txt.readline()
    line = line.split()
    start_comp_list.append([line])
    for i in range(1,177):
        while True:
            line = start_txt.readline()
            if len(line) == 0:
                break
            line = line.split()
            if float(line[1]) < i*3:
                start_comp_list[i].append(line)
            else:
                start_comp_list.append([line])
                break

    rdm_gen = dice_gen()

    output = open("output.txt", "w")
    for (measure, val) in enumerate(rdm_gen):
        for note in start_comp_list[val]:
            output.write(note[0]+" ")
            output.write(str(float(note[1])-val*3+(measure+1)*3)+" ")
            output.write(note[2]+"\n")

    output.close()
    start_txt.close()

def dice_gen():
    """ Returns measure selection from table
    """
    import random

    rdm = random.Random()
    rdm_gen = []

    table_txt = open("dice-table.txt", "r")
    while True:
        line = table_txt.readline()
        if len(line) == 0:
            break
        line = list(map(int, line.split()))
        rdm_gen.append(line[rdm.randint(0,10)])

    table_txt.close()
    return(rdm_gen)


Mozart_mus_dice()