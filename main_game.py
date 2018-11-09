from cocos.layer import Layer
from cocos.scene import Scene
from piece_model import Piece

class Main_Game:
    def __init__(self, director, lines, columns):
        self.game_director = director
        self.lines = lines
        self.columns = columns
        self.layer = Layer()
        self.scene = Scene(self.layer)
        
        piece = Piece((400,600), "flat")
        self.scene.add(piece.layer)

        piece = Piece((400,900), "flat")
        self.scene.add(piece.layer)

        piece = Piece((400,1200), "flat")
        self.scene.add(piece.layer)
        
