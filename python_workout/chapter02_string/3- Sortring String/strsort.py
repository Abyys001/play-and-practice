"""
in this practice you are going to wirte a functions named srtsort, that takes a
single string as its input and returns a string. The returned string should contain the
same characters as the input, except that its characters should be sorted in order, from
the lowest Unicode value to the highest Unicode value. For example, the result of
invoking strsort('cba') will be the string abc.
"""

def strsort(word):
    try:
        word = str(word)
        word_list = []
        for char in word:
            word_list.append(char)
        # for sorting chars in word_list i use this sorting algorithm 
        # but this algorithm uses for java so i do a little bit chnages 
        for i in range(len(word_list)):
            j = i + 1
            while j < len(word_list):
                if word_list[i] > word_list[j]:
                    word_list[i],word_list[j] = word_list[j], word_list[i] 
                j += 1
    except:
        raise ValueError("word can not be non-string or numerical value!!")
    
    sorted_word = ''.join(word_list)

    return sorted_word
    

def strsort_using_method(word):
    sorted_word = ''.join(sorted(word))
    return sorted_word

if __name__ == "__main__":
    print(strsort("Tom Dick Harry"))
    print(strsort_using_method("sdfkjsadsdfa"))
