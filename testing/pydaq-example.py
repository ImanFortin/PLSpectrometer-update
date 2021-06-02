# coding= latin-1

from PyDAQmx.DAQmxFunctions import *
from PyDAQmx.DAQmxConstants import *
import time

class ContinuousPulseTrainGeneration():
    """ Class to create a continuous pulse train on a counter

    Usage:  pulse = ContinuousTrainGeneration(period [s],
                duty_cycle (default = 0.5), counter (default = "dev1/ctr0"),
                reset = True/False)
            pulse.start()
            pulse.stop()
            pulse.clear()
    """
    def __init__(self, period=1., duty_cycle=0.5, counter="Dev2/ctr0", reset=False):
        if reset:
            DAQmxResetDevice(counter.split('/')[0])
        taskHandle = TaskHandle(0)
        DAQmxCreateTask("",byref(taskHandle))
        DAQmxCreateCOPulseChanFreq(taskHandle,counter,"",DAQmx_Val_Hz,DAQmx_Val_Low,
                                                                   0.0,1/float(period),duty_cycle)
        DAQmxCfgImplicitTiming(taskHandle,DAQmx_Val_ContSamps,1000)
        self.taskHandle = taskHandle
    def start(self):
        DAQmxStartTask(self.taskHandle)
    def stop(self):
        DAQmxStopTask(self.taskHandle)
    def clear(self):
        DAQmxClearTask(self.taskHandle)


class ContinuousCounting():
    """ Class to create a continuous pulse train on a counter

    Usage:  pulse = ContinuousTrainGeneration(period [s],
                duty_cycle (default = 0.5), counter (default = "dev1/ctr0"),
                reset = True/False)
            pulse.start()
            pulse.stop()
            pulse.clear()
    """
    def __init__(self, period=1., duty_cycle=0.5, counter="Dev2/ctr0", reset=False):
        if reset:
            DAQmxResetDevice(counter.split('/')[0])
        taskHandle = TaskHandle(0)
        DAQmxCreateTask("",byref(taskHandle))
        DAQmxCreateCIPulseChanFreq(taskHandle,counter,"",0,10)
        DAQmxCfgImplicitTiming(taskHandle,DAQmx_Val_ContSamps,1000)
        self.taskHandle = taskHandle
    def start(self):
        DAQmxStartTask(self.taskHandle)
    def stop(self):
        DAQmxStopTask(self.taskHandle)
    def clear(self):
        DAQmxClearTask(self.taskHandle)


if __name__=="__main__":
    # pulse_gene1 = ContinuousPulseTrainGeneration(period = 1.,duty_cycle = 0.5, counter = "Dev2/ctr0", reset=True)
    # pulse_gene2 = ContinuousCounting(period = 1,)
    # pulse_gene1.start()
    # time.sleep(20)
    # pulse_gene1.stop()
    # pulse_gene1.clear()

    analogInTask = Task();

    myChannel = analogInTask.AIChannels.CreateVoltageChannel(
        "dev1/ai0", #The physical name of the channel
        "myChannel", #The name to associate with this channel
        AITerminalConfiguration.Differential, #idk
        -10, #min voltage
        10, #max voltage
        AIVoltageUnits.Volts)
