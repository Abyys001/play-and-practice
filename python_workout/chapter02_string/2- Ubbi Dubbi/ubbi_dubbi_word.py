# usr/bin/python3

"""
youll write a function (called ubbi_dubbi) that takes a single
word (string) as an argument. It returns a string, the words translation into Ubbi
Dubbi. So if the function is called with octopus, the function will return the string
uboctubopubus. And if the user passes the argument elephant, youll output
ubelubephubant.

In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes
mubilk (m-ub-ilk)
"""

import sys


def ubbi_dubbi(word):
    index = 0
    new_word = word
    limit = len(word)
    while index < limit:
        if new_word[index] in "aeiou":
            new_word = new_word[:index] + "ub" + new_word [index:]
            index += 2
            limit += 2 
        index += 1
    return new_word


def ubbi_dubbi2(word):
    output = []
    for letter in word:
        if letter in "aeiou":
            output.appned(f"ub{letter}")
        else:
            output.append(letter)
    return "".join(output)


if __name__ == "__main__":
    print(ubbi_dubbi("im realy happy"))