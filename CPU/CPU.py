import math
import functools

class Registers:
    # region Register Structures
    def __init__(self,pc=0): #program counter
        self.reset(pc)

    def reset(self,pc=0):
        self.a = 0  # Accumulator
        self.x = 0  # General Purpose X
        self.y = 0  # General Purpose Y
        self.s = 0xff  # Stack Pointer
        self.pc = pc  # Program Counter
    


        self.flagBit = {
            'N': 128,  # N - Negative
            'V': 64,  # V - Overflow
            'B': 16,  # B - Break Command
            'D': 8,  # D - Decimal Mode
            'I': 4,  # I - IRQ Disable
            'Z': 2,  # Z - Zero
            'C': 1  # C - Carry
        }

        self.p = 0b00100100   # Flag Pointer - N|V|1|B|D|I|Z|C
    #endregion

    # region Status Register
    def getFlag(self, flag):
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
        )
    #endregion


class CPU:

    def __init__(self, mmu=None, pc=None, stack_page=0x1, magic=0xee):
        """
        Parameters
        ----------
        mmu: An instance of MMU
        pc: The starting address of the pc (program counter)
        stack_page: The index of the page which contains the stack.  The default for
            a 6502 is page 1 (the stack from 0x0100-0x1ff) but in some varients the
            stack page may be elsewhere.
        magic: A value needed for on of the illegal opcodes, XAA.  This value differs
            between different versions, even of the same CPU.  The default is 0xee.
        """
        self.mmu = mmu
        self.r = Registers()
        self.cc = 0 # cycle counter - licznik cykli
        # Which page the stack is in.  0x1 means that the stack is from
        # 0x100-0x1ff.  In the 6502 this is always true but it's different
        # for other 65* varients.
        self.stack_page = stack_page
        self.magic = magic
        self.reset()

        if pc:
            self.r.pc = pc
        else:
            # if pc is none get the address from $FFFD,$FFFC
            pass

        self._create_ops()

    def reset(self):
        self.r.reset()
        self.mmu.reset()

        self.running = True

    def step(self):
        self.cc = 0
        # pc = self.r.pc
        opcode = self.nextByte()
        self.ops[opcode]()

    def execute(self, instruction):
        """
        Execute a single instruction independent of the program in memory.
        instruction is an array of bytes.
        """
        pass

    def nextByte(self):
        v = self.mmu.read(self.r.pc)
        self.r.pc += 1
        return v

    def nextWord(self):
        low = self.nextByte()
        high = self.nextByte()
        return (high << 8) + low

    def stackPush(self, v):
        self.mmu.write(self.stack_page*0x100 + self.r.s, v)
        self.r.s = (self.r.s - 1) & 0xff

    def stackPushWord(self, v):
        self.stackPush(v >> 8)
        self.stackPush(v & 0xff)

    def stackPop(self):
        v = self.mmu.read(self.stack_page*0x100 + ((self.r.s + 1) & 0xff))
        self.r.s = (self.r.s + 1) & 0xff
        return v

    def stackPopWord(self):
        return self.stackPop() + (self.stackPop() << 8)

    def fromBCD(self, v):
        return (((v & 0xf0) // 0x10) * 10) + (v & 0xf)  # Binary-Coded Decimal, czyli zapis dziesiętny kodowany dwójkowo, kod dwójkowo-dziesiętny

    def toBCD(self, v):
        return int(math.floor(v/10))*16 + (v % 10) #Binary-Coded Decimal, czyli zapis dziesiętny kodowany dwójkowo, kod dwójkowo-dziesiętny

    def fromTwosCom(self, v): # Kod uzupełnień do dwóch
        return (v & 0x7f) - (v & 0x80)

    interrupts = {
        "ABORT":    0xfff8, #ekstra
        "COP":      0xfff4, #ekstra
        "BRK":      0xfffe, #ekstra
        "IRQ":      0xfffe,  # IRQ-L
        "NMI":      0xfffa, #NMI-L
        "RESET":    0xfffc #RESET-L
    }

    def interruptAddress(self, i):
        return self.mmu.readWord(self.interrupts[i])
