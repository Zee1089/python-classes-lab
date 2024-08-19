#welcome message at the start of a game
#printed board game
#check which turn is it
#prompted to enter a move and be provided an example of valid input : Enter a valid move 
#enter my moves in upper or lower cases
# invalid format or occupied cell ==> message chastising me and be reprompeted 
# after move, updated mgame board , notifiy or turn, ask to enter a move until smoene win or tie
#message at the end of the game indicating winner or Tie 

class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board =  {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
                    Tic   Tac   Toe
          _________________________________
                        {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                        ----------
                        {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                        ----------
                        {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
            ________________________________
         """)

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid movie (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("invalid move! Please try again!")
                
    def print_message(self):
        if self.tie:
            print("Tie Game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")


    def check_winner(self):
        winning_combinations = [
            ('a1', 'b1', 'c1'),  
            ('a2', 'b2', 'c2'),  
            ('a3', 'b3', 'c3'),  
            ('a1', 'a2', 'a3'),  
            ('b1', 'b2', 'b3'),  
            ('c1', 'c2', 'c3'),  
            ('a1', 'b2', 'c3'),  
            ('c1', 'b2', 'a3')   
        ]

        for win in winning_combinations:
            if self.board[win[0]] == self.board[win[1]] == self.board[win[2]] and self.board[win[0]] is not None:
                self.winner = self.board[win[0]]
                return
        
    def check_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True

    def switching_turns(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_winner()
            self.check_tie()
            if not self.winner and not self.tie:
                self.switching_turns()

        self.render()

game_instance = Game()
game_instance.play_game()


