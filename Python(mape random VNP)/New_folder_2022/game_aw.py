import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []
win_history = []

while(True):

    human_turn = input("Enter your turn, or tipe exit: ")
    computer_turn = random.choice(turns)

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    if human_turn == 'exit':
        print('thx for playing')
        break

    print(f'human:{human_turn}vs. computer:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
        win_history.append('Draw')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
        win_history.append('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
        win_history.append('Human wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
        win_history.append('Human wins!')
    else:
        print('Computer wins!')
        win_history.append('Computer wins!')

print(f'You have plaeyed {len(human_turns)-1} times')
print(human_turns)
print(computer_turns)