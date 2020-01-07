# coding=utf-8
import numpy as np


# lista o długości 65,536‬ (każdy element ma wielkość 1B, w sumie 64kB)
pamiec = [0 for bit in range(256 * 256)]
# https://skilldrick.github.io/easy6502/#first-program + ustawienie flagi I dla testów
program = [0x78,0xa9, 0x05, 0x8d, 0x00, 0x02, 0xa9, 0x05, 0x8d,
          0x01, 0x02, 0xa9, 0x08, 0x8d, 0x02, 0x02]

#program = [0xa9, 0x05,0xa9,0x08,0xea,0x50,0x600,0xa9,0x09,0xea]
#1536=0x600 tu jest test branchy

# NEGATIVE, ZERO, CARRY, IRQ DISABLE, DECIMAL, OVERFLOW
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}
sp=0

# ZROBIC FLAGI N i Z !!!

akumulator = 0
X = 0
Y = 0
CarryValue = 0  # Zmienna przechowująca nadmiar liczby dodatniej

# program counter: przechowuje indeks czytanej komórki pamięci
pc = 1536


def get_index_abs(): # zczytuje 2 liczby jako index listy pamiec.
    return pamiec[pc+2]*256 + pamiec[pc+1]


def get_index_abs_x(): # zczytuje 2 liczby jako index listy pamiec + x.
    return pamiec[pc+2]*256 + pamiec[pc+1] + x


def get_index_abs_y(): # zczytuje 2 liczby jako index listy pamiec + x.
    return pamiec[pc+2]*256 + pamiec[pc+1] + y


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
    akumulator = pamiec[pc + 2] # druga liczba (Strona) do pomnozenia przez 256 (wielkosc strony)
    akumulator = akumulator * 256 + pamiec[pc + 1] # liczba stron + pierwsza liczba (miejsce na stronie)
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
    akumulator = pamiec[pc + 2]
    akumulator = akumulator * 256 + pamiec[pc + 1] + X
    pc = pc + 3


def LDA_abs_y():
    global akumulator
    global Y
    global pc
    akumulator = pamiec[pc + 2]
    akumulator = akumulator * 256 + pamiec[pc + 1] + Y
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
    X = pamiec[pc + 2]
    X = X * 256 + pamiec[pc + 1]
    pc = pc + 3


def LDX_zpg():
    global X
    global pc
    X = pamiec[pc + 1]  # adres do pobrania
    X = pamiec[X]
    pc = pc + 2


def LDX_abs_y():
    global X
    global pc
    global Y
    X = pamiec[pc + 2]
    X = X * 256 + pamiec[pc + 1] + Y
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
    Y = pamiec[pc + 2]
    Y = Y * 256 + pamiec[pc + 1]
    pc = pc + 3


def LDY_zpg():
    global Y
    global pc
    Y = pamiec[pc + 1]  # adres do pobrania
    Y = pamiec[Y]
    pc = pc + 2


def LDY_abs_x():
    global Y
    global pc
    global X
    Y = pamiec[pc + 2]
    Y = Y * 256 + pamiec[pc + 1] + X
    pc = pc + 3


def LDY_zpg_y():
    pass
# endregion LDY
# endregion

# region STA, STX, STY
# region STA


def STA_abs():
    global akumulator
    global pc
    pamiec[get_index()] = akumulator
    pc = pc + 3


def STA_zpg():
    global akumulator
    global pc
    pamiec[pc + 1] = akumulator
    pc = pc + 2


def STA_abs_x():
    global akumulator
    global X
    global pc
    pamiec[get_index()] = akumulator + X
    pc = pc + 3


def STA_abs_y():
    global akumulator
    global X
    global pc
    pamiec[get_index()] = akumulator + X
    pc = pc + 3


def STA_zpg_x():
    pass


# Metody oznaczone nawiasami na wiekszej liczbie cykli
def STA_zpg2_y():
    pass


def STA_zpg2_x():
    pass

# endregion
# region STX
def STX_abs():
    global X
    global pc
    pamiec[get_index()] = X
    pc = pc + 3


def STX_zpg():
    global X
    global pc
    pamiec[pc + 1] = X
    pc = pc + 2


