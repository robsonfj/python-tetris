import pyglet
import random
import time
import copy
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.actions import MoveBy
from cocos.actions import RotateBy
from cocos.euclid import Vector2
#local libs
from sprites.block import Block
import game_controller


pieces_generated = {#dicionario para armazenar quantas de cada peca ja foram inseridas no jogo
    "S":0,
    "S_inverted" :0,
    "T"          :0,
    "L"          :0,
    "L_inverted" :0,
    "I"          :0,
    "Square"     :0}
Pieces = {#dicionario para armazenar a configuracao dos blocos e cores de cada peca
    "S"          :([ Vector2(), Vector2(-25, 0), Vector2( 0,25),  Vector2(25,25) ], "lightblue"),
    "S_inverted" :([ Vector2(), Vector2(25, 0), Vector2( 0,25), Vector2(-25,25)  ], "blue"),
    "T"          :([ Vector2(), Vector2(-25, 0), Vector2(25, 0), Vector2( 0,-25) ], "green"),
    "L"          :([ Vector2(), Vector2( 0,-25), Vector2( 0,25), Vector2(25,-25) ], "red"),
    "L_inverted" :([ Vector2(), Vector2( 0,-25), Vector2( 0,25), Vector2(-25,-25)], "red2"),
    "I"          :([ Vector2(), Vector2(-25, 0), Vector2( 25, 0), Vector2(50, 0) ], "purple"),
    "Square"     :([ Vector2(), Vector2(-25, 0), Vector2( 0,25), Vector2(-25,25) ], "orange")
}


def getPosition(offset:Vector2, initPos = Vector2()):
    try:
        return Vector2(initPos.x + offset.x, initPos.y + offset.y)
    except:
        return initPos


def sort_new_piece():# sorteia uma peca nova randomicamente

        keys = list(Pieces.keys())
        max_num = max(pieces_generated.values())
        count = 0
        for key in Pieces.keys():# remove pecas que ja foram mais usadas, para aumentar "randomicidade"
            if(pieces_generated[key] >=  max_num-3):
                keys.remove(key)
                pieces_generated[key] = pieces_generated[key] >= 10 and 0 or pieces_generated[key]
                count += 1
            if(count >= 2):
                break

        random.shuffle(keys)

        count = 1
        chosen = random.uniform(1,len(keys))
        random.seed(time.time()+chosen)
        for key in keys:
            if(count >= round(chosen,0)):
                pieces_generated[key] += 1
                return key
            count += 1

        pieces_generated["square"] += 1
        return "square"

class Piece(Sprite):
    def __init__(self, position:Vector2, p_type=None):
        Sprite.__init__(self, pyglet.resource.image("block_template.png"), opacity=0)
        self.position = position
        self.anchor = Vector2()
        
        try:
            self.p_type = p_type == None and sort_new_piece() or p_type
            blocks_offsets = Pieces[self.p_type][0] # De acordo com o tipo retorna lista com ofsets dos blocos para formar a peca
        except KeyError:
            self.p_type = "Square" # peca padrao caso valor passado seja incorreto
            blocks_offsets = Pieces[self.p_type][0]
        
        self.is_stopped = True # Booleano para checar se a peca ja parou de cair
        
        # Inicializa os blocos nas posicoes obtidas do dicionario de pecas
        for offset in blocks_offsets:
            blk_pos = getPosition(offset)
            block = Block(blk_pos, block_color= Pieces[self.p_type][1], b_type='Piece')
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

    def can_rotate(self, rotation:int):# verifica se na proxima rotacao havera uma colisao com algum bloco
        c_manager = game_controller.game_controller.c_manager # collision manager

        ghost_piece = copy.copy(self) # cria uma peca fantasma para apricar a rotacao e verificar se eh valida
        ghost_piece.rotation += rotation
        for (_,block) in ghost_piece.children:
            real_blk_pos = ghost_piece.point_to_world(block.position)# obtem a posicao do bloco real
            real_blk_pos = ghost_piece.parent.point_to_local(real_blk_pos)# obtem a posicao do bloco na layer da peca
            for obj in c_manager.objs_touching_point(real_blk_pos.x, real_blk_pos.y):
                if(not obj.b_type == "Piece"):
                    return False
        return True

    def can_move(self, amount:Vector2): # verifica se na proxima posicao havera uma colisao com algum bloco
        main_game = game_controller.game_controller.main_game   # main game scene
        c_manager = game_controller.game_controller.c_manager # collision manager
        
        for (_,block) in self.children:
            real_blk_pos = self.point_to_world(block.position)
            real_blk_pos = self.parent.point_to_local(real_blk_pos)
            for obj in c_manager.objs_touching_point(real_blk_pos.x + amount.x, real_blk_pos.y + amount.y):
                if(obj.b_type == "Base_Floor" or obj.b_type == "Base_Block"):
                    if(amount.x == 0 and amount.y != 0):# se a peca colidiu somente com a base de pecas ou chao
                        main_game.piece_must_stop()# tocando o chao ou base de um bloco... para a peca

                if(not obj.b_type == "Piece"):
                    return False
                
        return True

    def update_blk_cshape(self):#atualiza os retangulos de colisao dos blocos para a ultima posicao conhecida
        for (_,block) in self.children:
            pos = self.point_to_world(block.position)# obtem a posicao do bloco real
            pos = self.parent.point_to_local(pos)# obtem a posicao do bloco na layer da peca
            block.update_cshape_center(pos)# reposiciona o retangulo de colisao para refletir a posicao real da peca
            

