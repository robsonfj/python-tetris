import pyglet
import random
import time
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions import MoveBy
from cocos.actions import RotateBy
from sprites.block import Block
import game_controller

def getPosition(offset, initPos = (0,0)):
    try:
        return (initPos[0] + offset[0], initPos[1] + offset[1])
    except:
        return initPos

def sort_new_piece():# sorteia uma peca nova randomicamente
        count = 1
        chosen = round(random.uniform(1, len(piece_types.keys())), 0)
        time.sleep(random.uniform(0,1))
        random.seed(time.time())
        for key, _ in piece_types.items():
            if(count >= chosen):
                return key
            count += 1
        return "square"

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
    def __init__(self, position, p_type=None):
        Sprite.__init__(self, pyglet.resource.image("white.png"), opacity=0)
        self.position = position
        self.anchor = (0,0)

        try:
            self.p_type = p_type == None and sort_new_piece() or p_type
            blocks_offsets = piece_types[self.p_type] # De acordo com o tipo retorna lista com ofsets dos blocos para formar a peca
        except KeyError:
            self.p_type = "Square" # peca padrao caso valor passado seja incorreto
            blocks_offsets = piece_types[self.p_type]
        
        self.is_stopped = True # Booleano para checar se a peca ja parou de cair
        
        # Inicializa os blocos nas posicoes obtidas do dicionario de pecas
        for offset in blocks_offsets:
            blk_pos = getPosition(offset)
            block = Block(blk_pos, block_color= piece_colors[self.p_type], b_type='Piece', scale=0.4)
            self.add(block)
            block.set_cshape_center(getPosition(offset, self.position)) # realinha o centro do retangulo de colisao

    def start_fall(self):
        self.is_stopped = False # Quando colidir com um bloco base tem que ser True
        self.schedule_interval(self.do_fall, 0.8)

    def do_fall(self, time_elapsed):        
        action = MoveBy((0,-25),0)
        self.do(action)
        self.update_blocks()

    def stop_fall(self):# retira do processamento a acao de cair
        try:
            self.unschedule(self.do_fall)
            if(not self.is_stopped):
                self.is_stopped = True

        except AttributeError as e:
            print("Error! Piece stop_fall -", e)
        
    
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
            rel_pos = self.point_to_world(block.position)
            block.set_cshape_center( rel_pos) # reposiciona o retangulo de colisao para refletir a posicao real da peca
            count += 1

