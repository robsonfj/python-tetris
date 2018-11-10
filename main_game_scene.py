from cocos.layer import Layer
from cocos.scene import Scene
from piece_layer import Piece
from block_sprite import Block
from help_layer import Keys

class Main_Game(Scene):
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns

        Scene.__init__(self)

        piece = Piece((200,300), "flat")
        self.add(piece)

        piece1 = Piece((200,200), "flat")
        self.add(piece1)

        piece2 = Piece((200,100), "flat")
        self.add(piece2)

        keys_help = Keys((200,100))
        self.add(keys_help)

        

        border_layer = Layer()
        init_pos_x = 200
        init_pos_y = 16
        tmp_block = Block((0,0), chosen_color='gray')
        for i in range(16):
            border_layer.add(Block((init_pos_x+ (i*tmp_block.width),16), chosen_color='gray'))
        for i in range(20):
            border_layer.add(Block((init_pos_x, init_pos_y+ (i*tmp_block.height)), chosen_color='gray'))
            border_layer.add(Block((init_pos_x+ (tmp_block.width*16), init_pos_y+ (i*tmp_block.height)), chosen_color='gray'))

        self.add(border_layer, z=1)
        
        