def STX_zpg_y():
    pass

# endregion
# region STY
def STY_abs():
    global Y
    global pc
    pamiec[get_index()] = Y
    pc = pc + 3


def STY_zpg():
    global Y
    global pc
    pamiec[pc + 1] = Y
    pc = pc + 2


def STY_zpg_x():
    pass

# endregion
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


def INC_zpg(): # Inkrementacja pamięci
    global pc
    global pamiec
    global indeks
    indeks = pamiec[pc+1]
    pamiec[indeks]=pamiec[indeks]+1   # lub coś innego zamiast jedynki
    if pamiec[indeks] < 0: # chyba tak
        flagi.update(N=1)
    elif pamiec[indeks] == 0:
        flagi.update(Z=1)
    pc = pc + 2



def DEC_zpg(): # Dekrementacja pamięci
    global pc
    global pamiec
    global indeks
    indeks = pamiec[pc+1]
    pamiec[indeks]=pamiec[indeks]-1  # lub coś innego zamiast jedynki
    if pamiec[indeks] < 0: # chyba tak
        flagi.update(N=1)
    elif pamiec[indeks] == 0:
        flagi.update(Z=1)
    pc = pc + 2



def INC_abs(): # Inkrementacja pamięci
    global pc
    global pamiec
    global indeks
    indeks = pamiec[pc + 2]
    indeks = indeks * 256 + pamiec[pc + 1]
    pamiec[indeks] = pamiec[indeks] + 1  # lub coś innego zamiast jedynki
    pc = pc + 3
    if pamiec[indeks] < 0: # chyba tak
        flagi.update(N=1)
    elif pamiec[indeks] == 0:
        flagi.update(Z=1)



def DEC_abs(): # Dekrementacja pamięci
    global pc
    global pamiec
    global indeks
    indeks = pamiec[pc + 2]
    indeks = indeks * 256 + pamiec[pc + 1]
    pamiec[indeks]=pamiec[indeks] - 1  # lub coś innego zamiast jedynki
    pc = pc + 3
    if pamiec[indeks] < 0: # chyba tak
        flagi.update(N=1)
    elif pamiec[indeks] == 0:
        flagi.update(Z=1)


def INC_abs_x(): # Inkrementacja pamięci
    global pc
    global pamiec
    global indeks
    indeks = pamiec[pc + 2]
    indeks = indeks * 256 + pamiec[pc + 1] + X
    pamiec[indeks] = pamiec[indeks] + 1  # lub coś innego zamiast jedynki
    pc = pc + 3
    if pamiec[indeks] < 0: # chyba tak
        flagi.update(N=1)
    elif pamiec[indeks] == 0:
        flagi.update(Z=1)


def DEC_abs_x(): # Dekrementacja pamięci
    global pc
    global pamiec
    global indeks
    indeks = pamiec[pc + 2]
    indeks = indeks * 256 + pamiec[pc + 1] + X
    pamiec[indeks]=pamiec[indeks] - 1   # lub coś innego zamiast jedynki
    pc = pc + 3
    if pamiec[indeks] < 0: # chyba tak
        flagi.update(N=1)
    elif pamiec[indeks] == 0:
        flagi.update(Z=1)


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

# region Dodawanie z przenoszeniem


def ADC_imm():
    global akumulator
    global flagi
    global pc

    akumulator = akumulator + pamiec[pc + 1] + flagi.get('C')
    pc = pc + 2


    # Negative
    if akumulator < 0:
        flagi.update(N=1)
    else:
        flagi.update(N=0)

    # Carry

    if akumulator >= 255 and flagi.get('C') == 0:
        flagi.update(C=1)
        akumulator = 255
    else:
        flagi.update(C=0)

    # Zero

    if akumulator != 0:
        flagi.update(Z=0)
    else:
        flagi.update(Z=1)

    # Overflow
    if akumulator >= 127:
        akumulator = 127
        flagi.update(V=1)

    elif akumulator < -128:
        akumulator = -128
        flagi.update(V=1)
    else:
        flagi.update(V=0)


