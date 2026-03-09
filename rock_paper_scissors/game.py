from enum import Enum
import random

class Hand(Enum):
    paper = 1
    rock = 2
    scissors = 3

    def __str__(self) -> str:
        return self.name

class Player():
    def __init__(self, name):
        self.name = name
        self.gesture = Hand(1)
        self.score = 0

    def set_gesture(self, gesture: Hand):
        self.gesture = gesture

    def bump_score(self):
        self.score += 1


def random_hand_gesture() -> Hand:
    return random.choice(list(Hand))

def print_scores(p1: Player, p2: Player):
    print("====== SCORE ======")
    print(f"{p1.name} = {p1.score}")
    print(f"{p2.name} = {p2.score}")
    print()

def get_winning_player(p1: Player, p2: Player) -> Player | None:
    p1_val = p1.gesture.value
    p2_val = p2.gesture.value

    if p1_val == p2_val:
        return None
    
    if p1_val == ((p2_val + 1) % 3) + 1:
        return p1
    return p2
