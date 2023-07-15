# usr/bin/python3

"""
"""


def lazy_hacker():
    # taking data and cleaning 

    total_tasks = int(input())
    taks_times = input()
    tasks = []
    tasks = taks_times.split(" ")
    tasks.sort(reverse=True)

    if len(tasks) != total_tasks:
        print("Please enter correct data")
        quit()

    # The process of data and doing

    # hacker_time = 0  
    # flag = True

    # while flag:

    #     if len(tasks) >= 2:

    #         del tasks[0:2]

    #         if len(tasks) >= 1:

    #             hacker_time += int(tasks[-1])
    #             del tasks[-1]
    #     else:
    #         flag = False
    return tasks


if __name__ == "__main__":
    print(lazy_hacker())
    # pdb.set_trace()
