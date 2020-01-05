# coding=utf-8
import numpy as np


# lista o długości 65,536‬ (każdy element ma wielkość 1B, w sumie 64kB)
pamiec = [0 for bit in range(256 * 256)]
# https://skilldrick.github.io/easy6502/#first-program + ustawienie flagi I dla testów
#program = [0x78,0xa9, 0x05, 0x8d, 0x00, 0x02, 0xa9, 0x05, 0x8d,
 #          0x01, 0x02, 0xa9, 0x08, 0x8d, 0x02, 0x02]

program = [0xa9, 0x05,0xa9,0x08,0xea,0x50,0x600,0xa9,0x09,0xea]
#1536=0x600 tu jest test branchy

# NEGATIVE, ZERO, CARRY, IRQ DISABLE, DECIMAL, OVERFLOW
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}


# ZROBIC FLAGI N i Z !!!

akumulator = 0
X = 0
Y = 0
CarryValue = 0  # Zmienna przechowująca nadmiar liczby dodatniej

# program counter: przechowuje indeks czytanej komórki pamięci
pc = 1536
sp = 0 # stack pointer (niech bedzie taki na ten moment)

def get_index():
    return pamiec[pc+2]*0x100 + pamiec[pc+1]


def load_program():
    for i in range(len(program)):
        pamiec[1536+i] = program[i]

# region LDA,LDX, LDY
# region LDA


# Wczytaj miejsce z danego miejsca w pamięci do zmiennej Akumaltora
def LDA_imm():
    global akumulator
    global pc
    akumulator = pamiec[pc+1]
    pc = pc + 2


# 3 bity, 1 to polecenie, drugi to numer strony, trzeci to numer indeksu, ich przemnozenie daje indeks tablicy pamieci
def LDA_abs():
    global akumulator
    global pc
    akumulator = pamiec[pc + 1] # pierwsza liczba (Strona) do pomnozenia przez 256 (wielkosc strony)
    akumulator = akumulator * 256 + pamiec[pc + 2] # liczba stron + druga liczba (miejsce na stronie)
    pc = pc + 3




def LDA_zpg():
    global akumulator
    global pc
    akumulator = pamiec[pc + 1] # adres do pobrania
    akumulator = pamiec[akumulator]
    pc = pc + 2


def LDA_abs_x():
    global akumulator
    global X
    global pc
    akumulator = pamiec[pc + 1]
    akumulator = akumulator * 256 + pamiec[pc + 2] + X
    pc = pc + 3


def LDA_abs_y():
    global akumulator
    global Y
    global pc
    akumulator = pamiec[pc + 1]
    akumulator = akumulator * 256 + pamiec[pc + 2] + Y
    pc = pc + 3


def LDA_zpg_x():
    pass


# Metody oznaczone nawiasami na wiekszej liczbie cykli
def LDA_zpg2_y():
    pass


def LDA_zpg2_x():
    pass


# endregion LDA
# region LDX
def LDX_imm():
    global X
    global pc
    X = pamiec[pc + 1]
    pc = pc + 2


def LDX_abs():
    global X
    global pc
    X = pamiec[pc + 1]
    X = X * 256 + pamiec[pc + 2]
    pc = pc + 3


def LDX_zpg():
    global X
    global pc
    X = pamiec[pc + 1]  # adres do pobrania
    X = pamiec[akumulator]
    pc = pc + 2


def LDX_abs_y():
    global X
    global pc
    global Y
    X = pamiec[pc + 1]
    X = X * 256 + pamiec[pc + 2] + Y
    pc = pc + 3


def LDX_zpg_y():
    pass


# endregion LDX
# region LDY
def LDY_imm():
    global Y
    global pc
    Y = pamiec[pc + 1]
    pc = pc + 2


def LDY_abs():
    global Y
    global pc
    Y = pamiec[pc + 1]
    Y = akumulator * 256 + pamiec[pc + 2]
    pc = pc + 3


def LDY_zpg():
    global Y
    global pc
    Y = pamiec[pc + 1]  # adres do pobrania
    Y = pamiec[akumulator]
    pc = pc + 2


