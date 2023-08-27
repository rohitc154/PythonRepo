# Write a python program to translate a message into secret code language. Use the rules below to translate normal english into secret code language

# Coding:
# If the word contains atleast 3 characters, remove the first letter and append it at the end
# Now append three random characters at the starting and the end
# else: Simply reverse the string

# Decoding:
# If the word contains less than 3 characters, reverse it
# else : Remove 3 random characters from start and end, Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

from random import *
from string import *

s = input("Enter a String : ")
fc = s[0]
l = len(s)

if l >= 3:
    s = s.replace(fc,'')
    s = s+fc
    # randchar = ''.join(random.choices(string.)))
    print(s)
    print(len(s))
