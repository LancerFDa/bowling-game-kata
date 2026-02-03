
class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card

    def frame_pins(self, pins):
        pins = list(pins.replace('-', '0'))
        return sum(int(pin) for pin in pins)
