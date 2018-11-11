from sprites.block import Block
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions.interval_actions import MoveBy
import pyglet
matrixes_by_piece = {"S":[[0,1,1,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
            "S_inverted":[[1,1,0,0],
                          [0,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                     "T":[[0,0,0,0],
                          [1,1,1,0],
                          [0,1,0,0],
                          [0,0,0,0]],
                     "L":[[0,1,0,0],
                          [0,1,0,0],
                          [0,1,1,0],
                          [0,0,0,0]],
            "L_inverted":[[0,1,0,0],
                          [0,1,0,0],
                          [1,1,0,0],
                          [0,0,0,0]],
                     "I":[[0,0,0,0],
                          [1,1,1,1],
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
        first_block = Block(position, block_color='red')
        self.blk_width = first_block.width
        self.blk_height = first_block.height
        self.blocks = []
        self.blocks.append(first_block)
        self.blocks.append(Block((position[0]+first_block.width, position[1]), block_color='red'))
        self.blocks.append(Block((position[0]+first_block.width, position[1]+first_block.height), block_color='red'))
        self.blocks.append(Block((position[0]+(first_block.width*2), position[1]+first_block.height), block_color='red'))

    #def start_fall(self):
        #self.schedule_interval(self.move_piece_down,1)

    #def stop_fall(self):
        #self.schedule_interval(self.move_piece_down,0)
        
    #def move_piece_down(self):
        #self.y -= self.blk_height