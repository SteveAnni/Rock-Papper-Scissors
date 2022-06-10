import random
from simple_chalk import green, cyan, red, blue, yellowBright



GAME_OPTIONS = {'R': "ROCK", 'S': "SCISSORS", 'P': "Paper"}     # this defines the choices available in the game
GAME_RESULTS = {    # this defines what happens by combining the player and computer choice
    'PR': "covers",
    'SP': "cuts",
    'RS': "beats",
}

h = cyan("##########################################################")    
print(f"""{h}
{green('🚀🚀Welcome to ROCK-PAPER-SCISSORS🚀🚀').center(len(h))}
{h}""")

while True:     # starting the game loop
    player = input(f"\n\t{red('R - ROCK')}\n\t{blue('P - PAPER')}\n\t{yellowBright('S - SCISSORS')}\nMake your play: ").upper()   # player makes his/her play
    computer = random.choice(list(GAME_OPTIONS.keys()))     # the computer makes its play.
    # computer = 'S'
    print(f"\n\tPlayer ({GAME_OPTIONS.get(player)}) : CPU ({GAME_OPTIONS.get(computer)})")

    if not GAME_OPTIONS.get(player):
        print("[-] Invalid Option. Please Try Again!")
        continue

    
    if player == computer:  # asks the player to try again if it is a tie
        print("\n\tIt is a TIE. Play Again.")
        continue
    else:
        determinant = player + computer  # 'PR'    

        if GAME_RESULTS.get(determinant):   
            print("\n\tPlayer WON!!!")
            break
        else:  
            print("\n\tComputer WON!!! Play Again.")
            determinant = determinant[::-1]  #  'RP'

        # print(f"\n\t{GAME_OPTIONS.get(determinant[0])} {GAME_RESULTS.get(determinant)} {GAME_OPTIONS.get(determinant[1])}. Play Again.")    
        continue