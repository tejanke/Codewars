import string
import re

def is_pangram(s):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sentence = []
    for l in s:
        l = l.lower()
        if re.match("[a-z]",l):
            if l not in sentence:
                sentence.append(l)
    sentence.sort()
    if letters == sentence:
        return True
    else:
        return False
