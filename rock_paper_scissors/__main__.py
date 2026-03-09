import argparse
from .game import Player, random_hand_gesture, get_winning_player, print_scores

def iterative(rounds: int):
    p1 = Player(input("Player one name: "))
    p2 = Player(input("Player two name: "))

    for _ in range(rounds):
        p1.set_gesture(random_hand_gesture())
        p2.set_gesture(random_hand_gesture())

        winner = get_winning_player(p1, p2)

        print(f"{p1.name} choose {p1.gesture}")
        print(f"{p2.name} choose {p2.gesture}")

        if winner is None:
            print("It's a tie!")
            print()
            continue

        print(f"{winner.name} won!")
        winner.bump_score()
        print()

    print_scores(p1, p2)
    

def interactive():
    p1 = Player(input("Player one name: "))
    p2 = Player(input("Player two name: "))

    on = True

    while on:
        p1.set_gesture(random_hand_gesture())
        p2.set_gesture(random_hand_gesture())

        winner = get_winning_player(p1, p2)

        print(f"{p1.name} choose {p1.gesture}")
        print(f"{p2.name} choose {p2.gesture}")

        if winner is None:
            print("It's a tie!")
            print()
        else:
            print(f"{winner.name} won!")
            winner.bump_score()

        on = input("Do you want to continue? (y/N)").strip().lower() == "y"
        print()

    print_scores(p1, p2)

def main():
    parser = argparse.ArgumentParser(
            prog="Rock Paper Scissors",
            description="Simple python rock paper scissors game",
            epilog="womp womp"
            )
    parser.add_argument("-i", "--iterative", type=int, help="How many times you want to play")
    parser.add_argument("-a", "--auto", help="Run the game and ask if you want to continue after each round", action="store_true")

    opts = parser.parse_args()

    try:
        if opts.auto:
            interactive()
        elif opts.iterative is not None:
            iterative(opts.iterative)
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
