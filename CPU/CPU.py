# coding=utf-8
import numpy as np


# lista o długości 65,536‬ (każdy element ma wielkość 1B, w sumie 64kB)
pamiec = [0 for bit in range(256 * 256)]
# https://skilldrick.github.io/easy6502/#first-program
program = [0xa9, 0x01, 0x8d, 0x00, 0x02, 0xa9, 0x05, 0x8d,
           0x01, 0x02, 0xa9, 0x08, 0x8d, 0x02, 0x02]

# NEGATIVE, ZERO, CARRY, IRQ DISABLE, DECIMAL, OVERFLOW
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}

#ZROBIC FLAGI N i Z !!!
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
def LDA():
    global akumulator
    global pc
    akumulator = pamiec[pc+1]
    pc = pc + 2


def LDA_imm():
    pass
    global akumulator
    global pc_high
    akumulator = pc_high


# 3 bity, 1 bit to polecenie, drugi bit to numer strony, trzeci bit to numer indeksu, ich przemnozenie daje indeks tablicy pamieci
def LDA_abs():
    global akumulator
    global pc
    akumulator = pamiec[pc + 1]
    akumulator = akumulator * pamiec[pc + 2]
    pc = pc + 3


def LDA_zpg():
    pass


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
    pass


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
    pass


def LDY_abs_y():
    pass


def LDY_zpg_y():
    pass


# endregion LDY
# Wczytaj miejsce z danego miejsca w pamięci do zmiennej X
# def LDX(x=None, y=None):
#     global X
#     if x and y is not None:
#         X = pamiec[x][y]
#     elif x is not None:
#         X = pamiec[x][pc_low]
#     elif y is not None:
#         X = pamiec[pc_high][y]
#     else:
#         X = pamiec[pc_high][pc_low]
#     print('X: ', X)
#
#
# # Wczytaj miejsce z danego miejsca w pamięci do zmiennej Y
# def LDY(x=None, y=None):
#     global Y
#     if x and y is not None:
#         Y = pamiec[x][y]
#     elif x is not None:
#         Y = pamiec[x][pc_low]
#     elif y is not None:
#         Y = pamiec[pc_high][y]
#     else:
#         Y = pamiec[pc_high][pc_low]
#     print('Y: ', Y)


# endregion
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


def STY():
    global Y
    global pc
    pamiec[get_index()] = Y
    print('STY: ', hex(get_index()), '\n')
    pc = pc + 3


def STX():
    global X
    global pc
    pamiec[get_index()] = X
    print('STX: ', hex(get_index()), '\n')
    pc = pc + 3


# endregion
# region STX
# Zapisz z X do danego miejsca w pamięci do zmiennej
# def STX(x=None, y=None):
#     global X
#     if x and y is not None:
#         X = pamiec[x][y]
#     elif x is not None:
#         X = pamiec[x][pc_low]
#     elif y is not None:
#         X = pamiec[pc_high][y]
#     else:
#         pamiec[pc_high][pc_low] = X
#     X = 0
#     print('pamięć', pamiec[pc_high][pc_low], 'Wartość Y', X)


def STX_abs():
    pass


def STX_zpg():
    pass


def STX_zpg_y():
    pass


# endregion STX
# region STY
# Zapisz z Y do danego miejsca w pamięci do zmiennej
# def STY(x=None, y=None):
#     global Y
#     if x and y is not None:
#         Y = pamiec[x][y]
#     elif x is not None:
#         Y = pamiec[x][pc_low]
#     elif y is not None:
#         Y = pamiec[pc_high][y]
#     else:
#         pamiec[pc_high][pc_low] = Y
#     Y = 0
#     print('pamięć', pamiec[pc_high][pc_low], 'Wartość X', Y)


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
# endregion Flagi

