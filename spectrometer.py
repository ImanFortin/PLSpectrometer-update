import nidaqmx
import math
import time
from nidaqmx.constants import AcquisitionType
from miscellaneous import sleep

class Spectrometer():

    '''spectrometer class the only object is the position but the communication
    with the DAQ is handled in this class and not the UI, it will eventually also
    store a DAQ instance'''


    def __init__(self,device, shutter_prt = '/port1/line1', direction_prt = '/port1/line3'):
        #open file where we will store the last position
        try:
            f = open(device + '_last_position.txt', 'r')
            self._position = float(f.readline())
            print(self.position)
            f.close()
        except:
            print("there was an error trying to load the data from last_position.txt")
            self._position = 0.0
        else:
            print(f'successfully loaded last position for {device}\n')

        #makes testing easier since trying to access a channel that doesn't exist
        #or is in use will cause the program to crash
        try:
            self.shutter = nidaqmx.Task()#task to control the shutter
            #port that we send signals to, if the port changes change this
            self.shutter.do_channels.add_do_chan(device + shutter_prt)
            self.shutter.start()

            self.direction = nidaqmx.Task()
            self.direction.do_channels.add_do_chan(device + direction_prt)
            self.direction.start()

        except:
            print(f'the device or channel name you entered for {device} may be incorrect or you may have an unclosed window running')
            print(f'you will be unable to send commands to this daq: {device}\n')

        self.name = device
        self.frequency = 2000#frequency of pulses generated

    #getter method google @property for reasoning
    #short description it allows us to sanitaze the inputs while keeping the syntax neat
    @property
    def position(self):
        return self._position

    #setter method related to @property
    #IMPORTANT TO UNDERSTAND WHAT THIS DOES
    @position.setter
    def position(self,wavelength):
        #check these conditons before accepting a value when assigning a value to position
        if isinstance(wavelength, float) and wavelength >= 0 and wavelength < 1300:
            self._position = wavelength
        else:#will crash the program stopping the scan (can't stop a move)
            raise ValueError("spectrometer position must be between 0 and 1300")
        return

    #print function for the spectrometer function (useless might delete)
    def __str__(self):
        return str(self.position)

    def open_shutter(self):
        #set voltage to zero
        self.shutter.write(False)

    def close_shutter(self):
        #set voltage to 5
        self.shutter.write(True)

    #sets the direction of the move to be called before the move and
    def set_direction(self,direction):
        if direction > 0:
            self.direction.write(True)
        else:
            self.direction.write(False)

    #save the last position
    def save(self):
        try:
            f = open(self.name + '_last_position.txt', 'w')
            f.write(str(self.position))
            f.close()
        except:
            print(f'there was an error writing to {self.name}_last_position.txt')
        else:
            print(self.position)
            print(f'position of {self.name} saved')


    def move(self,distance,**kwargs):
        #passing zero pulses to the channnel will cause an error
        if distance == 0:
            return
        #calculate the amount of pulses its 4 pulses for 0.001nm of movement
        pulse_count = int(distance * 4000)
        print(pulse_count)
        #ensures that the task is closed properly when done
        with nidaqmx.Task() as task:
            #can't have two counter channels at once (co or ci), so important that this is closed
            task.co_channels.add_co_pulse_chan_time(self.name + "/ctr0",**kwargs)
            #AcquisitionType.FINITE changes the mode to send a set number of pulses
            #samps per chan is the number of pulses to send
            task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE, samps_per_chan=pulse_count)
            task.start()
            task.wait_until_done(timeout = math.inf)#need to wait until done before continuing
        print('done')


    def read(self, count_time):
        with nidaqmx.Task() as task:#open a task
             task.ci_channels.add_ci_count_edges_chan(self.name +"/ctr0")#start a count channel
             task.ci_channels[0].ci_count_edges_term = '/'+self.name+'/PFI0'#set the terminal
             task.start()#start counting
             sleep(count_time)#wait the count time
             data = task.read()#read the counts
        return data/count_time#return the average count/s

    def recalibrate(self,wavelength):
        self.position = wavelength#change the stored position


    #closes the tasks properly upon closing the application
    def close_channels(self):
        try:
            #sets the voltages to zero, if not done daq will continue to ouput
            #this could be desirable I'm not sure
            self.shutter.write(False)
            self.direction.write(False)
            self.shutter.stop()
            self.shutter.close()
            self.direction.stop()
            self.direction.close()
        except:
            print('there was an error when closing the tasks')
        else:
            print('spectrometer closed')


if __name__ == '__main__':
    test = Spectrometer('Dev1')
    time.sleep(20)
