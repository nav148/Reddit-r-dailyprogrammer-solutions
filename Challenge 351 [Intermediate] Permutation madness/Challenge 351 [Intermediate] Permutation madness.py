#-------------------------------------------------------------------------------
# Name:        [2018-02-14] Challenge #351 [Intermediate] Permutation madness
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7xkhar/20180214_challenge_351_intermediate_permutation/
# Created:     19/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def Perm_Mad(strng):
    lines = strng.split()
    original = list(lines[0])
    moves = lines[1].split(",")

    output = original[:]
    for i in range(len(original)):
        output[i] = output[i] + str(i)

    for move in moves:
        if move[0] == 's':
            output = output[-int(move[1:]):] + output[:-int(move[1:])]
        else:
            indexes = list(map(int, move[1:].split("/")))
            if move[0] == 'x':
                output[indexes[0]], output[indexes[1]] = output[indexes[1]], output[indexes[0]]
            if move[0] == 'p':
                index_a = output.index(original[indexes[0]] + str(indexes[0]))
                index_b = output.index(original[indexes[1]] + str(indexes[1]))
                output[index_a], output[index_b] = output[index_b], output[index_a]
    for val in output:
        print(val[0], end="")
    print()

def Perm_Mad_file(text):
    t = open(text, "r")
    lines = t.readlines()
    original = list(lines[0][:-1])
    moves = lines[1].split(",")

    output = original[:]
    for i in range(len(original)):
        output[i] = output[i] + str(i)

    for move in moves:
        if move[0] == 's':
            output = output[-int(move[1:]):] + output[:-int(move[1:])]
        else:
            indexes = list(map(int, move[1:].split("/")))
            if move[0] == 'x':
                output[indexes[0]], output[indexes[1]] = output[indexes[1]], output[indexes[0]]
            if move[0] == 'p':
                index_a = output.index(original[indexes[0]] + str(indexes[0]))
                index_b = output.index(original[indexes[1]] + str(indexes[1]))
                output[index_a], output[index_b] = output[index_b], output[index_a]
    for val in output:
        print(val[0], end="")
    print()

Perm_Mad("""abcde
s1,x3/4,p4/1""")

Perm_Mad("""dbagcfe
s4,s5,x5/3,x5/6,s5,s3,x0/3,x3/6,x6/0,x2/3,x3/5,s5,s5,s5,s1,s5,s3,s3,x2/3,x1/0,s1,s1,s1,s4,x1/3,x4/2,x5/1,x6/0,s2,x2/1""")

Perm_Mad_file("challenge3.txt")
Perm_Mad_file("challenge4.txt")