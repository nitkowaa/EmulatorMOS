import numpy as np


pamiec = np.random.randint(2, size=(8, 8))  # Two-dimensional array
flagi = {"N" : "Not affected" ,"Z" : "Not affected","C" : "Not affected","I" : "Not affected","D" : "Not affected","V" : "Not affected"}
print("Flagi ",flagi)
print(pamiec)
print()

akumulator = 0
X = 0
Y = 0

#N Z C I D V


pc = (np.random.randint(8,size=(2,1))) # musi mieć format macierzy 2 wymiarowej
pc_x = pc[0][0]
pc_y = pc[1][0]

#Wczytaj miesjce z danego miejsca w pamieci do zmiennej Akumaltora


def LDA(pc = pc,x = None,y = None):
    global akumulator
    global X
    global Y
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        akumulator = pamiec[x][pc_y]
    elif y is not None:
        akumulator = pamiec [pc_x][y]
    else:
        akumulator = pamiec[pc_x][pc_y]

    print('akumulator: ',akumulator)

#Wczytaj miesjce z danego miejsca w pamieci do zmiennej X


def LDX(pc = pc,x = None,y = None):
    global X
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        X = pamiec[x][pc_y]
    elif y is not None:
        X = pamiec [pc_x][y]
    else:
        X = pamiec[pc_x][pc_y]

    print('X: ',X)

#Wczytaj miesjce z danego miejsca w pamieci do zmiennej Y


def LDY(pc = pc,x = None,y = None):
    global Y
    if x and y is not None:
        Y = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec [pc_x][y]
    else:
        Y = pamiec[pc_x][pc_y]

    print('Y: ',Y)


#Zapisz z Akumaltora do danego miejsca w pamieci do zmiennej


def STA(x = None,y = None):
    global akumulator
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec [pc_x][y]
    else:
        pamiec[pc_x][pc_y] = akumulator
    akumulator = 0
    print('pamiec',pamiec[pc_x][pc_y],'akumulator',akumulator)
#Zapisz z X do danego miejsca w pamieci do zmiennej


def STX(x = None,y = None):
    global X
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec [pc_x][y]
    else:
        pamiec[pc_x][pc_y] = X
    X = 0
    print('pamiec',pamiec[pc_x][pc_y],'Wartosc Y',X)
#Zapisz z Y do danego miejsca w pamieci do zmiennej


def STY(x = None,y = None):
    global Y
    if x and y is not None:
        X = pamiec[x][y]
    elif x is not None:
        Y = pamiec[x][pc_y]
    elif y is not None:
        Y = pamiec [pc_x][y]
    else:
        pamiec[pc_x][pc_y] = Y
    Y = 0
    print('pamiec',pamiec[pc_x][pc_y],'Wartosc X',Y)


print('pc_x: ' ,pc_x)
print('pc_y: ' ,pc_y)
print('wartosc pamieci: ',pamiec[pc_x][pc_y])
print()
print('TESTY:')
print(akumulator,X,Y)
LDA() #LDA

LDX() #LDX
LDY() #LDY
print(akumulator,X,Y)
STA() #STA
STX() #STX
STY() #STY
print(akumulator,X,Y)


#Tu zaczynamy zerowanie flag
def CLC(): #zerowanie C
    global flagi
    flagi.update(C="0")

print()
CLC() #CLC
print()
print("CLC start")
print("CLC robi flagi" , flagi)


def CLD(): #zerowanie D
    global flagi
    flagi.update(D="0")

print()
CLD() #CLD
print()
print("CLD start")
print("CLD robi flagi" , flagi)


def CLI(): #zerowanie I
    global flagi
    flagi.update(I="0")

print()
CLI() #CLI
print()
print("CLI start")
print("CLI robi flagi" , flagi)



def CLV(): #zerowanie V
    global flagi
    flagi.update(V="0")

print()
CLV() #CLV
print()
print("CLV start")
print("CLV robi flagi" , flagi)


def SED(): #jedynkowanie D
    global flagi
    flagi.update(D="1")

print()
SED() #SED
print()
print("SED start")
print("SED robi flagi" , flagi)


def SEC(): #jedynkowanie C
    global flagi
    flagi.update(C="1")

print()
SEC() #SEC
print()
print("SEC start")
print("SEC robi flagi" , flagi)


def SEI(): #jedynkowanie I
    global flagi
    flagi.update(I="1")

print()
SEI() #SEI
print()
print("SEI start")
print("SEI robi flagi" , flagi)