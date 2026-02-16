'''
# Project Creation Date: 9:18:18 PM, 2/15/2026
'''

#Note: When parsing parenthesis, put them in a nested list, and create a preemptive check for that which solves it before putting it the equation

def validate(full, new):
    # - |Rejects invalid first char| - #
    if new not in "1234567890.(-pl" and full == "":
        return False
    
    # - |Rejects operators after incompatible| - #
    if new in "+-x*/^" and full[-1] in ".":
        return False
    if new in "+x*/^" and full[-1] in "(+x*/^-":
        return False
    
    # - |Rejects right parenthesis after incompatible| - #
    if new in ")" and full[-1] in "(+x*/^-":
        return False
    
    # - |Rejects right parenthesis after incompatible| - #
    if new in "." and full[-1] in ".":

    
    return True