'''
# Project Creation Date: 9:18:18 PM, 2/15/2026
'''

#Note - when parsing parenthesis, put them in a nested list, and create a preemptive check for that which solves it before putting it the equation

def parse(full):
    pass

def live_validate(full, new):
    if full == "":
        # - |Rejects invalid first char| - #
        if new not in "1234567890.(-pl":
            return False
    else:
        # - |Rejects incompatible operators| - #
        if new in "+-×÷ ^" and full[-1] in ".":
            return False
        if new in "+×÷ ^" and full[-1] in "(+×÷ ^-":
            return False
        if new == "-":
            if full[-1] == ".":
                return False
            if full[-1] == "-":
                if len(full) == 1 or full[-2] in "+-×÷ ^(":
                    return False
        
        # - |Rejects incompatible right parenthesis| - #
        if new in ")" and full[-1] in "(+×÷ ^-":
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
            if i in "-+×()÷ ^":
                dec_check = False

        if new == "." and full != "" and full[-1] in ".+-×÷ ^(":
            return False
        if new == "." and dec_check:
            return False

        # - |Rejects numbers after closing paren| - #
        if new in "0123456789" and full != "" and full[-1] == ")":
            return False
    
    return True