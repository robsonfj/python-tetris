import pyglet
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions import MoveBy
from cocos.actions import RotateBy
from sprites.block import Block

def getPosition(offset, initPos = (0,0)):
    try:
        return (initPos[0] + offset[0], initPos[1] + offset[1])
    except:
        return initPos

piece_types = {
    "S"          :[ (0,0), (-25, 0), ( 0,25),  (25,25) ],
    "S_inverted" :[ (0,0), (25, 0), ( 0,25), (-25,25)  ],
    "T"          :[ (0,0), (-25, 0), (25, 0), ( 0,-25) ],
    "L"          :[ (0,0), ( 0,-25), ( 0,25), (25,-25) ],
    "L_inverted" :[ (0,0), ( 0,-25), ( 0,25), (-25,-25)],
    "I"          :[ (0,0), (-25, 0), ( 25, 0), (50, 0) ],
    "Square"     :[ (0,0), (-25, 0), ( 0,25), (-25,25) ]
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

class Piece(Sprite):
    def __init__(self, position, p_type):
        Sprite.__init__(self, pyglet.resource.image("white.png"), opacity=0)
        try:
            self.p_type = p_type
            blocks_offsets = piece_types[self.p_type]
        except KeyError:
            self.p_type = "Square" # peca padrao caso valor passado seja incorreto
            blocks_offsets = piece_types[self.p_type]
        
        self.is_stopped = True
        self.position = position

        #inicializa os blocos nas posicoes obtidas do dicionario de pecas
        for offset in blocks_offsets:
            blk_pos = getPosition(offset)
            block = Block(blk_pos, block_color= piece_colors[self.p_type], b_type='Piece', scale=0.4)
            self.add(block)
            block.set_cshape_center(getPosition(offset, self.position)) # realinha o centro do retangulo de colisao

    def start_fall(self):
        self.is_stopped = False
        self.schedule_interval(self.do_fall, 1)

    def do_fall(self, time_elapsed):
        print("x-",self.x)
        print("y-",self.y)
        
        action = MoveBy((0,-25),0)
        self.do(action)

    def stop_fall(self):
        try:
            self.unschedule(self.do_fall)
            self.parent.currentScore += 15
            self.parent.wall_limits.update_score(self.currentScore) 
        except:
            print("Error! Piece stop_fall")
        
    
    def move(self, amount):
        action = MoveBy(amount,0)
        self.do(action)
        self.update_blocks()

    def rotate(self):
        action = RotateBy(90,0)
        self.do(action)
        self.update_blocks()

    def update_blocks(self):
        count = 0
        for (_,block) in self.children :
            offset = piece_types[self.p_type][count]
            block.set_cshape_center(getPosition(offset, self.position)) # realinha o centro do retangulo de colisao
            count += 1

