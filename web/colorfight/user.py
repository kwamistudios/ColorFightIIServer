class User:
    def __init__(self, username, password):
        self.uid = uid
        self.username = username
        self.password = password
        self.energy   = 100
        self.gold     = 0
        self.energy_source = 0
        self.gold_source = 0
        self.dead = False
        self.cells = {}

    def get_cell(self, cell):
        self.cells[cell.position] = cell

    def update(self):
        self.energy += self.energy_source
        self.gold   += self.gold_source
        if len(self.cells) == 0:
            self.dead = True

    def info(self):
        return {"uid":self.uid, \
                "username": self.username, \
                "energy": self.energy, \
                "gold": self.gold, \
                "dead": self.dead, \
                "energy_source": self.energy_source, \
                "gold_source": self.gold_source}
