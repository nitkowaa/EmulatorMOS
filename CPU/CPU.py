import numpy as np

pamiec = np.random.randint(2, size=(8, 8))  # Two-dimensional array
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}

#Zapis MSD\LSD 13 strona w pdfie
Rozkazy = \
    {
        "00": BRK(None), "01": ORA_indX(), "05": ORA_zpg(), "06": ASL_zpg(None), "08": PHP(None), "09": ORA_imm(), "0A": ASLA(None), "0D": ORA_abs(), "0E": ASL_abs(None),
        "10": BPL_rel(None), "11": ORA_indY(), "15": ORA_zpgX(), "16": ASL_zpgX(None), "18": CLC(), "19": ORA_absY(), "1D": ORA_absX(), "1E": ASL_absX(None),
        "20": JSR_abs(None), "21": AND_indX(), "24": BIT_zpg(None), "25": AND_zpg(), "26": ROL_zpg(None), "28": PLP(None), "2A": ROLA(None), "2C": BIT_abs(None),"2D": AND_abs(), "2E": ROL_abs(None),
        "30": BMI_rel(None), "31": AND_indY(), "35": AND_zpgX(), "36": ROL_zpgX(None), "38": SEC(), "39": AND_absY(), "3D": And_absX(), "3E": ROL_absX(None),
        "40": RTI(None), "41": EOR_indX(), "45": EOR_zpg(), "46": LSR_zpg(None), "48": PHA(None), "49": EOR_imm(), "4A": LSRA(None), "4C": JMP_abs(None), "4D": EOR_abs(), "4E": LSR_abs(None),
        "50": BVC_rel(None), "51": EOR_indY(), "55": EOR_zpgX(), "56": LSR_zpgX(None), "58": CLI(), "59": EOR_absY(), "5D": EOR_absX(), "5E": LSR_absX(None),
        "60": RTS(None), "61": ADC_indX(), "65": ADC_zpg(), "66": ROR_zpg(None), "68": PLA(None), "69": ADC_imm(), "6A": RORA(None), "6C": JMP_ind(None), "6D": ADC_abs(), "6E": ROR_abs(None),
        "70": BVS_rel(None), "71": ADC_indY(), "75": ADC_zpgX(), "76": ROR_zpgX(None), "78": SEI(), "79": ADC_absY(), "7D": ADC_absX(), "7E": ROR_absX(None),
        "81": STA_indX(), "84": STY_zpg(), "85": STA_zpg(), "86": STX_zpg(), "88": DEY(), "8A": TXA(None), "8C": STY_abs(), "8D": STA_abs() , "8E": STX_abs(),
        "90": BCC_rel(None), "91": STA_indX(), "94": STY_zpgX(), "95": STA_zpgX(), "96": STX_zpgY(), "98": TYA(), "99": STA_absY(), "9A": TXS(None), "9D": STA_absX(),
        "A0": LDY_imm(), "A1": LDA_indX(), "A2": LDX_imm(), "A4": LDY_zpg(), "A5": LDA_zpg(), "A6": LDX_zpg(), "A8": TAY(None), "A9": LDA_imm(), "AA": TAX(None), "AC": LDY_absX(), "AD": LDA_absX(), "AE": LDX_absY(),
        "B0": BCS_rel(None), "B1": LDA_indY(), "B4": LDY_zpgX(), "B5": LDA_zpgX(), "B6": LDX_zpgY(), "B8": CLV(), "B9": LDA_absY(), "BA": TSX(None), "BC": LDY_absX(), "BD": LDA_absX(), "BE": LDX_absY(),
        "C0": CPY_imm(None), "C1": CMP_indX(None), "C4": CPY_zpg(None), "C5": CMP_zpg(None), "C6": DEC_zpg(), "C8": INY(), "C9": CMP_imm(None), "CA": DEX(), "CC": CPY_abs(None), "CD": CMP_abs(None), "CE": DEC_abs(),
        "D0": BNE_rel(None), "D1": CMP_indY(None), "D5": CMP_zpgX(), "D6": DEC_zpgX(), "D8": CLD(), "D9": CMPabsY(None), "DD": CMP_absX(None), "DE": DEC_abs(),
        "E0": CPX_imm(None), "E1": SBC_indX(), "E4": CPX_zpg(None), "E5": SBC_zpg(), "E6": INC_zpg(), "E8": INX(), "E9": SBC_imm(), "EA": NOP(), "EC": CPX_abs(None), "ED": SBC_abs(), "EE": INC_abs(),
        "F0": BEQ_rel(None), "F1": SBC_indY(), "F5": SBC_zpgX(), "F6": INC_zpgX(), "F8": SED(), "F9": SBC_absY(), "FD": SBC_absX(), "FE": INC_absX()
    }

