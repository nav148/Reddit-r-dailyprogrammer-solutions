#-------------------------------------------------------------------------------
# Name:        [2018-02-06] Challenge #350 [Easy] Bookshelf problem
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7vm223/20180206_challenge_350_easy_bookshelf_problem/
# Created:     07/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import itertools

def shelves(strng_input):

    books_dict = {}     # Dictionary of all books
    solution = {}       # Dictionary of the solution

    lines = strng_input.split('\n')

    shelves = list(map(int, lines[0].split()))  # List of all available shelves
    shelves.sort(reverse = True)

    books = lines[1:]   # List of all books with lengths
    for val in books:
        temp = val.split(' ', 1)
        books_dict[temp[1]] = int(temp[0])
    book_lens = list(books_dict.values()) # List of all book lengths
    book_lens.sort(reverse = True)

    shelf_index = 0
    while len(book_lens) > 0 and shelf_index < len(shelves) - 1:
        filled_shelf = shelf_calc(book_lens, shelves[shelf_index])
        if filled_shelf == False:
            break
        solution[shelves[shelf_index]] = filled_shelf
        for val in filled_shelf:
            book_lens.remove(val)
        shelf_index += 1

    if len(book_lens) == 0:
        print(len(list(solution.items())))
        print(list(solution.keys()))
    else:
        print("impossible")

def shelf_calc(book_lengths, shelf):
    """ Returns the largest book number combination with the greatest sum
        from 'book_lengths' to fit a shelf of size 'shelf'
    """
    for i in range(len(book_lengths), 0, -1):
        combs = list(itertools.combinations(book_lengths, i))
        temp_combs = combs[:]
        for (j, val) in enumerate(temp_combs):
            if sum(val) > shelf:
                combs.remove(val)
        if len(combs) > 0:
            return combs[0]
    return False



shelves("""150 150 300 150 150
70 A Game of Thrones
76 A Clash of Kings
99 A Storm of Swords
75 A Feasts for Crows
105 A Dance With Dragons""")

shelves("""500 500 500
1309 Artamene
303 A la recherche du temps perdu
399 Mission Earth""")

shelves("""30
30 Artamene
20 A la recherche du temps perdu""")

shelves("""40 20 40 180 90
40 book1
50 book2
40 book3
50 book4
40 book5
50 book6""")

##shelves("""270 142 501 865 384 957 947 603 987 428 907 10 691 707 397 917 492 750 935 672 935 712 234 683 702 508 822 379 36 59 382 280 867 155 829 756 360 995 526 52 559 250 450 843 523 446 972 555 55 985 81 831 43 802 473 379 461 639 910 529 128 878 914 426 569 59 139 913 69 649 501 889 470 112 92 6 80 571 220 22 676 91 889 799 115 194 555 477 277 718 378 838 822 358 178 562 674
##96 b400786
##69 b390773
##174 b410413
##189 b337528
##80 b308576
##194 b151872
##190 b174310
##157 b272731
##45 b326576
##112 b379689
##177 b18459
##122 b915759
##138 b967342
##96 b786519
##184 b718074
##75 b696975
##192 b46366
##168 b533904
##45 b885475
##186 b872991
##63 b231207
##162 b912709
##123 b786720
##7 b743805
##120 b862301
##54 b929784
##89 b61876
##168 b775890
##87 b850242
##60 b695331
##0 b56157
##139 b875241
##78 b281324
##122 b236962
##1 b79403
##68 b213353
##103 b650997
##97 b955752
##177 b815100
##139 b958679
##43 b829736
##163 b445471
##94 b472821
##167 b5429
##57 b946679
##13 b748794
##146 b920913
##17 b547056
##33 b437091
##12 b247401
##120 b228908
##178 b509018
##98 b482352
##152 b915322
##14 b874214
##71 b164605
##11 b457140
##35 b502201
##5 b15232
##49 b641136
##166 b385360
##183 b78285
##199 b274935
##195 b424221
##79 b422570
##150 b502699
##41 b662132
##63 b430898
##111 b813368
##100 b700970
##157 b803925
##140 b611243
##25 b877197
##136 b577201
##94 b50211
##56 b762270
##120 b578094
##21 b672002
##9 b107630
##156 b547721
##186 b911854
##71 b594375
##32 b330202
##3 b464002
##36 b718293
##44 b282975
##130 b826246
##77 b529800
##117 b66381
##89 b949447
##133 b348326
##178 b517646
##184 b809038
##105 b70260
##182 b894577
##123 b203409
##79 b174217
##159 b552286
##40 b854638
##78 b159990
##139 b743008
##1 b714402
##153 b923819
##107 b201001
##48 b567066
##138 b570537
##100 b64396
##139 b412215
##132 b805036
##121 b772401
##120 b370907
##51 b388905
##77 b442295
##152 b195720
##46 b453542""")