def LDY_abs_x():
    global Y
    global pc
    global X
    Y = pamiec[pc + 1]
    Y = akumulator * 256 + pamiec[pc + 2] + X
    pc = pc + 3


def LDY_zpg_y():
    pass
# endregion LDY
# endregion

# region STA, STX, STY


def STA_abs():
    pass


def STA_zpg():
    pass


def STA_abs_x():
    pass


def STA_abs_y():
    pass


def STA_zpg_x():
    pass


# Metody oznaczone nawiasami na wiekszej liczbie cykli
def STA_zpg2_y():
    pass


def STA_zpg2_x():
    pass


# Zapisz z Akumaltora do danego miejsca w pamięci
def STA():
    global akumulator
    global pc
    pamiec[get_index()] = akumulator
    print('STA: ', hex(get_index()), '\n')
    pc = pc + 3


# Zapisz z Y do danego miejsca w pamięci
def STY():
    global Y
    global pc
    pamiec[get_index()] = Y
    print('STY: ', hex(get_index()), '\n')
    pc = pc + 3


# Zapisz z X do danego miejsca w pamięci
def STX():
    global X
    global pc
    pamiec[get_index()] = X
    print('STX: ', hex(get_index()), '\n')
    pc = pc + 3


def STX_abs():
    pass


def STX_zpg():
    pass


def STX_zpg_y():
    pass


def STY_abs():
    pass


def STY_zpg():
    pass


def STY_zpg_x():
    pass


# endregion

# region metody Flag & NOP


def NOP():
    global pc
    pc = pc +1


def CLC():  # zerowanie C
    global flagi
    global pc
    flagi.update(C=0)
    pc = pc + 1


def CLD():  # zerowanie D
    global flagi
    global pc
    flagi.update(D=0)
    pc = pc + 1


def CLI():  # zerowanie I
    global flagi
    global pc
    flagi.update(I=0)
    pc = pc + 1


def CLV():  # zerowanie V
    global flagi
    global pc
    flagi.update(V=0)
    pc = pc + 1


def SED():  # jedynkowanie D
    global flagi
    global pc
    flagi.update(D=1)
    pc = pc + 1


def SEC():  # jedynkowanie C
    global flagi
    global pc
    flagi.update(C=1)
    pc = pc + 1


def SEI():  # jedynkowanie I
    global flagi
    global pc
    flagi.update(I=1)
    pc = pc + 1

# endregion

# region Inkremenetacja / Dekrementacja


def DEX():  # Dekrementacja X
    global X
    global pc
    X = X - 1
    if X < 0:
        flagi.update(N=1)
    elif X == 0:
        flagi.update(Z=1)
    pc = pc + 1


def DEY():  # Dekrementacja Y
    global Y
    global pc
    Y = Y - 1
    if Y < 0:
        flagi.update(N=1)
    elif Y == 0:
        flagi.update(Z=1)
    pc = pc + 1


def INX():  # Inkrementacja X
    global X
    global pc
    X = X + 1
    if X < 0:
        flagi.update(N=1)
    elif X == 0:
        flagi.update(Z=1)
    pc = pc + 1


def INY():  # Inkrementacja Y
    global Y
    global pc
    Y = Y + 1
    if Y < 0:
        flagi.update(N=1)
    elif Y == 0:
        flagi.update(Z=1)
    pc = pc + 1
# endregion

# region TAX, TXA, TAY, TYA


def TAX():  # Transfer z A do X
    global X
    global akumulator
    global pc
    X = akumulator
    if X < 0:
        flagi.update(N=1)
    elif X == 0:
        flagi.update(Z=1)
    pc = pc + 1


def TXA():  # Transfer z X do A
    global X
    global akumulator
    global pc
    akumulator = X
    if X < 0:
        flagi.update(N=1)
    elif X == 0:
        flagi.update(Z=1)
    pc = pc + 1


def TYA():  # Transfer z Y do A
    global Y
    global akumulator
    global pc
    akumulator = Y
    if Y < 0:
        flagi.update(N=1)
    elif Y == 0:
        flagi.update(Z=1)
    pc = pc + 1


