# usr/bin/python3

# module 
from math import ceil
"""

"""

def parketParty():
    while True:
        try: 
            areaLength = int(input())
            areaWideth = int(input())
            parketLength = int(input())
            parketWideth = int(input())
            break
        except: 
            print("ENTER VALID VALUE")
        

    landArea = areaLength * areaWideth
    parketArea = parketWideth * parketLength

    parketNeeded = landArea // parketArea

    return ceil(parketNeeded)


if __name__ == "__main__":
    print(parketParty())