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

"""
def pig_latin(string):
    english_words = string.split()
    pig_latin_words = []
    for word in english_words:
        if word[0] in "aeiou":
            new_word = f""
            pig_latin_words.append(new_word)
        else:
            new_word = word[1:] + word[0] + "ay"
            pig_latin_words.append(new_word)
    pig_latin = " ".join(pig_latin_words)

    return pig_latin





if __name__ == "__main__":
    print(pig_latin("hey my name is siavash"))