def ADC_abs():
    global akumulator
    global flagi
    global pc

    akumulator = akumulator + pamiec[get_index_abs()] + flagi.get('C')
    pc = pc + 3

    # Negative
    if akumulator < 0:
        flagi.update(N=1)
    else:
        flagi.update(N=0)

    # Carry

    if akumulator >= 255 and flagi.get('C') == 0:
        flagi.update(C=1)
        akumulator = 255
    else:
        flagi.update(C=0)

    # Zero

    if akumulator != 0:
        flagi.update(Z=0)
    else:
        flagi.update(Z=1)

    # Overflow
    if akumulator >= 127:
        akumulator = 127
        flagi.update(V=1)

    elif akumulator < -128:
        akumulator = -128
        flagi.update(V=1)
    else:
        flagi.update(V=0)


def ADC_zpg():
    global akumulator
    global flagi
    global pc

    akumulator = akumulator + pamiec[pamiec[pc+1]] + flagi.get('C')
    pc = pc + 2

    # Negative
    if akumulator < 0:
        flagi.update(N=1)
    else:
        flagi.update(N=0)

    # Carry

    if akumulator >= 255 and flagi.get('C') == 0:
        flagi.update(C=1)
        akumulator = 255
    else:
        flagi.update(C=0)

    # Zero

    if akumulator != 0:
        flagi.update(Z=0)
    else:
        flagi.update(Z=1)

    # Overflow
    if akumulator >= 127:
        akumulator = 127
        flagi.update(V=1)

    elif akumulator < -128:
        akumulator = -128
        flagi.update(V=1)
    else:
        flagi.update(V=0)


def ADC_abs_x():
    global akumulator
    global flagi
    global pc

    akumulator = akumulator + pamiec[get_index_abs_x()] + flagi.get('C')
    pc = pc + 3

    # Negative
    if akumulator < 0:
        flagi.update(N=1)
    else:
        flagi.update(N=0)

    # Carry

    if akumulator >= 255 and flagi.get('C') == 0:
        flagi.update(C=1)
        akumulator = 255
    else:
        flagi.update(C=0)

    # Zero

    if akumulator != 0:
        flagi.update(Z=0)
    else:
        flagi.update(Z=1)

    # Overflow
    if akumulator >= 127:
        akumulator = 127
        flagi.update(V=1)

    elif akumulator < -128:
        akumulator = -128
        flagi.update(V=1)
    else:
        flagi.update(V=0)


def ADC_abs_y():
    global akumulator
    global flagi
    global pc

    akumulator = akumulator + pamiec[get_index_abs_y()] + flagi.get('C')
    pc = pc + 3

    # Negative
    if akumulator < 0:
        flagi.update(N=1)
    else:
        flagi.update(N=0)

    # Carry

    if akumulator >= 255 and flagi.get('C') == 0:
        flagi.update(C=1)
        akumulator = 255
    else:
        flagi.update(C=0)

    # Zero

    if akumulator != 0:
        flagi.update(Z=0)
    else:
        flagi.update(Z=1)

    # Overflow
    if akumulator >= 127:
        akumulator = 127
        flagi.update(V=1)

    elif akumulator < -128:
        akumulator = -128
        flagi.update(V=1)
    else:
        flagi.update(V=0)


def ADC_zpg_x():
    global akumulator
    global flagi
    global pc

    akumulator = akumulator + pamiec[pamiec[pc + 1] + x] + flagi.get('C')
    pc = pc + 2

    # Negative
    if akumulator < 0:
        flagi.update(N=1)
    else:
        flagi.update(N=0)

    # Carry

    if akumulator >= 255:
        flagi.update(C=1)
        akumulator = 255
    else:
        flagi.update(C=0)

    # Zero

    if akumulator != 0:
        flagi.update(Z=0)
    else:
        flagi.update(Z=1)

    # Overflow
    if akumulator >= 127:
        akumulator = 127
        flagi.update(V=1)

    elif akumulator < -128:
        akumulator = -128
        flagi.update(V=1)
    else:
        flagi.update(V=0)


# Metody oznaczone nawiasami na wiekszej liczbie cykli


def ADC_zpg2_x():
    pass


def ADC_zpg2_y():
    pass

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

# region Porównania


