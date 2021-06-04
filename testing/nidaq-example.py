import nidaqmx
from nidaqmx.types import CtrTime
from nidaqmx.constants import AcquisitionType
import time
import math



def move(self,stepsize,**kwargs):
    pulse_count = int(stepsize/0.001)
    print(pulse_count)
    with nidaqmx.Task() as task:
        task.co_channels.add_co_pulse_chan_time("Dev2/ctr0",**kwargs)
        task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE, samps_per_chan=pulse_count)

        task.start()

        task.wait_until_done(timeout = math.inf)





move('self',0.01, high_time = 0.001, low_time = 0.001)

#
#      shutter.stop()
#      shutter.close()
