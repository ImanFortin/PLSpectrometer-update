import time
import os

#high precision sleep function from testing on syzygy accurate to about 1e-6
def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()

#avoid overwriting data
def available_name(filename):

    exists = os.path.exists(filename)

    depth =  0

    while exists:
        dot = filename.find('.')
         #if there is no postfix set dot to zero
        if dot == -1:
            dot = 0

        if depth == 0:
            filename = filename[:dot] + '(' + str(depth + 1) + ')' + filename[dot:] #add the brackets and number before the dot
        else:
            filename = filename[:dot - 2] + str(depth + 1) + filename[dot - 1:]#replace the number

        exists = os.path.exists(filename)
        depth += 1

    return filename

def make_header(sample_id):
    pass
