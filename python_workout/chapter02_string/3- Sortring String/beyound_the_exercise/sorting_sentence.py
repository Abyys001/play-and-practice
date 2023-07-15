"""
as the last exercise we see the method sorting one word but on this file we want to do this with sentence
"""
sorted
def strsort(word):
    sorted_list = []
    try:
        word = str(word)
        word_lists = word.split(" ")
        for w in word_lists:
            word_list = []
            for char in str(w).lower():
                word_list.append(char)
            # for sorting chars in word_list i use this sorting algorithm 
            # but this algorithm uses for java so i do a little bit chnages 
            for i in range(len(word_list)):
                j = i + 1
                while j < len(word_list):
                    if word_list[i] > word_list[j]:
                        word_list[i],word_list[j] = word_list[j], word_list[i] 
                    j += 1
            for char in word_list:
                
                sorted_list.append(char)
            sorted_list.append(",")
        del sorted_list[-1]
        sorted_word = ''.join(sorted_list)

    except:
        raise ValueError("word can not be non-string or numerical value!!")
    return sorted_word
    
if __name__ == "__main__":
    print(strsort("Tom Dick Harry"))