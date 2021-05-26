import nidaqmx
import numpy as np
from nidaqmx import *

test_Task = nidaqmx.Task()
test_Task.ao_channels.add_ao_voltage_chan('Dev1/ao1')
test_Task.timing.cfg_samp_clk_timing(rate= 10, sample_mode= nidaqmx.constants.AcquisitionType.CONTINUOUS, samps_per_chan= 5)
test_Writer = nidaqmx.stream_writers.AnalogSingleChannelWriter(test_Task.out_stream, auto_start=True)
samples = np.append(5*np.ones(10), np.zeros(10))
test_Writer.write_many_sample(samples)
test_Task.wait_until_done(timeout=100)