akumulator = 0
X = 0
Y = 0
CarryValue = 0  # Zmienna przechowująca nadmiar liczby dodatniej
# N Z C I D V


pc = (np.random.randint(8, size=(2, 1)))  # musi mieć format macierzy 2 wymiarowej
pc_x = pc[0][0]
pc_y = pc[1][0]


def NOP():
    return None

  
# Wczytaj miejsce z danego miejsca w pamięci do zmiennej Akumaltora
def LDA(pc=pc, x=None, y=None):  # dlaczego tu jest pc=pc, co to w ogóle znaczy
    global akumulator
    global X
    global Y  # nieużywane
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        akumulator = pamiec[x][pc_y]
    elif y is not None:
        akumulator = pamiec[pc_x][y]
    else:
        akumulator = pamiec[pc_x][pc_y]
    print('akumulator: ', akumulator)


# Wczytaj miejsce z danego miejsca w pamięci do zmiennej X
def LDX(pc=pc, x=None, y=None):
    global X
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        X = pamiec[x][pc_y]
    elif y is not None:
        X = pamiec[pc_x][y]
    else:
        X = pamiec[pc_x][pc_y]
    print('X: ', X)


# Wczytaj miejsce z danego miejsca w pamięci do zmiennej Y
def LDY(pc=pc, x=None, y=None):
    global Y
    if x and y is not None:
        Y = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec[pc_x][y]
    else:
        Y = pamiec[pc_x][pc_y]
    print('Y: ', Y)


# Zapisz z Akumaltora do danego miejsca w pamięci
def STA(x=None, y=None):
    global akumulator
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec[pc_x][y]
    else:
        pamiec[pc_x][pc_y] = akumulator
    akumulator = 0


# Zapisz z X do danego miejsca w pamięci do zmiennej
def STX(x=None, y=None):
    global X
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec[pc_x][y]
    else:
        pamiec[pc_x][pc_y] = X
    X = 0
    print('pamięć', pamiec[pc_x][pc_y], 'Wartość Y', X)


# Zapisz z Y do danego miejsca w pamięci do zmiennej
def STY(x=None, y=None):
    global Y
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec[pc_x][y]
    else:
        pamiec[pc_x][pc_y] = Y
    Y = 0
    print('pamięć', pamiec[pc_x][pc_y], 'Wartość X', Y)


def CLC():  # zerowanie C
    global flagi
    flagi.update(C=0)
    print()
    print('CLC zeruje flagi', flagi)
    print()


def CLD():  # zerowanie D
    global flagi
    flagi.update(D=0)
    print()
    print('CLD zeruje flagi', flagi)
    print()


def CLI():  # zerowanie I
    global flagi
    flagi.update(I=0)
    print()
    print('CLI zeruje flagi', flagi)
    print()


def CLV():  # zerowanie V
    global flagi
    flagi.update(V=0)
    print()
    print('CLV zeruje flagi', flagi)
    print()


def SED():  # jedynkowanie D
    global flagi
    flagi.update(D=1)
    print()
    print('SED ustawia flagi', flagi)
    print()


def SEC():  # jedynkowanie C
    global flagi
    flagi.update(C=1)
    print()
    print('SEC ustawia flagi', flagi)
    print()


def SEI():  # jedynkowanie I
    global flagi
    flagi.update(I=1)
    print()
    print('SEI ustawia flagi', flagi)

    
