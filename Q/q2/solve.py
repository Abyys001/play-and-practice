# /usr/bin/activate

# modules 
import sys
'''

'''
# variables 
DAY_SECONDS = 86400
HOUR_SECONDS = 3600
MINUTE_SECONDS = 60


time_of_explosion = input("""
    how much time left?!
                          
""")
                          
try:
    time_of_explosion = int(time_of_explosion)
except:
    print("I AM JOKE TO YOU")
    sys.exit()
    

def claculate_remain_time(boom_time):

    if boom_time / DAY_SECONDS != 0:
        day = boom_time // DAY_SECONDS
        boom_time %= DAY_SECONDS
    else: 
        day = 00
    
    if boom_time / HOUR_SECONDS != 0:
        hour = boom_time // HOUR_SECONDS
        boom_time %= HOUR_SECONDS
    else: 
        hour = 00
    
    if boom_time / MINUTE_SECONDS != 0:
        minute = boom_time // MINUTE_SECONDS
        boom_time %= MINUTE_SECONDS
    else:
        minute = 00
    
    if boom_time <= 60:
        second = boom_time
    
    remain_time = f'{day}:{hour}:{minute}:{second}'

    return remain_time




if __name__ == "__main__":
    print(claculate_remain_time(time_of_explosion))