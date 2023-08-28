import time

print("Enter time for count down ")
hour = int(input("Enter hours: "))
min = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))


def count_down():
    global hour, min, sec  # Declare as global to modify them
    while hour > 0 or min > 0 or sec > 0:
        hour_str = f"{hour:02d}"   # formatting strings for printing
        minute_str = f"{min:02d}"
        second_str = f"{sec:02d}"
        print(f"{hour_str}:{minute_str}:{second_str}")
        time.sleep(1)
        sec = sec -1
        if sec < 0:
            sec = 59
            min = min -1
            if min < 0:
                min = 59
                hour = hour - 1

    print("OO:OO:OO") 


count_down()



