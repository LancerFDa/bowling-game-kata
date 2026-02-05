class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card

    def frame_pins(self, pins):
        pins = self.pins
        score = list(pins)
        frames = []
        for i,j in enumerate(score):
            if score[i] == "-":
                frames.append(0)
            elif score[i]:
                if score[i] == "/":
                    frames.append(10 - frames[-1])
                else : frames.append(int(score[i]))
        for i,j in enumerate(frames):
            if frames[i] + frames[i-1] == 10:
                frames[i] = frames[i] + frames[i+1]
        total = sum(frames)
        return total
    

if __name__=="__main__":
    ScoreCard("9-3/613/815/-/8-7/8-").frame_pins("9-3/613/815/-/8-7/8-")

    