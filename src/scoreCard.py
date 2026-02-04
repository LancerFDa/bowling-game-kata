class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card

    def frame_pins(self, pins):
        pins = self.pins
        frames = {}
        for i, j  in enumerate(pins):
            frames[i] = j
            score = frames.values()
            #sumar todos los valores de todos los diccionario
            total = sum(int(x) for x in score)
        return total
        