from TicTacToe.Model.piece_type import PeiceType
from TicTacToe.Model.playing_peice import PlayingPeice


class PlayingPeiceO(PlayingPeice):
    def __init__(self):
        super().__init__(PeiceType.O)