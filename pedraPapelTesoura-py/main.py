from random import randint

#moves
moves = ["rock", "paper", "scissors"]

computer = moves[randint(0,2)]


while True:
    player = input("rock, paper or scissor? (or end the game) ").lower()

    if player == "end the game":
        print("the game has ended")
        break
    #caso haja empate
    elif player == computer:
        print('Tie')
    #pedra
    elif player == "rock":
        if computer == "paper":
            print("you loose", computer, "beats", player)
        else:
            print("you win", player, "beats", computer)
    #papel
    elif player == "paper":
        if computer == "scissors":
            print("you loose", computer, "beats", player)
        else:
            print("you win", player, "beats", computer)
    #tesoura
    elif player == "scissors":
        if computer == "rock":
            print("you loose", computer, "beats", player)
        else:
            print("you win", player, "beats", computer)

    

#myList = [1, 2, 3]
#mylist[1]