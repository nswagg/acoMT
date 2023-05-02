import math


class TARGET:
    def __init__(self, x, y, weight, animate=0, step=.125):
        self.x = x
        self.y = y
        self.x_init = 0+x
        self.y_init = 0+y
        self.weight = weight
        self.animate = animate  # 0 for off, 1, or 2
        self.time = 0
        self.step = step  # how far the target moves on step

    def __repr__(self):
        return f"[{str(self.x)},{str(self.y)},{str(self.weight)}]"

    def next(self):
        if self.animate != 0:
            self.update_location()
        self.time += self.step

    def update_location(self, radius=1):
        """function for transforming the location of a target"""
        if self.animate == 1:
            """Transform on vertical"""
            self.y = self.y_init + radius * math.sin(2*math.pi * self.time * self.step)
        if self.animate == 2:
            """Transform on horizontal"""
            self.x = self.x_init + radius * math.cos(2*math.pi * self.time * self.step)
        elif self.animate == 3:
            """Transform in circle"""
            self.x = self.x + math.cos(self.time) * radius
            self.y = self.y + math.sin(self.time) * radius
        else:
            self.animate = 0