# def ADC(x=None, y=None):
#     global akumulator
#     global flagi
#     global CarryValue
#     if x and y is not None:
#         akumulator = akumulator + pamiec[x][y] + flagi.get('C')
#     elif x is not None:
#         akumulator = akumulator + pamiec[x][pc_low] + flagi.get('C')
#     elif y is not None:
#         akumulator = akumulator + pamiec[pc_high][y] + flagi.get('C')
#     else:
#         akumulator = akumulator + pamiec[pc_high][pc_low] + flagi.get('C')
#
#     # Negative
#     if akumulator < 0:
#         flagi.update(N=1)
#     else:
#         flagi.update(N=0)
#
#     # Carry
#     if akumulator >= 255 and flagi.get('N') == 0:
#         flagi.update(C=1)
#         CarryValue = akumulator % 255
#         akumulator = 255
#
#     # Zero
#     if akumulator != 0:
#         flagi.update(Z=0)
#     else:
#         flagi.update(Z=1)
#
#     # Overflow
#     if akumulator > 127 and flagi.get('N') == 1:
#         akumulator = 127
#         flagi.update(V=1)
#     elif akumulator < -128 and flagi.get('N') == 1:
#         akumulator = -128
#         flagi.update(V=1)
#     else:
#         flagi.update(V=0)
#
#
# def SBC(x=None, y=None):
#     SEC()
#     global akumulator
#     if x and y is not None:
#         akumulator = akumulator - pamiec[x][y] - (255 - CarryValue)
#     elif x is not None:
#         akumulator = akumulator - pamiec[x][pc_low] - (255 - CarryValue)
#     elif y is not None:
#         akumulator = akumulator - pamiec[pc_high][y] - (255 - CarryValue)
#     else:
#         akumulator = akumulator - pamiec[pc_high][pc_low] - (255 - CarryValue)


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

# def INC():  # Inkrementacja  pamięci
#     global pamiec
#     global flagi
#     if flagi.get("Z") == 1:
#         pamiec[pc_high][pc_low] = (pamiec[pc_high][pc_low]) + 1
#     else:
#         pamiec[pc_high][pc_low] = pamiec[pc_high][pc_low]
#
#
# def DEC():  # Dekrementacja pamięci
#     global pamiec
#     global flagi
#     if flagi.get("N") == 1:
#         pamiec[pc_high][pc_low] = (pamiec[pc_high][pc_low]) - 1
#     else:
#         pamiec[pc_high][pc_low] = (pamiec[pc_high][pc_low])
#
#
# def AND():  # do sprawdzenia jeszcze; logic 1 = 1
#     global akumulator
#     global pamiec
#     if pamiec[pc_high][pc_low] == 1 and akumulator >= 0:
#         akumulator = 1
#         flagi.update(Z=0)
#         flagi.update(N=1)
#     else:
#         akumulator = 0
#         flagi.update(Z=1)
#         flagi.update(N=0)
#
#
# def ORA():
#     global akumulator
#     global pamiec
#     if pamiec[pc_high][pc_low] == 0 and akumulator <= 0:
#         akumulator = 0
#         flagi.update(Z=1)
#         flagi.update(N=0)
#     else:
#         akumulator = 1
#         flagi.update(Z=0)
#         flagi.update(N=1)
#
#
# def EOR():
#     global akumulator
#     global pamiec
#     if (pamiec[pc_high][pc_low] == 0 and akumulator) <= 0 or (pamiec[pc_high][pc_low] == 1 and akumulator >= 0):
#         akumulator = 0
#         flagi.update(Z=1)
#         flagi.update(N=0)
#     else:
#         akumulator = 1
#         flagi.update(Z=0)
#         flagi.update(N=1)

# endregion

# słownik rozkazów


rozkazy = {0xa9: LDA, 0x8d: STA, 0xea: NOP, 0x18: CLC, 0x38:SEC, 0x58: CLI, 0x78: SEI, 0xb8: CLV,
           0xd8: CLD, 0xf8: SED}




def main():
    global pamiec
    global pc

    load_program()
    while pamiec[pc] != 0:
        print('pc: ', pc, hex(pamiec[pc]), 'akumulator: ', akumulator, '\n')
        rozkazy[pamiec[pc]]()


if __name__ == '__main__':
    main()
