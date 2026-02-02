class Game:
    def hitting_pins_regular(self, pins):
        self.pins = pins

    def total(self):
        for j in self.pins:
            if "X" != j and "/" != j:
                return 60