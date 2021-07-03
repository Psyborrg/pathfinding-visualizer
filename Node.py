from Dijkstras import bigNumber


class Node():

    def __init__(self, row, col, widget):
        self.isPassable = True
        self.isStart = False
        self.isFinish = False
        self.row = row
        self.col = col
        self.weight = 1
        self.widget = widget
        self.prevNode = None
        self.distance = bigNumber