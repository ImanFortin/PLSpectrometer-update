import nidaqmx
from nidaqmx.constants import AcquisitionType

task = nidaqmx.Task()

task.do_channels.add_do_chan("Dev1/port0/line0")

task.timing.cfg_samp_clk_timing(1, sample_mode=AcquisitionType.FINITE, samps_per_chan=2)

task.write([True, False])



task.start()

task.wait_until_done()

task.stop()
