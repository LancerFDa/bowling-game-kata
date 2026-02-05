class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card

    def frame_pins(self, pins):
        pins = self.pins
        score = list(pins)
        frames = []
        for i in range(len(pins)):
            if score[i] == "-":
                score[i] = 0
        for i in score:
            frames.append(int(i))
        total = sum(frames)
        return total
    

if __name__=="__main__":
    ScoreCard("9-9-9-9-9-9-9-9-9-9-").frame_pins()

    