#!/usr/bin/python3
def no_c(my_string):
    slist = list(my_string)
    for i in range(len(slist)):
        if slist[i] is 'C' or slist[i] is 'c':
            del slist[i]
