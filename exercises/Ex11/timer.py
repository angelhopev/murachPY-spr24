#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print(f"Start time: {start_time:%X.%f}") # print("Start time:", start_time)
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print(f"Start time: {start_time:%X.%f}") # print("Stop time: ", stop_time)
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    if hours > 0 or minutes > 0:
        print(f"Hours/minutes: {time_object:%H:%M}")
    print(f"Seconds: {time_object:%S.%f}")
    # if days > 0:
    #     print("Days:", days)
    # print("Time:", time_object)

if __name__ == "__main__":
    main()