def ADC(pc=pc, x=None, y=None):
    global akumulator
    global flagi
    global CarryValue
    if x and y is not None:
        akumulator = akumulator + pamiec[x][y] + flagi.get('C')
    elif x is not None:
        akumulator = akumulator + pamiec[x][pc_y] + flagi.get('C')
    elif y is not None:
        akumulator = akumulator + pamiec[pc_x][y] + flagi.get('C')
    else:
        akumulator = akumulator + pamiec[pc_x][pc_y] + flagi.get('C')

    # Negative
    if akumulator < 0:
        flagi.update(N=1)
    else:
        flagi.update(N=0)

    # Carry
    if akumulator >= 255 and flagi.get('N') == 0:
        flagi.update(C=1)
        CarryValue = akumulator % 255
        akumulator = 255

    # Zero
    if akumulator != 0:
        flagi.update(Z=0)
    else:
        flagi.update(Z=1)

    # Overflow
    if akumulator > 127 and flagi.get('N') == 1:
        akumulator = 127
        flagi.update(V=1)
    elif akumulator < -128 and flagi.get('N') == 1:
        akumulator = -128
        flagi.update(V=1)
    else:
        flagi.update(V=0)


def SBC(pc=pc, x=None, y=None):
    SEC()
    global akumulator
    if x and y is not None:
        akumulator = akumulator - pamiec[x][y] - (255 - CarryValue)
    elif x is not None:
        akumulator = akumulator - pamiec[x][pc_y] - (255 - CarryValue)
    elif y is not None:
        akumulator = akumulator - pamiec[pc_x][y] - (255 - CarryValue)
    else:
        akumulator = akumulator - pamiec[pc_x][pc_y] - (255 - CarryValue)


# region Do sprawdzenia PROSZE niech ktoś mądry to sprawdzi
def DEX():  # Dekrementacja X
    global X
    X = X - 1
    if X < 0:
        flagi.update(N=1)
    elif X == 0:
        flagi.update(Z=1)


def DEY():  # Dekrementacja Y
    global Y
    Y = Y - 1
    if Y < 0:
        flagi.update(N=1)
    elif Y == 0:
        flagi.update(Z=1)


def INX():  # Inkrementacja X
    global X
    X = X + 1
    if X < 0:
        flagi.update(N=1)
    elif X == 0:
        flagi.update(Z=1)


def INY():  # Inkrementacja Y
    global Y
    Y = Y + 1
    if Y < 0:
        flagi.update(N=1)
    elif Y == 0:
        flagi.update(Z=1)


def INC():  # Inkrementacja  pamięci
    global pamiec
    global flagi
    if flagi.get("Z") == 1:
        pamiec[pc_x][pc_y] = (pamiec[pc_x][pc_y]) + 1
    else:
        pamiec[pc_x][pc_y] = pamiec[pc_x][pc_y]

        
def DEC():  # Dekrementacja pamięci
    global pamiec
    global flagi
    if flagi.get("N") == 1:
        pamiec[pc_x][pc_y] = (pamiec[pc_x][pc_y]) - 1
    else:
        pamiec[pc_x][pc_y] = (pamiec[pc_x][pc_y])


def AND():  # do sprawdzenia jeszcze; logic 1 = 1
    global akumulator
    global pamiec
    if pamiec[pc_x][pc_y] == 1 and akumulator >= 0:
        akumulator = 1
        flagi.update(Z=0)
        flagi.update(N=1)
    else:
        akumulator = 0
        flagi.update(Z=1)
        flagi.update(N=0)


def ORA():
    global akumulator
    global pamiec
    if pamiec[pc_x][pc_y] == 0 and akumulator <= 0:
        akumulator = 0
        flagi.update(Z=1)
        flagi.update(N=0)
    else:
        akumulator = 1
        flagi.update(Z=0)
        flagi.update(N=1)


def EOR():
    global akumulator
    global pamiec
    if (pamiec[pc_x][pc_y] == 0 and akumulator) <= 0 or (pamiec[pc_x][pc_y] == 1 and akumulator >= 0):
        akumulator = 0
        flagi.update(Z=1)
        flagi.update(N=0)
    else:
        akumulator = 1
        flagi.update(Z=0)
        flagi.update(N=1)


#endregion
