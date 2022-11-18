import random
choice = ["n", "k", "b"]


def check_ans(t):
    if t == "k":
        print("kamen'")
    elif t == "b":
        print("bumaga")
    elif t == "n":
        print("nozhnicy")


def main():
    while True:
        turn = input("Enter your turn (k, n, b):").lower()
        if turn == "exit":
            break
        else:
            check_ans(turn)
        c_turn = random.choice(choice)
        check_ans(c_turn)
        yours_count = 0
        comp_count = 0
        if c_turn == "n" and turn == "b" or c_turn == "b" and turn == "k" or c_turn == "k" and turn == "n":
            print("Computer win")
            comp_count += 1
        elif turn == "n" and c_turn == "b" or turn == "b" and c_turn == "k" or turn == "k" and c_turn == "n":
            print("You win")
            yours_count += 1
        elif turn == "n" and c_turn == "n" or turn == "b" and c_turn == "b" or turn == "k" and c_turn == "k":
            print("Friendship")
        print([yours_count, comp_count])


main()
