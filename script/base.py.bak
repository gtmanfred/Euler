"""
Matt Laporte <lapo3399@gmail.com> 2008
---
Base conversion tools. Allows for A-Z notation for digits greater than 9.
"""
from types import StringType

def inBase(num, base, fromBase = 10, result = ''):
    """ 
    Converts any number in fromBase to its representation in base.
    Defaults to converting to base_num from base_10.
    """
    if result == '': 
        #First call checks and corrections.
        if num == 0: return '0' 
        base = __check(base)
        if fromBase != 10: 
            fromBase = __check(fromBase)
            """ In order to maintain the simplicity of the actual
            conversion, this converts the number to base_10. """
            num = toBase10(num, fromBase)
            fromBase = 10
        if num < 0: 
            #Further simplification for the conversion component.
            result = '-' + result
            num = -1 * num
    if num == 0: return result #Return the final result when num has been handled.
    else:
        #Conversion. This builds up result and eats away at num.
        thisDigit = num%base
        if thisDigit > 9: thisDigit = chr(thisDigit + 55) #Accounting for A-Z digits.
        else: thisDigit = str(thisDigit)
        return inBase(num/base, base, fromBase, thisDigit + result)

def __check(base):
    """ 
    Verifies that a given base is 2-9 or A-Z.
    Converts any base from A-Z to 10-35 for numerical calculations.
    Should be used in the form: base == __check(base).
    """
    if type(base) == StringType and ((ord(base) > 96) and (ord(base) < 123)):
        #Correct a-z to A-Z
        base = chr(ord(base)-32)
    if type(base) == StringType and ((ord(base) > 64) and (ord(base) < 91)):
        #Correct A-Z to 10-35
        return (ord(base) - 55)
    elif type(base) != type(1) or type(base) == StringType:
        #Not an integer, or any string other than A-Z.
        raise TypeError, 'invalid base type for inBase()'
    if base <= 1 or base > 36:
        raise ValueError, 'invalid base for inBase(): %s' % base
    return base

def toBase10(num, base):
    """ 
    Converts any number represented in base to its base_10 representation.
    """
    sum = 0
    parseNum = str(num)
    indices = range(len(parseNum)) #Exponents depend on digit place, indices necessary.
    for i in indices:
        #Add the decimal representations of the digits.
        sum += int(parseNum[i])*base**int(indices[::-1][i])
    return sum
