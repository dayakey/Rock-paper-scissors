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
    count_comp = 0
    count_yours = 0
    while True:
        while True:
            turn = input("Enter your turn (k, n, b):").lower()
            if turn != "b" and turn != "n" and turn != "k":
                print("Enter only k, n, b")
            else:
                break
        if turn == "exit":
            break
        else:
            check_ans(turn)
        c_turn = random.choice(choice)
        check_ans(c_turn)
        if c_turn == "n" and turn == "b" or c_turn == "b" and turn == "k" or c_turn == "k" and turn == "n":
            print("Computer win")
            count_comp += 1
        elif turn == "n" and c_turn == "b" or turn == "b" and c_turn == "k" or turn == "k" and c_turn == "n":
            print("You win")
            count_yours += 1
        else:
            print("Friendship")
        print("Schet: ", count_comp, ":", count_yours)
        if count_comp == 3:
            print("The end, Computer win game")
            break
        elif count_yours == 3:
            print("The end, You win game")
            break
    rematch()


def rematch():
    while True:
        response = input("Do you want to play a rematch? (YES OR NO):").upper()
        if response != "YES" and response != "NO":
            print("Enter only YES or NO")
        else:
            break
    if response == "YES":
        main()
    elif response == "NO":
        print("Bye!")


main()
