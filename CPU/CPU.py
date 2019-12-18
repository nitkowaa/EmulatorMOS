import numpy as np

# lista o długości 65,536‬ (każdy element ma wielkość 1B, w sumie 64kB)
pamiec = [0 for x in range(256*256)]

# https://skilldrick.github.io/easy6502/#first-program
program = ['0xa9', '0x01', '0x8d', '0x00', '0x02', '0xa9', '0x05', '0x8d',
           '0x01', '0x02', '0xa9', '0x08', '0x8d', '0x02', '0x02']

# NEGATIVE, ZERO, CARRY, IRQ DISABLE, DECIMAL, OVERFLOW
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}

# Paweł = Przerobienie pamięci na listę (przepisanie),
# zmienić nazwe indeksów pamięci z małego x,y na jakieś czytelne i lub j
# Hubert = Przerobienie poleceń na ich różne warianty  (Rozkminienie jak działaja warianty)
# Kamil = słownik z Tabelki poleceń (przepisanie)
# Anita = Nowe polecenia w podstawowym wariancie (Rozkminienie)

akumulator = 0
X = 0
Y = 0
CarryValue = 0  # Zmienna przechowująca nadmiar liczby dodatniej

# program counter: przechowuje dwa indeksy - aktualnie czytane komórki pamięci, np. 1536 i 1537
pc_low = 1536
pc_high = pc_low + 1
pc = [pc_high, pc_low]


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
        akumulator = pamiec[x][pc_low]
    elif y is not None:
        akumulator = pamiec[pc_high][y]
    else:
        akumulator = pamiec[pc_high][pc_low]
    print('akumulator: ', akumulator)
#region LDA
def LDA_imm(value):
    pass
    global akumulator
    global  pc_high
    akumulator = pc_high
def LDA_abs():
    pass

def LDA_zpg():
    pass

def LDA_abs_x():
    pass

def LDA_abs_y():
    pass

def LDA_zpg_x():
    pass

def LDA_zpg2_y():
    pass

def LDA_zpg2_x():
    pass

#endregion LDA
#region LDX
def LDX_imm():
    pass

def LDX_abs():
    pass

def LDX_zpg():
    pass
def LDX_abs_y():
    pass

def LDX_zpg_y():
    pass
#endregion LDX
#region LDY
def LDY_imm():
    pass

def LDY_abs():
    pass

def LDY_zpg():

def LDY_abs_y():
    pass

def LDY_zpg_y():
    pass
#endregion LDY
# Wczytaj miejsce z danego miejsca w pamięci do zmiennej X
def LDX(pc=pc, x=None, y=None):
    global X
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        X = pamiec[x][pc_low]
    elif y is not None:
        X = pamiec[pc_high][y]
    else:
        X = pamiec[pc_high][pc_low]
    print('X: ', X)


# Wczytaj miejsce z danego miejsca w pamięci do zmiennej Y
def LDY(pc=pc, x=None, y=None):
    global Y
    if x and y is not None:
        Y = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_low]
    elif y is not None:
        Y = pamiec[pc_high][y]
    else:
        Y = pamiec[pc_high][pc_low]
    print('Y: ', Y)


# Zapisz z Akumaltora do danego miejsca w pamięci
def STA(x=None, y=None):
    global akumulator
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_low]
    elif y is not None:
        Y = pamiec[pc_high][y]
    else:
        pamiec[pc_high][pc_low] = akumulator
    akumulator = 0


# Zapisz z X do danego miejsca w pamięci do zmiennej
def STX(x=None, y=None):
    global X
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_low]
    elif y is not None:
        Y = pamiec[pc_high][y]
    else:
        pamiec[pc_high][pc_low] = X
    X = 0
    print('pamięć', pamiec[pc_high][pc_low], 'Wartość Y', X)


# Zapisz z Y do danego miejsca w pamięci do zmiennej
def STY(x=None, y=None):
    global Y
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_low]
    elif y is not None:
        Y = pamiec[pc_high][y]
    else:
        pamiec[pc_high][pc_low] = Y
    Y = 0
    print('pamięć', pamiec[pc_high][pc_low], 'Wartość X', Y)


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
        akumulator = akumulator + pamiec[x][pc_low] + flagi.get('C')
    elif y is not None:
        akumulator = akumulator + pamiec[pc_high][y] + flagi.get('C')
    else:
        akumulator = akumulator + pamiec[pc_high][pc_low] + flagi.get('C')

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
        akumulator = akumulator - pamiec[x][pc_low] - (255 - CarryValue)
    elif y is not None:
        akumulator = akumulator - pamiec[pc_high][y] - (255 - CarryValue)
    else:
        akumulator = akumulator - pamiec[pc_high][pc_low] - (255 - CarryValue)


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
        pamiec[pc_high][pc_low] = (pamiec[pc_high][pc_low]) + 1
    else:
        pamiec[pc_high][pc_low] = pamiec[pc_high][pc_low]

        
def DEC():  # Dekrementacja pamięci
    global pamiec
    global flagi
    if flagi.get("N") == 1:
        pamiec[pc_high][pc_low] = (pamiec[pc_high][pc_low]) - 1
    else:
        pamiec[pc_high][pc_low] = (pamiec[pc_high][pc_low])


def AND():  # do sprawdzenia jeszcze; logic 1 = 1
    global akumulator
    global pamiec
    if pamiec[pc_high][pc_low] == 1 and akumulator >= 0:
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
    if pamiec[pc_high][pc_low] == 0 and akumulator <= 0:
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
    if (pamiec[pc_high][pc_low] == 0 and akumulator) <= 0 or (pamiec[pc_high][pc_low] == 1 and akumulator >= 0):
        akumulator = 0
        flagi.update(Z=1)
        flagi.update(N=0)
    else:
        akumulator = 1
        flagi.update(Z=0)
        flagi.update(N=1)


#endregion
