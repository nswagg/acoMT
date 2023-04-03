from obj.target import Target
from obj.hive import Hive


class Environment:
    def __init__(self, env):
        self.env = env
        self.targets: [Target] = []     # list of Targets in the environment
        self.hives: [Hive] = []         # list of Hives in the environment
