import nidaqmx
from nidaqmx.types import CtrTime
from nidaqmx.constants import AcquisitionType, Edge
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




with nidaqmx.Task() as task:
    task.ci_channels.add_ci_count_edges_chan("Dev2/ctr0")
    task.ci_channels[0].ci_count_edges_term = '/Dev2/PFI15'#set the terminal
    out = nidaqmx.Task()
    out.do_channels.add_do_chan("Dev2/port0/line4")


    task.start()#start counting
    out.write(True)
    out.write(False)
    out.write(True)
    out.write(False)
    out.write(True)
    out.write(False)
    out.write(True)
    out.write(False)
    print(task.read())
    out.stop()
    out.close()
