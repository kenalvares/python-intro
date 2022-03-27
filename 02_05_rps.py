# RPS

import random, sys
print('RPS')

# These vars track wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:     # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:     # Player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break   # Break out of player loop
        print('Type one of r, p, s, or q.')

    # Display player choice:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display computer choice:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif (playerMove == 'r' and computerMove == 's') or (playerMove == 'p' and computerMove == 'r') or (playerMove == 's' and computerMove == 'p'):
        print('You win!')
        wins = wins + 1
    elif (playerMove == 'r' and computerMove == 'p') or (playerMove == 'p' and computerMove == 's') or (playerMove == 's' and computerMove == 'r'):
        print('You lose!')
        losses = losses + 1
