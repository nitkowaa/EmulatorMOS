import math
import functools

class Registers: #Obiekt do przechowywania rejsterów CPU"
    def __init__(self,pc=0): #program counter
        self.reset(pc)
    def reset(self,pc=0):
        self.a = 0  # Accumulator
        self.x = 0  # General Purpose X
        self.y = 0  # General Purpose Y
        self.s = 0xff  # Stack Pointer
        self.pc = pc  # Program Counter

        # region Związane z flagami, narazie zbędne(?)
        '''self.flagBit = {
            'N': 128,  # N - Negative
            'V': 64,  # V - Overflow
            'B': 16,  # B - Break Command
            'D': 8,  # D - Decimal Mode
            'I': 4,  # I - IRQ Disable
            'Z': 2,  # Z - Zero
            'C': 1  # C - Carry
        }

        self.p = 0b00100100 '''  # Flag Pointer - N|V|1|B|D|I|Z|C
        #endregion

    # region Metody związane z flagami, narazie zbędne(?)
    '''def getFlag(self, flag):
        return bool(self.p & self.flagBit[flag])

    def setFlag(self, flag, v=True):
        if v:
            self.p = self.p | self.flagBit[flag]
        else:
            self.clearFlag(flag)

    def clearFlag(self, flag):
        self.p = self.p & (255 - self.flagBit[flag])

    def clearFlags(self):
        self.p = 0

    def ZN(self, v):
        """
        The criteria for Z and N flags are standard.  Z gets set if the
        value is zero and N gets set to the same value as bit 7 of the value.
        """
        self.setFlag('Z', v == 0)
        self.setFlag('N', v & 0x80)

    def __repr__(self):
        return "A: %02x X: %02x Y: %02x S: %02x PC: %04x P: %s" % (
            self.a, self.x, self.y, self.s, self.pc, bin(self.p)[2:].zfill(8)
        ) ''' # Znowu do flag
    #endregion