import time

def epoch_time():
    print(time.time())

def current_date():
    t = time.localtime()
    year, month, day = t[0], t[1], t[2]
    print(str(month) + "/" + str(day) + "/" + str(year))

def sleep(sec):
    time.sleep(sec)