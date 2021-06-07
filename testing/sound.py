import winsound
import time

def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()


frequency = 1000000

for i in range(10):
    winsound.Beep(3000,1)
