import nidaqmx

import time

class Spectrometer():

    '''spectrometer class the only object is the position but the communication
    with the DAQ is handled in this class and not the UI, it will eventually also
    store a DAQ instance'''

    #init function
    def __init__(self,device):
        #open file where we will store the last position
        try:
            f = open(device + '_last_position.txt', 'r')
            self._position = float(f.readline())
            f.close()
        #if file was missing or empty set the value to zero
        except:
            print("there was an error trying to load the data from last_position.txt")
            self._position = 0.0
        #print success if the except doesn't trigger
        else:
            print(f'successfully loaded last position for {device}\n')

        try:
            self.shutter = nidaqmx.Task()
            #probably need to change the path name when in real spectrometer
            self.shutter.do_channels.add_do_chan(device +'/port0/line0')
            self.shutter.start()

            self.direction = nidaqmx.Task()
            self.direction.do_channels.add_do_chan(device +'/port0/line7')
            self.direction.start()

            self.move = nidaqmx.Task()
            self.move.do_channels.add_do_chan(device +'/port0/line2')
            self.move.start()

        except:
            print(f'the device or channel name you entered for {device} may be incorrect or you may have an unclosed window running')
            print(f'you will be unable to send commands to this daq: {device}\n')

        self.name = device

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
        else:
            print('invalid input')
        return

    #print function for the spectrometer function
    def __str__(self):
        #for now will only print the position
        return float(self.position)

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

    def take_steps(self,n,hightime,lowtime):
        for i in range(n):
            self.move.write(True)
            time.sleep(hightime)
            self.move.write(False)
            time.sleep(lowtime)

    def save(self):
        try:
            #open the file where we save the information
            f = open(self.name + '_last_position.txt', 'w')
            #write the last position
            f.write(str(self.position))
            #close
            f.close()
        #if there is an error with the write print
        except:
            print(f'there was an error writing to {self.name}_last_position.txt')
        #if we succeed print success message
        else:
            print(f'position of {self.name} saved')



    def recalibrate(self,wavelength):
        self.position = wavelength

    #closes the tasks properly
    def close_channels(self):
        try:
            self.shutter.write(False)
            self.direction.write(False)
            self.shutter.stop()
            self.shutter.close()
            self.direction.stop()
            self.direction.close()
            self.move.stop()
            self.move.close()
        except:
            print('there was an error when closing the tasks')
        else:
            print('spectrometer closed')


if __name__ == '__main__':
    test = Spectrometer('Dev1')
    time.sleep(20)
