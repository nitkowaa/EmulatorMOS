import unittest
from CPU import *

#region przeniesione z CPU

#Tutaj znajduje sie wypisanie wartości pamieci i losowego punktu, przeniesione z pliku CPU
def LosowaniePunktuPamieci():
    print("Flagi ", flagi)
    print(pamiec)
    print()
    print('pc_x: ', pc_x)
    print('pc_y: ', pc_y)
    print('wartosc pamieci pc_x,pc_y: ', pamiec[pc_x][pc_y])
    print()


#Tutaj znajdują sie wywołania przeniesione z pliku CPU
def Testy():
    print('TESTY:')
    print(akumulator, X, Y)
    LDA()  # LDA
    LDX()  # LDX
    LDY()  # LDY
    print(akumulator, X, Y)
    STA()  # STA
    STX()  # STX
    STY()  # STY
    print(akumulator, X, Y)
    CLC()  # CLC
    CLD()  # CLD
    CLI()  # CLI
    CLV()  # CLV
    SED()  # SED
    SEC()  # SEC
    SEI()  # SEI

#endregion

#region wywołania funkcji
LosowaniePunktuPamieci()
Testy()
#endregion


#region testy automatyczne i jak powinno wyglądać import (TODO)
'''
def command(x):
    x = 0  #Placeholder for more actual method

class TestCommandsMethods(unittest.TestCase):


    def test_commandCMP(self):
        self.assertEqual('CMP',command(x))

if __name__ == '__main__':
    unittest.main() '''
#endregion
