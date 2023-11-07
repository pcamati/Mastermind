
'''
This program executes the game Mastermind ("Senha") where 
two players compete against each other trying to guess
the sequence of colored pegs the other player set up.

Terms:

 - codemaker: player who creates the code
 - codebreaker: player who guesses the code
 - decoding_board: set of pins determined by the codemaker
 - code_pegs: the colored pins the codemaker can choose
 - key_pegs: white and black pins providing hints to the codebreaker

Rules:

The two players decide in advance how many games they will play,
which must be an even number.
One player becomes the codemaker, the other the codebreaker.
The codemaker chooses a pattern of four code pegs. 
Players decide in advance whether duplicates and blanks are allowed.
If so, the codemaker may even choose four same-colored code pegs 
or four blanks. 
If blanks are not allowed in the code, the codebreaker may not use 
blanks in their guesses. 
The codemaker places the chosen pattern in the four holes covered 
by the shield, visible to the codemaker but not to the codebreaker.
The codebreaker tries to guess the pattern, in both order and color,
within eight to twelve turns. 
Each guess is made by placing a row of code pegs on the 
decoding board.
Once placed, the codemaker provides feedback by placing from zero 
to four key pegs in the small holes of the row with the guess. 
A colored key peg (usually black) is placed for each code peg from the guess which 
is correct in both color and position. 
A white key peg indicates the existence of a correct color code peg 
placed in the wrong position.
If there are duplicate colors in the guess, they cannot all be 
awarded a key peg unless they correspond to the same number of 
duplicate colors in the hidden code. 
For example, if the hidden code is red-red-blue-blue and the player 
guesses red-red-red-blue, the codemaker will award two colored 
key pegs for the two correct reds, nothing for the third red as 
there is not a third red in the code, and a colored key peg for 
the blue. 
No indication is given of the fact that the code also includes a 
second blue.
Once feedback is provided, another guess is made; 
guesses and feedback continue to alternate until either the 
codebreaker guesses correctly, or all rows on the decoding board 
are full.
Traditionally, players can only earn points when playing as the 
codemaker. 
The codemaker gets one point for each guess the codebreaker makes. 
An extra point is earned by the codemaker if the codebreaker is 
unable to guess the exact pattern within the given number of turns.
(An alternative is to score based on the number of key pegs placed.)
The winner is the one who has the most points after the agreed-upon 
number of games are played.

'''

class game:

    decoding_board_size = 4
    #for testing purposes gonna set the value to 4
    number_attempts = 4 #12

    def __init__(self,number_rounds, player_one, player_two):
        if not isinstance(number_rounds, int):
            raise TypeError("Number of rounds must be an integer")
        if number_rounds % 2 != 0:
            raise ValueError("Number of rounds must be an even number")
        if not isinstance(player_one, str) & isinstance(player_two, str):
            raise TypeError("Players' names must be strings")
        
        self.rounds = number_rounds
        self.player_one = player_one
        self.player_two = player_two
        self.code_pegs = []
        self.key_pegs = []
        self.score_player_one = []
        self.score_player_two = []
        self.codemaker = None
        self.codebreaker = None
        self.decoding_board = []
        self.guessed_list = []

    def set_code_pegs(self,code_pegs):
        self.code_pegs = code_pegs

    def display_board(self):
        print("\n      Guessed Attempts                | | |       Key pegs \n")
        for line in range(len(self.guessed_list)):
            print(" | ".join(self.guessed_list[line])+" | | | "+" | ".join(self.key_pegs[line]))

    def set_decoding_board(self, codemaker):
        self.decoding_board = input(f"{codemaker.upper()}, please enter a sequence of colored pegs for the decoding board: ").split()

    def is_attempt_valid(self, guessed_attempt):
        while True:
            if len(guessed_attempt)!=len(self.decoding_board):
                guessed_attempt = input("Please enter a valid guess: ").split()
                if guessed_attempt=='exit':
                    break
            else:
                break
        return guessed_attempt

    def is_correct_guess(guessed_attempt):
        #check if the guess is the correct code
        pass

    def check_key_pegs(self, guessed_attempt: list):
        black_pegs = 0
        white_pegs = 0
        temporary_guessed_attempt = guessed_attempt[:]
        temporary_decoding_board = self.decoding_board[:]
        for guessed_peg, decoding_peg in zip(guessed_attempt, self.decoding_board):
            if guessed_peg == decoding_peg:
                black_pegs += 1
                temporary_decoding_board.remove(decoding_peg)
                temporary_guessed_attempt.remove(guessed_peg)
        for colors in temporary_guessed_attempt:
                if colors in temporary_decoding_board:
                    white_pegs += 1
                    temporary_decoding_board.remove(colors)
        self.key_pegs.append(['black']*black_pegs+['white']*white_pegs)

    def play_round(self, codemaker, codebreaker, round):
        print(f"\n Round number {round} starts \n")
        self.set_decoding_board(codemaker)
        for attempt in range(game.number_attempts):
            guessed_attempt = input(f"{codebreaker.upper()}, please guess a sequence of {game.decoding_board_size} colored pegs: ")
            guessed_attempt = guessed_attempt.split()
            guessed_attempt = self.is_attempt_valid(guessed_attempt)            
            self.guessed_list.append(guessed_attempt)
            self.check_key_pegs(guessed_attempt)
            self.display_board()

            if guessed_attempt==self.decoding_board:
                print(f"\n Congratulations {codebreaker.upper()}! You guessed right in {attempt+1} attempts. {attempt} points are added to {codebreaker.upper()} \n")
                break

    def display_score():
        #create function that displays the score
        pass

    def play_game(self):
        for round in range(self.rounds):
            round += 1
            if round % 2 == 1:
                self.codemaker = self.player_one
                self.codebreaker = self.player_two
            else:
                self.codemaker = self.player_two
                self.codebreaker = self.player_one
            self.play_round(self.codemaker, self.codebreaker, round)
            self.
            self.display_score()


player_one_name = input("Please, input Player One's name: ")
player_two_name = input ("Please, input Player Two's name: ")
number_rounds = input("Please, set the total number of rounds to be played: ")
number_rounds = int(number_rounds)

mastermind = game(number_rounds, player_one_name, player_two_name)

mastermind.play_game()
       










