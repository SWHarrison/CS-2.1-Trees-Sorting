class gameBoard:

    def __init__(self, size = 5, pieces = 2):

        self.board = []
        for rows in range(size):
            new_row = []
            for columns in range(size):
                new_row.append(" ")


        self.player1_pieces = player_pieces(size,1)
        self.player2_pieces = player_pieces(size,2)

        for piece in self.player1_pieces
            self.board[piece[0]][piece[1]] = "1"
        for piece in self.player2_pieces:
            self.board[piece[0]][piece[1]] = "2"

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        to_return = "-" * len(self.board) + "\n"
        for r in range(len(self.board)):
            to_return += "|"
            for c in range(len(self.board)):
                to_return += self.board[r][c] + "|"
            to_return += "\n" + "-" * len(self.board)

        return to_return


    def all_available_moves(player_num):

        pieces = None
        if(player_num == 1):
            pieces = self.player1_pieces
        else:
            pieces = self.player2_pieces

        moves = []
        for piece in pieces:
            moves.append(self.piece_moves(piece))

    def piece_moves(piece):

        if board[piece[0]][piece[1]] == " ":
            #Raise ValueError
            print("ERROR")
            return

        moves = []
        current_loc = [piece[0],piece[1]]
        current_loc[1] += 1

        # up moves
        while current_loc[1] < len(self.board) and board[current_loc[0]][current_loc[1]] == " ":
            moves.append(current_loc)
            current_loc[1] += 1

        current_loc = [piece[0],piece[1]]
        current_loc[1] -= 1

        # down moves
        while current_loc[1] >= 0 and board[current_loc[0]][current_loc[1]] == " ":
            moves.append(current_loc)
            current_loc[1] -= 1

        current_loc = [piece[0],piece[1]]
        current_loc[0] -= 1

        # left moves
        while current_loc[0] >= 0 and board[current_loc[0]][current_loc[1]] == " ":
            moves.append(current_loc)
            current_loc[0] -= 1

        current_loc = [piece[0],piece[1]]
        current_loc[0] += 1

        # right moves
        while current_loc[0] < len(self.board) and board[current_loc[0]][current_loc[1]] == " ":
            moves.append(current_loc)
            current_loc[0] += 1

        return moves


class player_pieces:

    def __init__(self,size,player_num,pieces = 2):

        self.player_pieces
        if(player_num == 1):
            self.player_pieces = [[0,0],[0,size-1]]
        else:
            self.player_pieces = [[size-1,0],[size-1,size-1]]

if __name__ == '__main__':

    game = gameBoard()
    print(game)
