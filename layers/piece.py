from sprites.block import Block
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions import MoveBy
from cocos.actions import RotateBy
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

        self.is_stopped = True

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

    def start_fall(self):
        self.is_stopped = False
        self.schedule_interval(self.do_fall, 1.2)

    def do_fall(self, time_elapsed):
        print("x-",self.x)
        print("y-",self.y)
        if(self.y >= 50 or self.is_stopped):
            action = MoveBy((0,-25),0)
            self.do(action)

    def stop_fall(self):
        self.unschedule(self.do_fall)
    
    def move(self, amount):
        action = MoveBy(amount,0)
        self.do(action)

    def rotate(self):
        action = RotateBy(90,0)
        self.do(action)

    def retrieve_blocks(self):
        pass
        