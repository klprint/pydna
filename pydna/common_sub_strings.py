#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pydna._py_rstr_max import rstr_max as _rstr_max
import itertools                   as _itertools
from operator import itemgetter    as _itemgetter
'''
    findsubstrings
    ~~~~~~~~~~~~~~

    The Python-dna package.


'''

def common_sub_strings(stringx, stringy, limit=25):
    '''
    common_sub_strings(stringx , stringy , limit=25)

    Finds all the common substrings between stringx and stringy
    longer than limit. This function is case sensitive.

    returns a list of tuples describing the substrings
    The list is sorted longest -> shortest.

    Examples
    --------

    [(startx1,starty1,length1),(startx2,starty2,length2), ...]

    startx1 = position in x where substring 1 starts
    starty1 = position in y where substring 1 starts
    length  = lenght of substring

    '''

    from collections import defaultdict

    rstr = _rstr_max.Rstr_max()
    rstr.add_str(stringx+"&"+stringy)
    r = rstr.go()
    match=defaultdict(int)
    for (offset_end, nb), (l, start_plage) in r.items():
        startsx=[]
        startsy=[]
        if l<limit:
            continue
        for o in range(start_plage, start_plage + nb):
            offset = rstr.idxPos[rstr.res[o]]
            if offset>len(stringx):
                startsy.append(offset-len(stringx)-1)
            else:
                startsx.append(offset)

        for a,b in _itertools.product(startsx, startsy):
            match[(a,b)] = max(match[(a,b)], l)


    match = [ (key[0], key[1] ,val) for key, val in list(match.items())]

    match.sort()

    match.sort(key=_itemgetter(2), reverse=True)

    return match

def terminal_overlap(stringx, stringy, limit=15):
    return [m for m in common_sub_strings(stringx, stringy, limit) if (m[0]==0 and m[1]+m[2]==len(stringy))
                                                                   or (m[1]==0 and m[0]+m[2]==len(stringx))]

