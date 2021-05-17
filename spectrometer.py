import numpy as np


class Spectrometer():
    def __init__():

        f = open('last_position', 'r')
        try:
            self.position = float(f.readline())
        except:
            print("there was an error trying to load the last position from 'last_position'")

        f.close()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self,wavelength):
        if isinstance(wavelength, float) and wavelength < 0:
            self._position = wavelength

        else:
            print('not valid entry')
        return


    def recalibrate(self,wavelength):
        self.position = Wavelength

    def move(self,wavelength):
        pass


    def scan(self,start,end,step):
        pass

    def close(self):
        f = open('last_position', 'w')
        f.write(self.position)
        f.close()
