from cocos.layer import Layer
from cocos.scene import Scene
from piece_layer import Piece
from help_layer import Keys

class Main_Game(Scene):
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns

        Scene.__init__(self)

        piece = Piece((100,300), "flat")
        self.add(piece)

        piece1 = Piece((100,200), "flat")
        self.add(piece1)

        piece2 = Piece((100,100), "flat")
        self.add(piece2)

        keys_help = Keys((100,100))
        self.add(keys_help)
        
