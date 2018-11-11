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
        self.anchor = position

        self.blocks = []

        first_block = Block(position, block_color='red')
        self.add(first_block)
        i = 1
        for j_array in self.p_matrix:
            j = 1
            for value in j_array:
                if(i == j and i == 2):
                    continue
                if(value == 1):
                    x = position[0]
                    y = position[1]
                    if(i < 2):
                        x -= first_block.width 
                    if(i > 2):
                        x += first_block.width*(i-2)

                    if(j < 2):
                        y += first_block.height
                    if(j > 2):
                        y -= first_block.height*(j-2)
                    print(i,',',j,'-', value)
                    print(x,',',y)
                    block = Block((x,y), block_color='red')
                    self.blocks.append(block)
                    self.add(block)
                
                j += 1
            i += 1

    #def start_fall(self):
        #self.schedule_interval(self.move_piece_down,1)

    #def stop_fall(self):
        #self.schedule_interval(self.move_piece_down,0)
        
    #def move_piece_down(self):
        #self.y -= self.blk_height