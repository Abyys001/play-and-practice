# usr/bin/python3 

"""
mySum 

write a program 
that summing numebrs
"""
 
def mySum(*numbers):
    sum = 0
    for arg in numbers:
        sum += arg
    return sum 


def myAvg(*numbers):
    avg = 0
    for arg in numbers:
        avg += arg
    avg /= 2
    return avg

if __name__ == "__main__":
    # print(mySum(*[23,11,11]))
    print(myAvg(10,20,30))

