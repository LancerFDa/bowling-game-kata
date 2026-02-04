class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card

    def frame_pins(self, pins):
        pins = self.pins
        L = list(pins)
        frames = {}
        for i, j  in enumerate(L):
            if i % 2 == 0:
                frames[i // 2] = [int(j)]
            else:
                frames[i // 2].append(int(j))
        return sum(sum(v) for v in frames.values())
        