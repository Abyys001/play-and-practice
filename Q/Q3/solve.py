# usr/bin/python3


# moudles 
import sys
import time
'''

'''
# variables
CURRENT_YEAR = 1402  


def getNameAndAge():
    while True:
        try: 
            name1 = input("name of the first person: ")
            age1 = int(input("his/her year of brith: "))
            name2 = input("name of the second person: ")
            age2 = int(input("his/her year of birth: "))
            break
        except:
            print("INVALID VALUE!!")

    data = [name1, age1, name2, age2]

    return data


class CalculateAgeDifference:


    def __init__(self,data) -> None:
        self.name1 = data[0]
        self.name2 = data[2]
        self.age1 = data[1]
        self.age2 = data[3]
    
    def check_validity(self):
        if self.age1 <= 1300 or self.age2 <= 1300:
            raise ValueError("INVALID VALUE")
        if self.age1 > CURRENT_YEAR or self.age2 > CURRENT_YEAR:
            raise ValueError("INVALID VALUE")

    def date_to_age(self):
        self.age1 = CURRENT_YEAR - self.age1
        self.age2 = CURRENT_YEAR - self.age2

    def find_older(self):
        if self.age1 == self.age2:
            self.same_age = True
            return f'{self.name1} and {self.name2} are the same age'

        if self.age1 > self.age2:
            difference = self.age1 - self.age2
            return f'{self.name1} is {difference} year older than {self.name2}'
        if self.age2 > self.age1:
            difference = self.age2 - self.age1
            return f'{self.name2} is {difference} year older than {self.name1}'


    def show_data(self):
        print(f"Hello {self.name1}, you are {self.age1} years old")
        # time.sleep(1)
        print(f"Hello {self.name2}, you are {self.age2} years old")
        # time.sleep(1)
        print(self.find_older())


    def run_class(self):
        self.check_validity()
        self.date_to_age()
        self.show_data()


if __name__ == "__main__":
    data = getNameAndAge()
    calculate = CalculateAgeDifference(data)
    calculate.run_class()