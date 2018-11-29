import pyglet
import random
import time
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions import MoveBy
from cocos.actions import RotateBy
from cocos.euclid import Vector2
#local libs
from sprites.block import Block
import game_controller

def getPosition(offset:Vector2, initPos = Vector2()):
    try:
        return initPos + offset
    except:
        return initPos

def sort_new_piece():# sorteia uma peca nova randomicamente
        count = 1
        chosen = random.uniform(1,7)
        random.seed(time.time()+chosen)
        for key, _ in piece_types.items():
            if(count >= round(chosen,0)):
                return key
            count += 1
        return "square"

piece_types = {
    "S"          :[ Vector2(), Vector2(-25, 0), Vector2( 0,25),  Vector2(25,25) ],
    "S_inverted" :[ Vector2(), Vector2(25, 0), Vector2( 0,25), Vector2(-25,25)  ],
    "T"          :[ Vector2(), Vector2(-25, 0), Vector2(25, 0), Vector2( 0,-25) ],
    "L"          :[ Vector2(), Vector2( 0,-25), Vector2( 0,25), Vector2(25,-25) ],
    "L_inverted" :[ Vector2(), Vector2( 0,-25), Vector2( 0,25), Vector2(-25,-25)],
    "I"          :[ Vector2(), Vector2(-25, 0), Vector2( 25, 0), Vector2(50, 0) ],
    "Square"     :[ Vector2(), Vector2(-25, 0), Vector2( 0,25), Vector2(-25,25) ]
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
    def __init__(self, position:Vector2, p_type=None):
        Sprite.__init__(self, pyglet.resource.image("white.png"), opacity=0)
        self.position = position
        self.anchor = Vector2()
        
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
            block = Block(blk_pos, block_color= piece_colors[self.p_type], b_type='Piece')
            self.add(block)
            block.update_cshape_center(blk_pos) # realinha o centro do retangulo de colisao

    def start_fall(self):
        self.is_stopped = False # Quando colidir com um bloco base tem que ser True
        self.schedule_interval(self.do_fall, 0.8)

    def do_fall(self, time_elapsed:int or float): 
        self.move(Vector2(0,-25))

    def stop_fall(self):# retira do processamento a acao de cair
        self.unschedule(self.do_fall)
        if(not self.is_stopped):
            self.is_stopped = True
        
    
    def move(self, amount:Vector2):
        if(self.can_move(amount)):
            action = MoveBy(amount,0)
            self.do(action)
        self.update_blk_cshape()

    def rotate(self):
        if(self.can_rotate(90)):
            action = RotateBy(90,0)
            self.do(action)

        self.update_blk_cshape()

    def can_rotate(self, rotation:int):
        return True

    def can_move(self, amount:Vector2): # verifica se na proxima posicao havera uma colisao com um bloco
        main_game = game_controller.game_controller.main_game   # main game scene
        c_manager = game_controller.game_controller.c_manager # collision manager
        
        for (_,block) in self.children:
            real_blk_pos = self.point_to_world(block.position)
            for obj in c_manager.objs_touching_point(real_blk_pos.x + amount.x, real_blk_pos.y + amount.y):
                if(obj.b_type == "Base_Floor" or obj.b_type == "Base_Block"):
                    if(amount.x == 0 and amount.y != 0):# se a peca colidiu somente com a base de pecas ou chao
                        main_game.piece_must_stop()# tocando o chao ou base de um bloco... para a peca

                if(not obj.b_type == "Piece"):
                    return False
                
        return True

    def update_blk_cshape(self):
        if(len(self.children) <= 0):
            return

        count = 0
        for offset in piece_types[self.p_type]:
            pos = getPosition(offset, self.position)
            pos = self.parent.point_to_local(pos)
            self.children[count][1].update_cshape_center(pos)# reposiciona o retangulo de colisao para refletir a posicao real da peca
            count += 1
            

