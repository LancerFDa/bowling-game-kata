class Game:
    def hitting_pins_regular(self, pins):
        self.pins = pins

    def open_frame(self):
        for pin in self.pins:
            if "X" != pin and "/" != pin:
                return 60