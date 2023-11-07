"""
author: Siavash Darvishi 

This function (permute) returns all permutations of the 
number or string that we enter into it.

"""

# Given two arrays, check if one array is
# stack permutation of other.


# function to check if input array is
# permutable to output array
def checkStackPermutation(ip, op):
    # we will be appending elements from input array to stack uptill top of our stack
    # matches with first element of output array
    s = []

    # will maintain a variable j to iterate on output array
    j = 0

    # will iterate one by one in input array
    for i in range(len(op)):
        # appended an element from input array to stack
        s.append(ip[i])

        # if our stack isn't empty and top matches with output array
        # then we will keep popping out from stack uptill top matches with
        # output array
        while len(s) > 0 and s[-1] == op[j]:
            s.pop()

            # increasing j so next time we can compare next element in output array
            j += 1

    # if output array was a correct permutation of input array then
    # by now our stack should be empty
    if len(s) == 0:
        return True

    return False

def convertToList(item):
    List = []
    List.extend(item)
    return List


lst = []


def permute(item, l):
    # l is first index of the item

    if type(item) != list:
        item = convertToList(str(item))
        # TODO: this app is not fully complete you have to find someway to keep stack to checkpermiutation fucntionF

    r = len(item)

    if l == r:
        temp = "".join(item)
        # print("".join(item))
        lst.append(temp)
    else:
        for i in range(l, r):
            item[l], item[i] = item[i], item[l]
            permute(item, l + 1)
            item[l], item[i] = item[i], item[l]


# ---------- main -------------

if __name__ == "__main__":
    number = "1234"
    permute(number, 0)
    x = convertToList(number)

    for i in range(len(lst)):
        y = convertToList(lst[i])
        if checkStackPermutation(x, y):
            print(lst[i])

    print("----------------")
