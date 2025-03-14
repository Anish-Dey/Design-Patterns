from TicTacToe.Model.board import Board
from TicTacToe.Model.player import Player
from TicTacToe.Model.playing_peice_o import PlayingPeiceO
from TicTacToe.Model.playing_peice_x import PlayingPeiceX


class TicTacToe:
    def __init__(self):
        self.player_list = []
        self.board = None
        self.initialize()

    def initialize(self):
        cross_peice = PlayingPeiceX()
        nought_peice = PlayingPeiceO()

        player1 = Player("A", cross_peice)
        player2 = Player("B", nought_peice)

        self.player_list.append(player1)
        self.player_list.append(player2)

        self.board = Board(3)

    def start_game(self):
        noWinner = True
        while noWinner:
            player_turn = self.player_list.pop(0)
            self.board.print_board()

            free_spaces = self.board.find_empty_space()
            if not free_spaces:
                noWinner = False
                continue

            print("Player: ", player_turn.name)
            s = input( " Enter Row, Col")
            row_col_list = s.split(",")
            row = row_col_list[0]
            col = row_col_list[1]

            peicesAddedSuccessfully = self.board.add_peice(row, col, player_turn.get_playing_peice())
            if not peicesAddedSuccessfully:
                print("Incorrect Position Chosen")
                self.player_list.insert(0, player_turn)
                continue

            self.player_list.append(player_turn)
            if self.is_there_winner(row, col, player_turn.get_playing_peice()):
                return player_turn.name

        return "tie"

    def is_there_winner(self, row, col, peice_type):




