from sprites.block import Block
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions.interval_actions import MoveBy
import pyglet
piece_types = {"S":[[0,1,1,0],
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
piece_colors = {
    "S":            "lightblue",
    "S_inverted":   "blue",
    "T":            "green",
    "L":            "red",
    "L_inverted":   "red2",
    "I":            "purple",
    "Square":       "orange"
}

class Piece(Layer):
    def __init__(self, position, p_type):
        Layer.__init__(self)
        try:
            self.p_type = p_type
            build_matrix = piece_types[self.p_type] 
        except KeyError:
            self.p_type = "Square" # peca padrao caso valor passado seja incorreto
            build_matrix = piece_types[self.p_type]

        self.position = position 
        self.anchor = (0,0)
    
        self.blocks = []
        first_block = Block((0,0), block_color= piece_colors[self.p_type])
        self.add(first_block)
        self.blocks.append(first_block)

        i = 1
        for j_array in build_matrix:
            j = 1
            for value in j_array:
                if(i == j and i == 2):
                    j += 1
                    continue
                if(value == 1):
                    x = 0
                    y = 0
                    # coloca os blocos nas posicoes corretas de acordo com a matriz 4x4
                    if(i < 2):
                        y += first_block.height
                    if(i > 2):
                        y -= first_block.height*(i-2)

                    if(j < 2):
                        x -= first_block.width 
                    if(j > 2):
                        x += first_block.width*(j-2)

                    block = Block((x,y), block_color= piece_colors[self.p_type])
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