def CMP_imm(): # porównuje wartosc do akumulatora
    global pc
    global akumulator
    global pamiec
    global a
    a = pamiec[pc + 1]
    if akumulator > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif akumulator == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif akumulator < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 2


def CMP_zpg(): # porównuje wartosc w pamieci do akumulatora
    global pc
    global akumulator
    global pamiec
    global a
    a = pamiec[pc + 1]  # adres do pobrania
    a = pamiec[a]
    if akumulator > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif akumulator == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif akumulator < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 2


def CMP_abs(): # porównuje wartosc w pamieci do akumulatora
    global pc
    global akumulator
    global pamiec
    global a
    a = pamiec[pc + 2]
    a = a * 256 + pamiec[pc + 1]
    if akumulator > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif akumulator == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif akumulator < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 3


def CMP_abs_x(): # porównuje wartosc w pamieci do akumulatora
    global pc
    global akumulator
    global pamiec
    global a
    a = pamiec[pc + 2]
    a = a * 256 + pamiec[pc + 1] + X
    if akumulator > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif akumulator == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif akumulator < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 3


def CMP_abs_y(): # porównuje wartosc w pamieci do akumulatora
    global pc
    global akumulator
    global pamiec
    global a
    a = pamiec[pc + 2]
    a = a * 256 + pamiec[pc + 1] + Y
    if akumulator > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif akumulator == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif akumulator < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 3


def CPX_imm(): # porównuje wartosc do X
    global pc
    global X
    global pamiec
    global a
    a = pamiec[pc + 1]
    if X > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif X == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif X < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 2


def CPX_zpg(): # porównuje wartosc do X
    global pc
    global X
    global pamiec
    global a
    a = pamiec[pc + 1]  # adres do pobrania
    a = pamiec[a]
    if X > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif X == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif X < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 2


def CPX_abs(): # porównuje wartosc do X
    global pc
    global X
    global pamiec
    global a
    a = pamiec[pc + 2]
    a = a * 256 + pamiec[pc + 1]
    if X > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif X == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif X < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 3


def CPY_imm(): # porównuje wartosc do Y
    global pc
    global Y
    global pamiec
    global a
    a = pamiec[pc + 1]
    if Y > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif Y == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif Y < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 2


def CPY_zpg(): # porównuje wartosc do Y
    global pc
    global Y
    global pamiec
    global a
    a = pamiec[pc + 1]
    a = pamiec[a]
    if Y > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif Y == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif Y < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 2


def CPY_abs(): # porównuje wartosc do Y
    global pc
    global Y
    global pamiec
    global a
    a = pamiec[pc + 2]
    a = a * 256 + pamiec[pc + 1]
    if Y > a:
        flagi.update("C",1)
        flagi.update("Z", 0)
        flagi.update("N", 0)
    elif Y == a:
        flagi.update("C", 1)
        flagi.update("Z", 1)
        flagi.update("N", 0)
    elif Y < a:
        flagi.update("C", 0)
        flagi.update("Z", 0)
        flagi.update("N", 1)
    pc = pc + 3




# endregion

# region STOS


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


# endregion


def BRK():
    global pc
    pc = pc+1


# słownik rozkazów

# tutaj trzeba posprawdzac z plikiem Kamila i dodac (None)


rozkazy = {0xa9: LDA_imm, 0x8d: STA_abs, 0xea: NOP, 0x18: CLC, 0x38:SEC, 0x58: CLI, 0x78: SEI, 0xb8: CLV,
           0xd8: CLD, 0xf8: SED,0x10: BPL,0x30: BMI,0x50: BVC,0x70: BVS,0x90: BCC,0xb0: BCS,0xd0: BNE,0xf0: BEQ,
           0x4c: JMP_abs,0xaa: TAX, 0x8a: TXA,0xca: DEX,0xe8: INX,0xa8: TAY, 0x98:TYA,0x88: DEY,0xc8: INY,0x00: BRK,
           0xe6: INC_zpg, 0xee: INC_abs, 0xc6: DEC_zpg, 0xce: DEC_abs, 0xfe: INC_abs_x, 0xde: DEC_abs_x}


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
