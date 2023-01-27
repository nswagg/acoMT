
class Ant:
    """
    Ant class for storing individual ant object data like location information.
    Minimize internal computation and initialize externally
    """

    def __init__(self, loc, jump, initAngle):
        """Initial ant values. These can be updated over time"""
        self.coords = loc  # [x,y] coords
        self.speed = jump
        self.angle = initAngle # 0 - 359 degrees
        self.isTracking = False
        self.isWandering = True

    def getAngle(self):
        return self.angle

    def getCoords(self):
        return self.coords

    def getSpeed(self):
        return self.speed

    def setAngle(self, angle):
        self.angle = angle

    def setCoords(self, coords):
        self.coords = coords

    def setSpeed(self, vel):
        self.speed = vel

    def setTracking(self):
        self.isTracking = True
        self.isWandering = False

    def setWandering(self):
        self.isTracking = False
        self.isWandering = True

    def wander(self):
        """wild ant function for moving through a space without a known target"""

    def track(self):
        """wild ant has detected a pheromone trail and begins following it"""

    def returnHome(self):
        """function for getting an ant to return home? Don't want to hardcode the coords"""

    def update(self):
        """Updates ant object data"""