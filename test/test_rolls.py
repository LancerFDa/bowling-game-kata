import pytest
from src.scoreCard import ScoreCard

@pytest.mark.state_n
def test_hitting_pins_regular():
    # Hitting pins total = 60
    pins = "12345123451234512345"
    total = 60
    score_card = ScoreCard(pins)
    assert score_card.frame_pins(pins) == total

@pytest.mark.state_n
def test_symbol_zero():
    # test symbol -
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    score_card = ScoreCard(pins)
    assert score_card.frame_pins(pins) == total

    pins = "9-3561368153258-7181"
    total = 82
    score_card = ScoreCard(pins)
    assert score_card.frame_pins(pins) == total

@pytest.mark.spare
def test_spare_not_extra():
    # test spare not extra
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    score_card = ScoreCard(pins)
    assert score_card.frame_pins(pins) == total