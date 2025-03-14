from TicTacToe.Model.playing_peice import PlayingPeice


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_peice(self, row: int, col: int, playing_peice: PlayingPeice):
        if self.board[row][col]: return False
        self.board[row][col] = playing_peice
        return True

    def find_empty_space(self):
        empty_space_list = []
        for i in range(self.size):
            for j in range(self.size):
                if not self.board[i][j]:
                    empty_space_list.append([i,j])

        return empty_space_list

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]: print(self.board[i][j].peice_type, " ")
                else: print("  ")
                print("|")

        print()