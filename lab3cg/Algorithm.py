from enum import Enum


class Algorithm(Enum):
    DDA = 0  # digital differential analyzer algorithm
    BRN = 1  # Bresenham algorithm with real numbers
    BIN = 2  # Bresenham algorithm with integer numbers
    BAA = 3  # Bresenham aliasing algorithm
    LA  = 4  # library algorithm

    # def __init__(self):
    #     self.DDA = 0  # digital differential analyzer algorithm
    #     self.BRN = 1  # Bresenham algorithm with real numbers
    #     self.BIN = 2  # Bresenham algorithm with integer numbers
    #     self.BAA = 3  # Bresenham aliasing algorithm
    #     self.LA = 4  # library algorithm
    #
    #     self.__algs = {0:  "ЦДА",
    #                    1: "Брезенхем с действит. числами",
    #                    2: "Брезенхем с целыми числами",
    #                    3: "Брезенхем с устранением ступенчатости",
    #                    4: "Библиотечный (PyQt5)"}
    #
    # def getStringAlgs(self):
    #     return self.__algs
    #
    # def DDA(self):
    #     return self.DDA
    #
    # def BRN(self):
    #     return self.BRN
    #
    # def BIN(self):
    #     return self.BIN
    #
    # def BAA(self):
    #     return self.BAA
    #
    # def LA(self):
    #     return self.LA
    #
    # def getStringByCode(self, code):
    #     if   code == self.DDA:
    #         return self.__algs.get(self.DDA)
    #     elif code == self.BRN:
    #         return self.__algs.get(self.BRN)
    #     elif code == self.BIN:
    #         return self.__algs.get(self.BIN)
    #     elif code == self.BAA:
    #         return self.__algs.get(self.BAA)
    #     elif code == self.LA:
    #         return self.__algs.get(self.LA)
    #
    # def getCodeByString(self, string):
    #     if   string == self.__algs.get(self.DDA):
    #         return self.DDA
    #     elif string == self.__algs.get(self.BRN):
    #         return self.BRN
    #     elif string == self.__algs.get(self.BIN):
    #         return self.BIN
    #     elif string == self.__algs.get(self.BAA):
    #         return self.BAA
    #     elif string == self.__algs.get(self.La):
    #         return self.LA
