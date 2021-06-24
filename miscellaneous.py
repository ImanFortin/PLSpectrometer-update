import time
import os
from datetime import datetime
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
        if dot == -1:#if there is no dot do this
            if depth == 0:
                filename = filename + ' (1)'

            else:
                filename = filename[:-2] + str(depth + 1) + ')'
        else:#If there is a dot do this
            if depth == 0:
                filename = filename[:dot] + '(' + str(depth + 1) + ')' + filename[dot:] #add the brackets and number before the dot
            else:
                filename = filename[:dot - 2] + str(depth + 1) + filename[dot - 1:]#replace the number

        exists = os.path.exists(filename)
        depth += 1

    return filename

#function to make header it takes f as in f = open(filename, 'w'), the smaple id and the count time
def make_header(f, sample_id, time_avg):
    f.write('Sample ID:\t\t' + sample_id + '\n')
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f.write('start Time:\t\t' + dt_string + '\n')
    f.write('Averaging Time:\t\t' + str(time_avg) + '\n\n')

#find minimum function for finding the the minimum distance in cursors
def find_minimum(xdata,ydata, cmpr_x, cmpr_y):
    if len(xdata) == 0:
        return None
    minimum = cmpr_x**2 + cmpr_y**2#set a baseline minimum
    min_i = 0
    for i in range(len(xdata)):
        distance = (cmpr_x - xdata[i])**2 + (cmpr_y - ydata[i])**2
        if distance < minimum:
            minimum = distance
            min_i = i
    return min_i#returns the index that this happens at not the value
