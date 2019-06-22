class CoordinatePlane:

    def __init__(self, size, startPos = "center"):
        self.size = size
        self.start = startPos

    def centerPoint(self):
        if self.start == "center":
            size = (self.size.width() / 2, self.size.height() / 2)
            return size

    def oneUnit(self):
        min = 0
        if self.size.width() > self.size.height():
            min = self.size.height()
        else:
            min = self.size.width()
        return min // 20