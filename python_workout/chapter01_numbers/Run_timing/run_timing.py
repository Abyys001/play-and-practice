# usr/bin/python3

"""
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until
the user presses Enter. At that point, the function exits—but only after calculating and
displaying the average time that the 10 km runs took.
"""


def rum_timeing():
    """Asks the user repeatedly for numeric input.
     Prints the average time and number of runs."""
    number_of_runs = 0 # counting the number of runs
    total_run = 0 
    while True:
        time = input("Enter 10 km rum time: ")
        try: 
            time = float(time)
            total_run += time
            number_of_runs += 1
        except ValueError:
            if not time:
                if number_of_runs == 0:
                    average_time = 0
                else:
                    average_time = total_run / number_of_runs
                break
            else:
                print("Invalid value!!")
        
    print(f"Average of {average_time:.2f}, over {number_of_runs} runs.")

if __name__ == "__main__":
    rum_timeing()