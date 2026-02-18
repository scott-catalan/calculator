'''
# Project Creation Date: 9:18:18 PM, 2/15/2026
'''

#Note - when parsing parenthesis, put them in a nested list, and create a preemptive check for that which solves it before putting it the equation
from sympy import sympify, pi, log

def calculate(full):
    for i in full:
        if i == "l"

def validate(full):
    if full == "":
        return False

    # - |Rejects ending operator/decimal/log| - #
    if full[-1] in "+-×÷ ^.g(":
        return False

    # - |Rejects ending open parenthesis| - #
    if full[-1] == "(":
        return False

    # - |Rejects non-balanced parenthesis| - #
    if full.count("(") != full.count(")"):
        return False

    return True


def live_validate(full, new):
    if full == "":
        # - |Rejects invalid first char| - #
        if new not in "1234567890.(-πl":
            return False
    else:
        last = full[-1]

        # - |Rejects implicit| - #
        if full[-1] in "0123456789π)":
            if new in "π(l" or new == "log(":
                return False

        # - |Rejects incompatible pi| - #
        if new == "π":
            if last in "0123456789.π)":
                return False
        if last == "π" and new in "0123456789.π":
            return False
        if full[-1] == "π" and new in "0123456789.":
            return False
        
        # - |Rejects incompatible log| - #
        if new == "log(":
            if last in "0123456789.π)":
                return False
        if last == "(" or full.endswith("log("):
            if new in "+×÷ ^.)":
                return False

        # - |Rejects incompatible operators| - #
        if new in "+-×÷ ^" and last in ".":
            return False
        if new in "+×÷ ^" and last in "(+×÷ ^-":
            return False
        if new == "-":
            if last == ".":
                return False
            if last == "-":
                if len(full) == 1 or full[-2] in "+-×÷ ^(":
                    return False
        
        # - |Rejects incompatible right parenthesis| - #
        if new in ")" and last in "(+×÷ ^-":
            return False

        # - |Rejects unmatched right parenthesis| - #
        if new == ")":
            if full.count("(") <= full.count(")"):
                return False
        
        # - |Rejects incompatible decimals| - # 
        dec_check = False
        for i in full:
            if i == ".":
                if dec_check:
                    return False
                dec_check = True
            if i in "-+×()÷ ^π":
                dec_check = False

        if new == "." and full != "" and last in ".+-×÷ ^(π":
            return False
        if new == "." and dec_check:
            return False

        # - |Rejects numbers after closing parenthesis| - #
        if new in "0123456789" and full != "" and last == ")":
            return False
    
    return True