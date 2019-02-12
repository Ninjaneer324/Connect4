class circle:

    red = 0
    green = 0
    blue = 0
    x = 0
    y = 0
    done = False

    def __init__(self, (r,g,b,), (x,y)):
        self.red = r
        self.green = g
        self.blue = b
        self.x = x
        self.y = y

    def moveLeft(self):
        self.x -= 100

    def moveRight(self):
        self.x += 100

    def color(self):
        return (self.red, self.green, self.blue)

    def pos(self):
        return (self.x, self.y)