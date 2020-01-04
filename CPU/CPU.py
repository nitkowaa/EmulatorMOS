# coding=utf-8
import numpy as np


# lista o długości 65,536‬ (każdy element ma wielkość 1B, w sumie 64kB)
pamiec = [0 for bit in range(256 * 256)]
# https://skilldrick.github.io/easy6502/#first-program + ustawienie flagi I dla testów
program = [0x78,0xa9, 0x05, 0x8d, 0x00, 0x02, 0xa9, 0x05, 0x8d,
           0x01, 0x02, 0xa9, 0x08, 0x8d, 0x02, 0x02]

# NEGATIVE, ZERO, CARRY, IRQ DISABLE, DECIMAL, OVERFLOW
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}


# ZROBIC FLAGI N i Z !!!

akumulator = 0
X = 0
Y = 0
CarryValue = 0  # Zmienna przechowująca nadmiar liczby dodatniej

# program counter: przechowuje indeks czytanej komórki pamięci
pc = 1536


def get_index():
    return pamiec[pc+2]*0x100 + pamiec[pc+1]


def load_program():
    for i in range(len(program)):
        pamiec[1536+i] = program[i]


# region Metody Load


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
    akumulator = pamiec[pc + 1]
    akumulator = akumulator * pamiec[pc + 2]
    pc = pc + 3


def BCS_rel(label):  # skok jeśli C=1
    global pc
    global flagi
    if flagi.get('C') == 1:
        pc = pamiec[pc+1]
    else:
        pc = pc+2



def LDA_zpg():
    global akumulator
    global pc
    akumulator = pamiec[pc + 1] # adres do pobrania
    akumulator = pamiec[akumulator]
    pc = pc + 2


def LDA_abs_x():
    pass


def LDA_abs_y():
    pass


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
    X = X * pamiec[pc + 2]
    pc = pc + 3


def LDX_zpg():
    global X
    global pc
    X = pamiec[pc + 1]  # adres do pobrania
    X = pamiec[akumulator]
    pc = pc + 2


def LDX_abs_y():
    pass


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
    Y = akumulator * pamiec[pc + 2]
    pc = pc + 3


def LDY_zpg():
    global Y
    global pc
    Y = pamiec[pc + 1]  # adres do pobrania
    Y = pamiec[akumulator]
    pc = pc + 2


def LDY_abs_y():
    pass


def LDY_zpg_y():
    pass
# endregion LDY

# region Metody Store
# region STA


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
# endregion

# region Flagi
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

def NOP():
    global pc
    pc = pc +1


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


# metody branchowe wczytują etykiety
def BCS():  # skok jeśli C=1
    global pc
    global flagi
    if flagi.get('C') == 1:
        pc = pamiec[pc + 1] # to trzeba sprawdzić we wszystkich branchach
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
# endregion branch

# słownik rozkazów


rozkazy = {0xa9: LDA_imm, 0x8d: STA, 0xea: NOP, 0x18: CLC, 0x38:SEC, 0x58: CLI, 0x78: SEI, 0xb8: CLV,
           0xd8: CLD, 0xf8: SED, BPL: 0x10,BMI: 0x30, BVC: 0x50, BVS: 0x70, BCC: 0x90, BCS: 0xb0, BNE: 0xd0, BEQ: 0xf0}


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
