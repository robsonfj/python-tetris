from block_sprite import Block
from cocos.layer import Layer
from cocos.actions.interval_actions import MoveBy

matrixes_by_piece = {"S":[[0,1,1,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
            "S_inverted":[[1,1,0,0],
                          [0,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                     "T":[[1,1,1,0],
                          [0,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                     "L":[[1,0,0,0],
                          [1,0,0,0],
                          [1,1,0,0],
                          [0,0,0,0]],
            "L_inverted":[[0,1,0,0],
                          [0,1,0,0],
                          [1,1,0,0],
                          [0,0,0,0]],
                     "I":[[1,1,1,1],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                "Square":[[1,1,0,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]]
}

class Piece(Layer):
    def __init__(self, position, p_type):
        Layer.__init__(self)

        try:
            self.p_type = p_type
            self.p_matrix = matrixes_by_piece[p_type] 
        except KeyError:
            self.p_matrix = matrixes_by_piece["Square"]

        self.position = position        
        tmp_block = Block((0,0), chosen_color='gray')

        self.add(Block(position, chosen_color='red'))
        self.add(Block((position[0]+tmp_block.width, position[1]), chosen_color='red'))
        self.add(Block((position[0]+tmp_block.width, position[1]+tmp_block.height), chosen_color='red'))
        self.add(Block((position[0]+(tmp_block.width*2), position[1]+tmp_block.height), chosen_color='red'))

        action = MoveBy((0,-700), 1)
        self.do(action)