if __name__=="__main__":
    import os as _os
    cache = _os.getenv("pydna_cache", "nocache")
    _os.environ["pydna_cache"]="nocache"
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
    _os.environ["pydna_cache"]=cache

    a="GGGCGCGGGCGGNNNNTATATCATATAAA"
    b=                "TATATCATATAAAnnGGGCGCGGGCGG"
    lim = 12
    #a,b=b,a
    print(terminal_overlap(a, b,lim))
    #x,y,l = terminal_overlap(a, b,lim).pop()

    #    x='atctgaacgctttgaatgttgtctctattccacgaggcattcaaaaactggttaccgaacctcaagactaaaagattcttgaccaactctttacccaagtaatggtcaattctgtacaactcttcttctttaaagaggggccccaggtttttttgcagctccctggcagaggccaggtcgtggccgaaaggtttctctacgattacacgggtgatgccattctctgcgtacacacgactcttgatctgcttggccaccgtcaaaaaaacgcttggcggcaaggccagatagaagagacggtgtgggacatcgacgttggcacttttctcgaatttctcgatctgcgttcttaattcgtcgaagccttcatctgtgtcgtaatttcccgaaatgtagctgaccatcttgaagaactgttcgaccttagagtcatcggcttcaccgtgaggttttttcaagtggggtaggacacgggacttcaggtcctcctccatggacaatttggaccgggcataaccgaagatcttggtagatggatcaaggtaaccttctctgaaaagcccaaataaggcgggaaaagtcttcttctttgccagatcacctgacgcaccaaagacagatatgacggtatttttttcgaatttgacggggccttcactcatctgcagcccgggggatccactagttctagaa'
    #    y='atcgataagcttgatatcgaattcctgcagctaattatccttcgtatcttctggcttagtcacgggccaagcgtaagggtgcttttcgggcataacatacttgtgtttttggtaatggtcaattctgtacaactcttcatatattccttcaatccctttggacctcttgatccgtaggggtaaatttccggtgttggaccgtccggacgctctatgtgcttcagtaatggggtgaatatgccccaactgatatccaattcgtcatctctgacaaagttggaatggtcacccagtagggcgtctcttatcaacacctcgtaagcctctggaatccaaaagtcttggtacctgcttgcgtaagttagattcagatctgtgacttgggtagcatttgacagaccaggggtcttagcattaaactttaggtacacagcggcatcgggctgcactctgatgaccagttcgttatttggaatgtctttgaagacacccgatgcgaccgctttgtactgcagtctgatctccaccttggactcattcaaagccttaccggcacgcatcatgatggggacgccctcccaacgctcgttttcgatgttgaaagtcattgctgcaaaagtgacacatttagagtccttgtctacagtgtcatcatccacgtaggcgggcttagacccgtcctcagatttaccgtactggcccaagaggacgtcgtccgtgtcgatgatctgaacgctttgaatgttgtctctattccacgaggcattcaaaaaggggccacggcctttagaaccttaaccttttcgtcacgaatagattccgggtcaaaagacaccggtctttccatagtcaagagagtcatgatttgtaacagatggttctgcatcacgtctctgattatgcctatagagtcgaaatagccgccacggccttcggtgccgaacctctctttaaacgaaatctgaacgctttgaatgttgtctctattccacgaggcattcaaaaa'
    #    print common_sub_strings(x,y)
    #a,b = "taaatc","aaataa"
    #print common_sub_strings(a+a, b, limit = min(25, 25*(len(a)/25)+1))

    #1404
    a= "tcaaaaatcatcgcttcgctgattaattaccccagaaataaggctaaaaaactaatcgcattatcatcctatggttgttaatttgattcgttcatttgaaggtttgtggggccaggttactgccaatttttcctcttcataaccataaaagctagtattgtagaatctttattgttcggagcagtgcggcgcgaggcacatctgcgtttcaggaacgcgaccggtgaagacgaggacgcacggaggagagtcttccttcggagggctgtcacccgctcggcggcttctaatccgtacttcaatatagcaatgagcagttaagcgtattactgaaagttccaaagagaaggtttttttaggctaagataatggggctctttacatttccacaacatataagtaagattagatatggatagttatatggatatgtatatggtggtaatgccatgtaatatgattattaaacttctttgcgtccatccaaaaaaaaagtaagaatttttggatcaataacagtgtttgtggagcattttctgaatacaataaacccaaaacagaaacttcccttttgtatcactgttctggaaaaggggtgggcggtaataaagctaatagggtgtgtccataagtaatactgaacttggaaatgtgcggctttgcagcattttgtctttctataaaaatgtgtcgttcctttttttcattttttggcgcgtcgcctcggggtcgtatagaatatgcgtcacttttaaaaataagattgcagatcagggcaaaacaagtagcaaatcatagcaagagaccctgatttttgtgacataaatatttttacttctgtgttaggttaactttttatgtaactgtaaatggaatagagttgaggggatagtgcccacaagtcaatatgtttattttgtaaagttgaaagataattatttttatgctcaggtgattttggtgttgaattttctgtaatattaacataagagtaatacattgagtggttagtatatggtgtaaaagtggtataacgcatgtattaagagcagttatacaatatttggggccgctgaatgagatatagatattaaaatgtggataatcatgggctttatgggtaaatggaacagggtatagaccactgaggcaagtgccgtgcataatgatatgagtgcatctagtactgatttagtgagagatgggccgtggagtggaatgtgagagtagggtaagttgagagtggtatatacttgtagcatccgtgtgcgtatgccatatcagtatacaagtgaaggtgagtatggcaagtggtggtgggattggtataaagtggtagggtaagtatgtgtgtattatttacgatcgtgccatctgtgcagacaaacgcatcaggatttaaat"

    a= "actctacgacttgatctttacgta"

    #9772
    b= "ccggtgaagacgaggacgcacggaggagagtcttccttcggagggctgtcacccgctcggcggcttctaatccgtacttcaatatagcaatgagcagttaagcgtattactgaaagttccaaagagaaggtttttttaggctaagataatggggctctttacatttccacaacatataagtaagattagatatggatatgtatatggatatgtatatggtggtaatgccatgtaatatgattattaaacttctttgcgtccatccaacgagatctggcgcgccttaattaacccaacctgcattaatgaatcggccaacgcgcggattaccctgttatccctacatattgttcgcgccatctgtgcagacaaacgcatcaggattcagtactgacaataaaaagattcttgttttcaagaacttgtcatttgtatagtttttttatattgtagttgttctattttaatcaaatgttagcgtgatttatattttttttcgcctcgacatcatctgcccagatgcgaagttaagtgcgcagaaagtaatatcatgcgtcaatcgtatgtgaatgctggtcgctatactgctgtcgattcgatactaacgccgccatccagtgtcgaaaacgagctcgaattcatcgatgatatcagatccactagtggcctatgcggccgcggatctgccggtctccctatagtgagtcgatccggatttacctgaatcaattggcgaaattttttgtacgaaatttcagccacttcacaggcggttttcgcacgtacccatgcgctacgttcctggccctcttcaaacaggcccagttcgccaataaaatcaccctgattcagataggagaggatcatttctttaccctcttcgtctttgatcagcactgccacagagcctttaacgatgtagtacagcgtttccgctttttcaccctggtgaataagcgtgctcttggatgggtacttatgaatgtggcaatgagacaagaaccattcgagagtaggatccgtttgaggtttaccaagtaccataagatccttaaatttttattatctagctagatgataatattatatcaagaattgtacctgaaagcaaataaattttttatctggcttaactatgcggcatcagagcagattgtactgagagtgcaccatatgcggtgtgaaataccgcacagatgcgtaaggagaaaataccgcatcaggcgctcttccgcttcctcgctcactgactcgctgcgctcggtcgttcggctgcggcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaaggccagcaaaaggccaggaaccgtaaaaaggccgcgttgctggcgtttttccataggctccgcccccctgacgagcatcacaaaaatcgacgctcaagtcagaggtggcgaaacccgacaggactataaagataccaggcgtttccccctggaagctccctcgtgcgctctcctgttccgaccctgccgcttaccggatacctgtccgcctttctcccttcgggaagcgtggcgctttctcatagctcacgctgtaggtatctcagttcggtgtaggtcgttcgctccaagctgggctgtgtgcacgaaccccccgttcagcccgaccgctgcgccttatccggtaactatcgtcttgagtccaacccggtaagacacgacttatcgccactggcagcagccactggtaacaggattagcagagcgaggtatgtaggcggtgctacagagttcttgaagtggtggcctaactacggctacactagaaggacagtatttggtatctgcgctctgctgaagccagttaccttcggaaaaagagttggtagctcttgatccggcaaacaaaccaccgctggtagcggtggtttttttgtttgcaagcagcagattacgcgcagaaaaaaaggatctcaagaagatcctttgatcttttctacggggtctgacgctcagtggaacgaaaactcacgttaagggattttggtcatgaggggtaataactgatataattaaattgaagctctaatttgtgagtttagtatacatgcatttacttataatacagttttttagttttgctggccgcatcttctcaaatatgcttcccagcctgcttttctgtaacgttcaccctctaccttagcatcccttccctttgcaaatagtcctcttccaacaataataatgtcagatcctgtagagaccacatcatccacggttctatactgttgacccaatgcgtctcccttgtcatctaaacccacaccgggtgtcataatcaaccaatcgtaaccttcatctcttccacccatgtctctttgagcaataaagccgataacaaaatctttgtcgctcttcgcaatgtcaacagtacccttagtatattctccagtagatagggagcccttgcatgacaattctgctaacatcaaaaggcctctaggttcctttgttacttcttctgccgcctgcttcaaaccgctaacaatacctgggcccaccacaccgtgtgcattcgtaatgtctgcccattctgctattctgtatacacccgcagagtactgcaatttgactgtattaccaatgtcagcaaattttctgtcttcgaagagtaaaaaattgtacttggcggataatgcctttagcggcttaactgtgccctccatggaaaaatcagtcaaaatatccacatgtgtttttagtaaacaaattttgggacctaatgcttcaactaactccagtaattccttggtggtacgaacatccaatgaagcacacaagtttgtttgcttttcgtgcatgatattaaatagcttggcagcaacaggactaggatgagtagcagcacgttccttatatgtagctttcgacatgatttatcttcgtttcctgcaggtttttgttctgtgcagttgggttaagaatactgggcaatttcatgtttcttcaacactacatatgcgtatatataccaatctaagtctgtgctccttccttcgttcttccttctgttcggagattaccgaatcaaaaaaatttcaaagaaaccgaaatcaaaaaaaagaataaaaaaaaaatgatgaattgaattgaaaagctagcttatcgatgataagctgtcaaagatgagaattaattccacggactatagactatactagatactccgtctactgtacgatacacttccgctcaggtccttgtcctttaacgaggccttaccactcttttgttactctattgatccagctcagcaaaggcagtgtgatctaagattctatcttcgcgatgtagtaaaactagctagaccgagaaagagactagaaatgcaaaaggcacttctacaatggctgccatcattattatccgatgtgacgctgcagcttctcaatgatattcgaatacgctttgaggagatacagcctaatatccgacaaactgttttacagatttacgatcgtacttgttacccatcattgaattttgaacatccgaacctgggagttttccctgaaacagatagtatatttgaacctgtataataatatatagtctagcgctttacggaagacaatgtatgtatttcggttcctggagaaactattgcatctattgcataggtaatcttgcacgtcgcatccccggttcattttctgcgtttccatcttgcacttcaatagcatatctttgttaacgaagcatctgtgcttcattttgtagaacaaaaatgcaacgcgagagcgctaatttttcaaacaaagaatctgagctgcatttttacagaacagaaatgcaacgcgaaagcgctattttaccaacgaagaatctgtgcttcatttttgtaaaacaaaaatgcaacgcgacgagagcgctaatttttcaaacaaagaatctgagctgcatttttacagaacagaaatgcaacgcgagagcgctattttaccaacaaagaatctatacttcttttttgttctacaaaaatgcatcccgagagcgctatttttctaacaaagcatcttagattactttttttctcctttgtgcgctctataatgcagtctcttgataactttttgcactgtaggtccgttaaggttagaagaaggctactttggtgtctattttctcttccataaaaaaagcctgactccacttcccgcgtttactgattactagcgaagctgcgggtgcattttttcaagataaaggcatccccgattatattctataccgatgtggattgcgcatactttgtgaacagaaagtgatagcgttgatgattcttcattggtcagaaaattatgaacggtttcttctattttgtctctatatactacgtataggaaatgtttacattttcgtattgttttcgattcactctatgaatagttcttactacaatttttttgtctaaagagtaatactagagataaacataaaaaatgtagaggtcgagtttagatgcaagttcaaggagcgaaaggtggatgggtaggttatatagggatatagcacagagatatatagcaaagagatacttttgagcaatgtttgtggaagcggtattcgcaatgggaagctccaccccggttgataatcagaaaagccccaaaaacaggaagattattatcaaaaaggatcttcacctagatccttttaaattaaaaatgaagttttaaatcaatctaaagtatatatgagtaaacttggtctgacagttaccaatgcttaatcagtgaggcacctatctcagcgatctgtctatttcgttcatccatagttgcctgactccccgtcgtgtagataactacgatacgggagcgcttaccatctggccccagtgctgcaatgataccgcgagacccacgctcaccggctccagatttatcagcaataaaccagccagccggaagggccgagcgcagaagtggtcctgcaactttatccgcctccatccagtctattaattgttgccgggaagctagagtaagtagttcgccagttaatagtttgcgcaacgttgttggcattgctacaggcatcgtggtgtcactctcgtcgtttggtatggcttcattcagctccggttcccaacgatcaaggcgagttacatgatcccccatgttgtgcaaaaaagcggttagctccttcggtcctccgatcgttgtcagaagtaagttggccgcagtgttatcactcatggttatggcagcactgcataattctcttactgtcatgccatccgtaagatgcttttctgtgactggtgagtactcaaccaagtcattctgagaatagtgtatgcggcgaccgagttgctcttgcccggcgtcaatacgggataatagtgtatcacatagcagaactttaaaagtgctcatcattggaaaacgttcttcggggcgaaaactctcaaggatcttaccgctgttgagatccagttcgatgtaacccactcgtgcacccaactgatcttcagcatcttttactttcaccagcgtttctgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaataagggcgacacggaaatgttgaatactcatactcttcctttttcaatattattgaagcatttatcagggttattgtctcatgagcggatacatatttgaatgtatttagaaaaataaacaaataggggttccgcgcacatttccccgaaaagtgccacctgctaagaaaccattattatcatgacattaacctataaaaataggcgtatcacgaggccctttcgtctcgcgcgtttcggtgatgacggtgaaaacctctgacacatgcagctcccggagacggtcacagcttgtctgtaagcggatgccgggagcagacaagcccgtcagggcgcgtcagcgggtgttggcgggtgtcggggctggcttaactatgcggcatcagagcagattgtactgagagtgcaccatagatcctgaggatcggggtgataaatcagtctgcgccacatcgggggaaacaaaatggcgcgagatctaaaaaaaaaggctccaaaaggagcctttcgcgctaccaggtaacgcgccactccgacgggattaacgagtgccgtaaacgacgatggttttaccgtgtgcggagatcaggttctgatcctcgagcatcttaagaattcgtcccacggtttgtctagagcagccgacaatctggccaatttcctgacgggtaattttgatttgcatgccgtccgggtgagtcatagcgtctggttgttttgccagattcagcagagtctgtgcaatgcggccgctgaccacatacgatttaggtgacactatagaacgcggccgccagctgaagcttcgtacgctgcaggtcgacggatccccgggttaattaaggcgcgccagatctgtttagcttgccttgtccccgccgggtcacccggccagcgacatggaggcccagaataccctccttgacagtcttgacgtgcgcagctcaggggcatgatgtgactgtcgcccgtacatttagcccatacatccccatgtataatcatttgcatccatacattttgatggccgcacggcgcgaagcaaaaattacggctcctcgctgcagacctgcgagcagggaaacgctcccctcacagacgcgttgaattgtccccacgccgcgcccctgtagagaaatataaaaggttaggatttgccactgaggttcttctttcatatacttccttttaaaatcttgctaggatacagttctcacatcacatccgaacataaacaaccgtcgaggaacgccaggttgcccactttctcactagtgacctgcagccggccaatcacatcacatccgaacataaacaaccatgggtaaaaagcctgaactcaccgcgacgtctgtcgagaagtttctgatcgaaaagttcgacagcgtctccgacctgatgcagctctcggagggcgaagaatctcgtgctttcagcttcgatgtaggagggcgtggatatgtcctgcgggtaaatagctgcgccgatggtttctacaaagatcgttatgtttatcggcactttgcatcggccgcgctcccgattccggaagtgcttgacattggggaattcagcgagagcctgacctattgcatctcccgccgtgcacagggtgtcacgttgcaagacctgcctgaaaccgaactgcccgctgttctgcagccggtcgcggaggccatggatgcgatcgctgcggccgatcttagccagacgagcgggttcggcccattcggaccgcaaggaatcggtcaatacactacatggcgtgatttcatatgcgcgattgctgatccccatgtgtatcactggcaaactgtgatggacgacaccgtcagtgcgtccgtcgcgcaggctctcgatgagctgatgctttgggccgaggactgccccgaagtccggcacctcgtgcacgcggatttcggctccaacaatgtcctgacggacaatggccgcataacagcggtcattgactggagcgaggcgatgttcggggattcccaatacgaggtcgccaacatcttcttctggaggccgtggttggcttgtatggagcagcagacgcgctacttcgagcggaggcatccggagcttgcaggatcgccgcggctccgggcgtatatgctccgcattggtcttgaccaactctatcagagcttggttgacggcaatttcgatgatgcagcttgggcgcagggtcgatgcgacgcaatcgtccgatccggagccgggactgtcgggcgtacacaaatcgcccgcagaagcgcggccgtctggaccgatggctgtgtagaagtactcgccgatagtggaaaccgacgccccagcactcgtccgagggcaaaggaataatcagtactgacaataaaaagattcttgtagggataacagggtaatcggacgcgccatctgtgcagacaaacgcatcaggatagagtcttttgtaacgaccccgtctccaccaacttggtatgcttgaaatctcaaggccattacacattcagttatgtgaacgaaaggtctttatttaacgtagcataaactaaataatacaggttccggttagcctgcaatgtgttaaatctaaaggagcatacccaaaatgaactgaagacaaggaaatttgcttgtccagatgtgattgagcatttgaacgttaataacataacatttttatacttaactatagaaagacttgtataaaaactggcaaacgagatattctgaatattggtgcatatttcaggtagaaaagcttacaaaacaatctaatcataatattgagatgaagagaaagataaaagaaaaaacgataagtcagatgagattatgattgtactttgaaatcgaggaacaaagtatatacggtagtagttccccgagttataacgggagatcatgtaaattgagaaaccagataaagatttggtatgcactctagcaagaaaataaaatgatgaatctatgatatagatcacttttgttccagcgtcgaggaacgccaggttgcccactttctcactagtgacctgcagccgggatcagatctttcaggaaagtttcggaggagatagtgttcggcagtttgtacatcatctgcgggatcaggtacggtttgatcaggttgtagaagatcaggtaagacatagaatcgatgtagatgatcggtttgtttttgttgatttttacgtaacagttcagttggaatttgttacgcagacccttaaccaggtattctacttcttcgaaagtgaaagactgggtgttcagtacgatcgatttgttggtagagtttttgttgtaatcccatttaccaccatcatccatgaaccagtatgccagagacatcggggtcaggtagttttcaaccaggttgttcgggatggtttttttgttgttaacgatgaacaggttagccagtttgttgaaagcttggtgtttgaaagtctgggcgccccaggtgattaccaggttacccaggtggttaacacgttcttttttgtgcggcggggacagtacccactgatcgtacagcagacatacgtggtccatgtatgctttgtttttccactcgaactgcatacagtaggttttaccttcatcacgagaacggatgtaagcatcacccaggatcagaccgatacctgcttcgaactgttcgatgttcagttcgatcagctgggatttgtattctttcagcagtttagagttcggacccaggttcattacctggttttttttgatgtttttcatatgcatggatccggggttttttctccttgacgttaaagtatagaggtatattaacaattttttgttgatacttttattacatttgaataagaagtaatacaaaccgaaaatgttgaaagtattagttaaagtggttatgcagtttttgcatttatatatctgttaatagatcaaaaatcatcgcttcgctgattaattaccccagaaataaggctaaaaaactaatcgcattatcatcctatggttgttaatttgattcgttcatttgaaggtttgtggggccaggttactgccaatttttcctcttcataaccataaaagctagtattgtagaatctttattgttcggagcagtgcggcgcgaggcacatctgcgtttcaggaacgcga"

    print(common_sub_strings(a, b, limit = 29))
    print("[(0, 9552, 224), (220, 0, 198), (420, 200, 67), (1369, 355, 30), (1369, 8033, 29)]")
'''
(1, 1, 2)
(2, 0, 2)
(7, 1, 2)
(8, 0, 2)
(2, 4, 2)
(8, 4, 2)

(1, 0, 2)
(1, 1, 2) 1
(1, 4, 2)
(2, 0, 2) 2
(2, 1, 2)
(2, 4, 2) 3
(7, 0, 2)
(7, 1, 2) 4
(7, 4, 2)
(8, 0, 2) 5
(8, 1, 2)
(8, 4, 2) 6
'''
