class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep a 3*3 board
        self.current_winner = None # Keep track of winner

    def print_board(self):
        # This is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row)+ ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 | ets (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+ ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_square(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X' # Starting letter
    """
    Iterate while game still has empty squares
    (We won't have to worry about winner because we'll just return that 
    which breaks the loop)
    """
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)