from TicTacToe.Model.playing_peice import PlayingPeice


class Player:
    def __init__(self, name, playing_peice: PlayingPeice):
        self.name = name
        self.playing_peice = playing_peice

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_playing_peice(self):
        return self.playing_peice.peice_type

    def set_playing_peice(self, playing_peice: PlayingPeice):
        self.playing_peice = playing_peice