import random

variants = ['rock', 'paper', 'scisscors', 'lizard', 'spock']
rock = variants[0]
paper = variants[1]
scisscors = variants[2]
lizard = variants[3]
spock = variants[4]

notice_loss = "You lost"
notice_win = "You won"
notice_draw = "It's a draw"

wins = 0
loses = 0
draws = 0

while input("Do you wanna play? y/n ") == "y":
    your_hand = input("Enter your choise: ")
    
    if your_hand not in variants:
        exit("your choice is unacceptable")
        continue

    computer_hand = random.choice(variants)
    print("Your hand: ", your_hand)
    print("Computer hand: ", computer_hand)

    if your_hand == computer_hand:
        draws += 1
        print(notice_draw)

    elif your_hand == 'rock':
        if computer_hand == 'paper'or computer_hand == 'lizard':
            wins += 1
            print(notice_win)
        else:
            loses += 1
            print(notice_loss)
    elif your_hand == 'paper' :
        if computer_hand == 'scisscors' or computer_hand == 'lizard':
            loses += 1
            print(notice_loss)
        else:
            wins += 1
            print(notice_win)    
    elif your_hand == 'scisscors':
        if computer_hand == 'rock' or computer_hand == 'spok':
            loses += 1
            print(notice_loss)
        else:
            wins += 1
            print(notice_win)
    elif your_hand == lizard:
        if computer_hand == spock or computer_hand == paper:
            wins +=1
            print(notice_win)
        else:
            loses +=1
            print(notice_loss)
    else:
        if computer_hand == rock or computer_hand == scisscors:
            wins +=1
            print(notice_win)
        else:
            wins += 1
            print(notice_win)                       
    print("wins ", wins,
    "; loses ", loses, 
    "; draws ", draws)
    