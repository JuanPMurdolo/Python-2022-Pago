'''
Complete the method/function so that it converts 
dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized 
only if the original word was capitalized (known as Upper Camel 
Case, also often referred to as Pascal case).


'''

def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])


'''
There exist two zeroes: +0 (or just 0) and -0.

Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).

In JavaScript / TypeScript / Coffeescript the input will be a number.

In Python / Java / C / NASM / Haskell / the input will be a float.


'''

import struct

def is_negative_zero(n):
    valor = float_a_hex(-0.0)
    if float_a_hex(n) == valor:
        return True
    else:
        return False
    
def float_a_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f',f))[0])
