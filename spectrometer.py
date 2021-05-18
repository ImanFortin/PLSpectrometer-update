


class Spectrometer():

    '''spectrometer class the only object is the position but the communication
    with the DAQ is handled in this class and not the UI, it will eventually also
    store a DAQ instance'''


    #init function
    def __init__(self):
        #file where we will store the last position
        try:
            f = open('last_position.txt', 'r')
            last_position = float(f.readline()
        except:
            print("there was an error trying to load the data from last_position.txt")
            last_postion = 0.0
        #print success if the except doesn't trigger
        else:
            print('successfully loaded last position\n')
        #close the file always
        finally:
            f.close()

        #set the position the underscore is necessary
        #it implies that this should not be accessed directly see the position
        #function below for how accessing and changing the value work
        self._position = last_position

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
        if isinstance(wavelength, float) and wavelength > 0:
            self._position = wavelength
        else:
            print('not valid entry')
        return

    #print function for the spectrometer function
    def __str__(self):
        #for now will only print the position
        return float(self.position)


    def recalibrate(self,wavelength):
        self.position = wavelength



#Methods to be implemented later
    def move(self,wavelength):
        pass


    def scan(self,start,end,step):
        pass

    def abort():
        pass

    def stop():
        pass

    def save(self):
        try:
            #open the file where we save the information
            f = open('last_position.txt', 'w')
            #write the last position
            f.write(str(self.position))

        #if there is an error with the write print it
        except:
            print('there was an error writing to last_position.txt')
        #if we succeed print success message
        else:
            print('position saved')
        #no matter what happens close the file
        finally:
            f.close()
