#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Patrick'

import re

def bedmas(Equation):
    def parse_brackets(equation):
        bracket_locs = [[]]
        layer_num = 0
        deepest_layer = 0
        for i, j in enumerate(equation):
            if j == '(':        # If the object is an open bracket
                bracket_locs[layer_num].append([i])     # Add a new array to its the right bracket layer
                layer_num += 1      # Make the current layer deeper
                if layer_num > deepest_layer:   # If the current layer is deeper than deepest layer, make a new layer
                    bracket_locs.append([])
                    deepest_layer += 1
            if j == ')':    # If the object is a close bracket
                for k in bracket_locs[layer_num-1]:     # Loop through the bracket locations and add the location to
                #  the first one not a pair then append the location to the single
                    if len(k) == 1:
                        k.append(i)
                layer_num -= 1      # Make the current layer less deep
        bracket_locs.pop()  # Remove a blank list created
        bracket_locs.reverse()  # Reverse the list so the deepest goes first
        return bracket_locs

    def edmas(equation):
        equation = re.split('([^a-zA-Z0-9._])', equation)

        ## This function takes a operator as string and returns the operator used on two numbers
        def oper(operator, n1, n2):
            if operator == '+':
                return n1 + n2
            if operator == '-':
                return n1 - n2
            if operator == '*':
                return n1 * n2
            if operator == '/':
                return n1 / n2
            if operator == '^':
                return n1 ** n2

        ## Loops through the equation and looks for a operator then solves accordingly
        def solve(operator, Equation):
            i = 0
            while i <= len(Equation)-1:
                j = Equation[i]
                if Equation[0] == '' and Equation[1] == '-':
                    Equation = [("-" + Equation[2])]
                elif j == operator:
                    print equation
                    Equation[i-1] = oper(operator, float(Equation[i-1]), float(Equation[i+1]))
                    Equation.pop(i)
                    Equation.pop(i)
                    i -= 2
                i += 1
            return Equation

        order_of_operators = ['^', '/', '*', '-', '+']

        for i in order_of_operators:
            equation = solve(i, equation)

        return equation


    Equation = "(" + Equation + ")"
    brackets = parse_brackets(list(Equation))

    while brackets != []:
        brackets = parse_brackets(list(Equation))
        for i in brackets:
            for j in i:
                Equation = Equation[:j[0]] + str(edmas(Equation[j[0]+1:j[1]])[0]) +  Equation[j[1]+1:]
                break
            break

    return edmas(Equation)

#(3*3-9)*9/1/9*5