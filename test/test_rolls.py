import pytest
from src.rolls import Game

@pytest.mark.state_n
def test_hitting_pins_regular():
    # Hitting pins total = 60
    pins = "12345122451234512345"
    total = 60
    score_card = Game()
    score_card.hitting_pins_regular(pins)
    assert score_card.total() == total