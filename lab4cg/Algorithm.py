from enum import Enum


class Algorithm(Enum):
    CANON_EQ = 'Каноническое уравнение'
    PARA_EQ = 'Параметрическое уравнение'
    BRESENHAM_ALG = 'Алгоритм Брезенхема'
    MIDDLE_DOT_ALG = 'Алгоритм средней точки'
    LIBRARY_ARG = 'Библиотечный алгоритм (PyQt5)'

    def getArray(self):
        return [self.CANON_EQ.value, self.PARA_EQ.value,
                self.BRESENHAM_ALG.value, self.MIDDLE_DOT_ALG.value,
                self.LIBRARY_ARG.value]
