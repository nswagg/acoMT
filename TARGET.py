class TARGET:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def __repr__(self):
        return f"[{str(self.x)},{str(self.y)},{str(self.weight)}]"

    def update_location(self):
        return
