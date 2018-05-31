#-------------------------------------------------------------------------------
# Name:        [2017-11-29] Challenge #342 [Intermediate] ASCII85 Encoding and Decoding
# Purpose:
#
# Author:      navin
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7gdsy4/20171129_challenge_342_intermediate_ascii85/
# Created:     08/03/2018
# Copyright:   (c) navin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def four_byte_encode(strng):
    str_list = list(strng) #split strng into list of characters
    for (i, val) in enumerate(str_list): #convert each character to ascii in binary form
        temp = ord(val)
        str_list[i] = bin(temp)[2:].zfill(8)

    concatenate = ''.join(str_list).ljust(32,'0')

    int_concatenate = int(concatenate,2)

    output = []
    for i in range(4,-1,-1):
        temp = int((int_concatenate/pow(85,i)) % 85) + 33
        output.append(chr(temp))

    if len(strng)==4:
        return(''.join(output))
    else:
        return(''.join(output)[:-len(strng)])

def four_byte_decode(strng):
    str_list = list(strng) #split strng into list of characters

    for(i, val) in enumerate(str_list):
        temp = ord(val)
        str_list[i] = temp-33

    if len(str_list) != 5:
        for i in range(5-len(strng)):
            str_list.append(84)

    int_concatenate = 0
    for (i, val) in enumerate(str_list):
        int_concatenate += str_list[i]*(pow(85, 4-i))
    bin_concatenate = bin(int_concatenate)[2:].zfill(32)

    output = [bin_concatenate[i:i+8] for i in range(0, len(bin_concatenate), 8)]

    for(i, val) in enumerate(output):
        output[i] = chr(int(val,2))

    if len(strng) == 5:
        return(''.join(output))
    else:
        return(''.join(output)[:-(5 - len(strng))])

def ascii85_encoder(strng):
    split = [strng[i:i+4] for i in range(0, len(strng), 4)]

    for (i,val) in enumerate(split):
        split[i] = four_byte_encode(val)
    print(''.join(split))

def ascii85_decoder(strng):
    split = [strng[i:i+5] for i in range(0, len(strng), 5)]

    for (i,val) in enumerate(split):
        split[i] = four_byte_decode(val)
    print(''.join(split))

def ascii85(strng):
    split = strng.split(" ", 1)

    if split[0] == 'e':
        ascii85_encoder(split[1])
    elif split[0] == 'd':
        ascii85_decoder(split[1])

ascii85("""e Attack at dawn""")
ascii85("""d 87cURD_*#TDfTZ)+T""")
ascii85("""d 06/^V@;0P'E,ol0Ea`g%AT@""")
ascii85("""d 7W3Ei+EM%2Eb-A%DIal2AThX&+F.O,EcW@3B5\\nF/hR""")
ascii85("""e Mom, send dollars!""")
ascii85("""d 6#:?H$@-Q4EX`@b@<5ud@V'@oDJ'8tD[CQ-+T""")



