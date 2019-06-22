from abc import ABC, abstractmethod

from PyQt5.QtGui import QPen, QColor
from PyQt5.QtCore import Qt


class DrawableObject(ABC):

    @abstractmethod
    def draw(self, sizeScreen, qp):
        pass

    def _drawDDA(self, xs, ys, xe, ye, color, qp):
        qp.setPen(self._newPen(color))

        if xs == xe and ys == ye:
            qp.drawPoint(xs, ys)
            return None, None

        dx = xe - xs
        dy = ye - ys
        lx = abs(dx)
        ly = abs(dy)

        if lx > ly:
            l = lx
        else:
            l = ly

        dx /= l
        dy /= l

        x = xs
        y = ys

        i = 1
        while i <= l:
            qp.drawPoint(x, y)
            x += dx
            y += dy
            i += 1

        if round(x) == round(xe) and round(y) == round(ye):
            print("ЦДА: пришел в конечную точку")
            return None, None
        else:
            print(x, y)
            print(xe, ye)
            print("ЦДА: не пришел в конечную точку")
            return x, y

    def _drawBRN(self, xs, ys, xe, ye, color, qp):
        qp.setPen(self._newPen(color))
        if xs == xe and ys == ye:
            qp.drawPoint(xs, ys)
            return None, None
        x = xs
        y = ys
        dx = xe - xs
        dy = ye - ys
        sx = self.sign(dx)  # знак приращения совпадает со знаком разности конечной и начальной координат отрезка
        sy = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)

        # большее по модулю приращение принимается шагом растра
        exchange = False
        if dx <= dy:
            exchange = True
            dx, dy = dy, dx

        m = dy / dx  # тангенс угла наклона

        e = m - 0.5  # ошибка
        i = 1

        # Основной цикл высвечивания отрезка
        while i <= dx:
            qp.drawPoint(x, y)
            if e >= 0:
                if exchange is False:
                    y += sy
                else:
                    x += sx
                e -= 1
            if e < 0:
                if exchange is False:
                    x += sx
                else:
                    y += sy
                e += m
            i += 1

        if x == xe and y == ye:
            print("Брезенхем с действ. числами: пришел в конечную точку")
            return None, None
        else:
            print(x, y)
            print(xe, ye)
            print("Брезенхем с действ. числами: не пришел в конечную точку")
            return x, y

    def _drawBIN(self, xs, ys, xe, ye, color, qp):
        qp.setPen(self._newPen(color))

        # Проверка на вырожденность
        if xs == xe and ys == ye:
            qp.drawPoint(xs, ys)
            return None, None

        x = xs
        y = ys
        dx = xe - xs
        dy = ye - ys
        sx = self.sign(dx)
        sy = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)

        exchange = False
        if dx <= dy:
            exchange = True
            dx, dy = dy, dx

        e = 2 * dy - dx
        i = 1

        # Основной цикл высвечивания отрезка
        while i <= dx:
            qp.drawPoint(x, y)
            if e >= 0:
                if exchange is False:
                    y += sy
                else:
                    x += sx
                e -= 2 * dx
            if e < 0:
                if exchange is False:
                    x += sx
                else:
                    y += sy
                e += 2 * dy
            i += 1

        if xe == x and ye == y:
            print("Брезенхем с целыми числами: пришел в конечную точку")
            return None, None
        else:
            print(x, y)
            print(xe, ye)
            print("Брезенхем с целыми числами: не пришел в конечную точку")
            return x, y

    def _drawBAA(self, xs, ys, xe, ye, color, qp):
        qp.setPen(self._newPen(color))

        # Проверка на вырожденность
        if xs == xe and ys == ye:
            qp.drawPoint(xs, ys)
            return None, None

        x = xs
        y = ys
        dx = xe - xs
        dy = ye - ys
        sx = self.sign(dx)
        sy = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)

        if color == QColor(Qt.black):
            i_max = 255
        else:
            i_max = max(color.getRgb()[0], color.getRgb()[1], color.getRgb()[2])

        try:
            m = dy / dx
        except ZeroDivisionError:
            m = 0

        exchange = False
        if dx <= dy:
            dx, dy = dy, dx
            exchange = True
            if m:
                m = 1 / m

        m *= i_max
        e = i_max / 2
        w = i_max - m
        i = 1
        while i <= dx:
            new = QColor()
            new.setRgb(color.getRgb()[0], color.getRgb()[1], color.getRgb()[2], alpha=255 - (255 - e))
            qp.setPen(self._newPen(new))
            qp.drawPoint(x, y)
            if e < w:
                if exchange:
                    y += sy
                else:
                    x += sx
                e += m
            else:
                x += sx
                y += sy
                e -= w
            i += 1

        if xe == x and ye == y:
            print("Брезенхем с устранением ступенчатости: пришел в конечную точку")
            return None, None
        else:
            print(x, y)
            print(xe, ye)
            print("Брезенхем с устранением ступенчатости: не пришел в конечную точку")
            return x, y

    def _drawLA(self, xs, ys, xe, ye, color, qp):
        qp.setPen(self._newPen(color))
        qp.drawLine(xs, ys, xe, ye)

    def sign(self, x):
        if x == 0:
            return 0
        else:
            return x / abs(x)

    def _newPen(self, color):
        newPen = QPen()
        newColor = QColor(color)
        newPen.setColor(newColor)
        return newPen
