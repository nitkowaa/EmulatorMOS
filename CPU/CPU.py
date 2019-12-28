# NEGATIVE, ZERO, CARRY, IRQ DISABLE, DECIMAL, OVERFLOW
flagi = {'N': 0, 'Z': 0, 'C': 0, 'I': 0, 'D': 0, 'V': 0}
value = 0
akumulator = 0
X = 0
Y = 0
CarryValue = 0  # Zmienna przechowująca nadmiar liczby dodatniej

# program counter: przechowuje indeks czytanej komórki pamięci
pc = 1536


#def get_index(): nie wiem po co
    #return pamiec[pc+2]*0x100 + pamiec[pc+1]


#def load_program():
 #for i in range(len(program)):
  #      pamiec[1536+i] = program[i]


# region Metody Load

# region LDA

# Wczytaj podaną wartość do Akumulatora
def LDA_imm(value):
    global akumulator
    global pc
    akumulator = value
    pc = pc + 2  # przechodzi o 2 miejsca dalej
# endregion LDA

# region LDX
def LDX_imm(value):
    global X
    global pc
    X = value
    pc = pc + 2  # przechodzi o 2 miejsca dalej
# endregion LDX
# region LDY
def LDY_imm(value):
    global Y
    global pc
    Y = value
    pc = pc + 2  # przechodzi o 2 miejsca dalej



# region Metody Flag
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


# endregion

def NOP():
    return None


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



# metody branchowe wczytują etykiety
def BCS_rel(label):  # skok jeśli C=1
    global pc
    global flagi
    if flagi.get('C') == 1:
        pc = label
    else:
        pc = pc+2


def BCC_rel(label):  # skok jeśli C=0
    global pc
    global flagi
    if flagi.get('C') == 0:
        pc = label
    else:
        pc = pc + 2


def BEQ_rel(label):  # skok jeśli Z=1
    global pc
    global flagi
    if flagi.get('Z') == 1:
        pc = label
    else:
        pc = pc + 2


def BNE_rel(label):  # skok jeśli Z=0
    global pc
    global flagi
    if flagi.get('Z') == 0:
        pc = label
    else:
        pc = pc + 2


def BMI_rel(label):  # skok jeśli N=1
    global pc
    global flagi
    if flagi.get('N') == 1:
        pc = label
    else:
        pc = pc + 2


def BPL_rel(label):  # skok jeśli N=0
    global pc
    global flagi
    if flagi.get('N') == 0:
        pc = label
    else:
        pc = pc + 2


def BVS_rel(label):  # skok jeśli V=1
    global pc
    global flagi
    if flagi.get('V') == 1:
        pc = label
    else:
        pc = pc + 2


def BVC_rel(label):  # skok jeśli V=0
    global pc
    global flagi
    if flagi.get('V') == 0:
        pc = label
    else:
        pc = pc + 2
# endregion branch


# słownik rozkazów
rozkazy = {0xa9: LDA_imm(89)
#,0xa2: LDX_imm(82),0xa0: LDY_imm(17)
}


def main():
    print('pc: ', pc, 'akumulator: ', akumulator, '\n')
    print('X: ', X, 'Y: ', Y, '\n')


if __name__ == '__main__':
    main()
