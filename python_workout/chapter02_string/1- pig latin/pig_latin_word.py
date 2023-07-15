# usr/bin/python3 

"""
write a Python function (pig_latin) that takes a string as input,
assumed to be an English word. The function should return the translation of this word
into Pig Latin. You may assume that the word contains no capital letters or punctuation.

translating words from English into Pig Latin are quite simple:

1.  If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
2.  If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”

beyond exercise:

1. Handle capitalized words
2. 
"""

def pig_latin(word):
    if word[0].lower() in "aeiou":    
        return f"{word}way"
    else:
        try:
            return f"{word[1].upper()}{word[2:]}{word[0]}ay"
        except IndexError:
            return f"{word[1].upper()}{word[0]}ay"
    


if __name__ == "__main__":
    print(pig_latin("hgh"))