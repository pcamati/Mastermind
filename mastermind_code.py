'''
Terms:
 - codemaker: player who creates the code
 - codebreaker: player who guesses the code
 - decoding_board: set of pins determined by the codemaker (should be the codebreaker, change)
 - code_pegs: the colored pins the codemaker can choose
 - key_pegs: white and black pins providing hints to the codebreaker
'''

import os

class game:

    decoding_board_size = 4
    #for testing purposes gonna set the value to 2
    number_attempts = 2 #12

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
        self.guessed_list = []
        print(f"\n Round number {round+1} starts \n")
        self.set_decoding_board(codemaker)
        os.system('cls')
        for attempt in range(game.number_attempts):
            guessed_attempt = input(f"{codebreaker.upper()}, please guess a sequence of {game.decoding_board_size} colored pegs: ")
            guessed_attempt = guessed_attempt.split()
            guessed_attempt = self.is_attempt_valid(guessed_attempt)            
            self.guessed_list.append(guessed_attempt)
            self.check_key_pegs(guessed_attempt)
            self.display_board()

            if guessed_attempt == self.decoding_board:
                print(f"\n Congratulations {codebreaker.upper()}! You guessed right in {attempt+1} attempts. {attempt} points are added to {codebreaker.upper()} \n")
                break

        if round % 2 == 0:
            self.score_player_one.append(attempt+1)
            self.score_player_two.append(0)
        else:
            self.score_player_one.append(0)
            self.score_player_two.append(attempt+1)          

    # def display_score(self, round):
    #     print("\n Score \n")
    #     print(f"              {self.player_one.upper()}'s score | {self.player_two.upper()}'s score")
    #     print(f"Round {round+1}: {self.score_player_one[round]} | {self.score_player_two[round]}")
    #     print(f"\n ### \n Total: {sum(self.score_player_one)} | {sum(self.score_player_two)}")

    def display_score(self, round):
        print("\n Score \n")
        print(f"              {self.player_one.upper()}'s score | {self.player_two.upper()}'s score")
        for i in range(round+1):
            print(f"Round {i+1}: {self.score_player_one[i]} | {self.score_player_two[i]}")
        print(f"\n ### \n Total: {sum(self.score_player_one)} | {sum(self.score_player_two)}")


    def play_game(self):
        for round in range(self.rounds):
            if round % 2 == 0:
                self.codemaker = self.player_one
                self.codebreaker = self.player_two
            else:
                self.codemaker = self.player_two
                self.codebreaker = self.player_one
            self.play_round(self.codemaker, self.codebreaker, round)
            self.display_score(round)

#message for when the game ends and states who is the winner if any

player_one_name = input("Please, input Player One's name: ")
player_two_name = input ("Please, input Player Two's name: ")
number_rounds = input("Please, set the total number of rounds to be played: ")
number_rounds = int(number_rounds)

mastermind = game(number_rounds, player_one_name, player_two_name)

mastermind.play_game()
       










