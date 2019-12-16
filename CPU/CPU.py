import numpy as np

pamiec = np.random.randint(2, size=(8, 8))  # Two-dimensional array
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}

# Paweł = Przerobienie pamieci na liste (przepisanie), zmiennic nazwe indeksow pamieci z malego x,y na jakieś czytlne i lub j
# Hubert = Przerobienie polecen na ich rozne warianty  (Rozkmienien jak działaja warianty)
# Kamil = słownik z Tabelki poleceń (przepisanie)
# Anita = Nowa polecenia w podstawowym wariancie (Rozkminienie)

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


def JMP():  #skok do konkretnej instrukcji, pominięcie innych instrukcji, brak flag jakichkolwiek
    global akumulator
    global pamiec


# Instrukcje branch zależą od flag


def BCS():  # skok jeśli C=1
    global akumulator
    global pamiec


def BCC():  # skok jeśli C=0
    global akumulator
    global pamiec


def BEQ():  # skok jeśli Z=1
    global akumulator
    global pamiec


def BNE():  # skok jeśli Z=0
    global akumulator
    global pamiec


def BMI():  # skok jeśli N=1
    global akumulator
    global pamiec


def BPL():  # skok jeśli N=0
    global akumulator
    global pamiec


def BVS():  # skok jeśli V=1
    global akumulator
    global pamiec


def BVC():  # skok jeśli N=0
    global akumulator
    global pamiec


#endregion
