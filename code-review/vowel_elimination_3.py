import re

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    m = re.findall(r"[^aeiuoAEIOU]", s)

    print(m)

if __name__ == "__main__":
    s = input()
    print_without_vowels(s)  