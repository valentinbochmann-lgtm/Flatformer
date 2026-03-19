import json
from world import World

LEVELS = [
    "levels/level1.json",
    "levels/level2.json",
    "levels/level3.json",
    # add more levels here
]

class LevelManager:
    def __init__(self):
        self.current_index = 0

    def load_current(self):
        path = LEVELS[self.current_index]
        with open(path, "r") as f:
            data = json.load(f)
        return World(data)

    def next_level(self):
        if self.current_index < len(LEVELS) - 1:
            self.current_index += 1
            return self.load_current()
        return None  # no more levels

    def has_next(self):
        return self.current_index < len(LEVELS) - 1