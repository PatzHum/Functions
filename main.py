__author__ = 'Patrick'

import bedmas

function = raw_input("f(x) = ")
x = raw_input("x = ")
while 'x' in function:
    for i,j in enumerate(function):
        if j == 'x':
            function = function [:i] + str(x) + function [i+1:]
            print function
            break
print function
print bedmas.bedmas(function)
print ""