def TAY():  # Transfer z A do Y
    global Y
    global akumulator
    global pc
    Y = akumulator
    if Y < 0:
        flagi.update(N=1)
    elif Y == 0:
        flagi.update(Z=1)
    pc = pc + 1

# endregion

# region Branche & JUMP

def JMP_abs():  # skok jeśli V=0
    global pc
    global flagi
    pc = pamiec[pc + 1]


def BCS():  # skok jeśli C=1
    global pc
    global flagi
    if flagi.get('C') == 1:
        pc = pamiec[pc + 1]
    else:
        pc = pc+2


def BCC():  # skok jeśli C=0
    global pc
    global flagi
    if flagi.get('C') == 0:
        pc = pamiec[pc + 1]
    else:
        pc = pc + 2


def BEQ():  # skok jeśli Z=1
    global pc
    global flagi
    if flagi.get('Z') == 1:
        pc = pamiec[pc + 1]
    else:
        pc = pc + 2


def BNE():  # skok jeśli Z=0
    global pc
    global flagi
    if flagi.get('Z') == 0:
        pc = pamiec[pc + 1]
    else:
        pc = pc + 2


def BMI():  # skok jeśli N=1
    global pc
    global flagi
    if flagi.get('N') == 1:
        pc = pamiec[pc + 1]
    else:
        pc = pc + 2


def BPL():  # skok jeśli N=0
    global pc
    global flagi
    if flagi.get('N') == 0:
        pc = pamiec[pc + 1]
    else:
        pc = pc + 2


def BVS():  # skok jeśli V=1
    global pc
    global flagi
    if flagi.get('V') == 1:
        pc = pamiec[pc + 1]
    else:
        pc = pc + 2


def BVC():  # skok jeśli V=0
    global pc
    global flagi
    if flagi.get('V') == 0:
        pc = pamiec[pc + 1]
    else:
        pc = pc + 2
# endregion

#region STOS
def TXS():
    global X
    global sp
    if X == 0:
        sp = sp
    else:
        sp = sp + X


def TSX():
    global X
    global sp
    if sp == 0:
        X = X
    else:
        X = X + sp
        sp = sp - 1


def PHA():
    global akumulator
    global sp
    if akumulator == 0:
        sp = sp
    else:
        sp = sp + akumulator
        sp = sp - 1

def PHP():
    global flagi
    global sp
    sp = sp + flagi.get("N") + flagi.get("Z")


def PLA():
    global akumulator
    global sp
    if akumulator == 0:
        sp = sp
    else:
        sp = sp - akumulator


def PLP():
    global flagi
    global sp
    sp = sp - flagi.get("N") - flagi.get("V") - flagi.get("B") - flagi.get("D") - flagi.get("I") - flagi.get("Z")
    - flagi.get("C")


#endregion
# słownik rozkazów

# tutaj trzeba posprawdzac z plikiem Kamila i dodac (None)
rozkazy = {0xa9: LDA_imm, 0x8d: STA, 0xea: NOP, 0x18: CLC, 0x38:SEC, 0x58: CLI, 0x78: SEI, 0xb8: CLV,
           0xd8: CLD, 0xf8: SED,0x10: BPL,0x30: BMI,0x50: BVC,0x70: BVS,0x90: BCC,0xb0: BCS,0xd0: BNE,0xf0: BEQ,
           0x4c: JMP_abs,0xaa: TAX, 0x8a: TXA,0xca: DEX,0xe8: INX,0xa8: TAY, 0x98:TYA,0x88: DEY,0xc8: INY,0x9a:TXS,
           0xba: TSX, 0x48: PHA,0x08: PHP,0x68: PLA, 0x28: PLP}


def main():
    global pamiec
    global pc

    load_program()
    while pamiec[pc] != 0:
        print('pc=', pc, hex(pamiec[pc]), 'akumulator=', akumulator, '\n'
              'X=', X,'Y=', Y, flagi,'\n')
        rozkazy[pamiec[pc]]()


if __name__ == '__main__':
    main()