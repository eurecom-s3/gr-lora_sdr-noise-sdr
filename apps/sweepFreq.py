"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class sweepFreq(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block"""
    def __init__(self, minFreq = 400e6, maxFreq = 2e9, stepFreq = 100e6, minOffset = 6e3, maxOffset = 10e3, stepOffset = 1e3):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__( self, name='Increase Frequency', in_sig=[], out_sig=[] )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.minFreq = minFreq;
        self.maxFreq = maxFreq;
        self.stepFreq = stepFreq;
        self.minOffset = minOffset;
        self.maxOffset = maxOffset;
        self.stepOffset = stepOffset;

        self.freq = self.minFreq
        self.offset = self.minOffset  

    def work(self, isOffset):
        if self.offset < self.maxOffset:
            if isOffset:
                self.offset += self.stepOffset
        else:
            if not isOffset:
                self.offset = self.minOffset
                if self.freq < self.maxFreq:
                    self.freq += self.stepFreq
                else:
                    self.freq = self.minFreq

        print isOffset, self.freq, self.offset

        if isOffset:
           return self.offset
        else:
           return self.freq
