import pyglet
import cocos
from cocos.euclid import Vector2
from cocos.director import director
from cocos.collision_model import CollisionManagerGrid
from cocos.sprite import Sprite
from cocos.layer import Layer
from cocos.text import Label
from sprites.block import Block
import game_controller

class Wall_Rect():
     def __init__(self, x, width, y, height, b_type):
         self.x = x
         self.width = width
         self.y = y
         self.height = height
         self.b_type = b_type
         self.cshape = cocos.collision_model.AARectShape(Vector2(x + width/2, y + height/2), width/2, height/2)


class Wall_Limits(Layer):
    def __init__(self):
        Layer.__init__(self)

        self.add(Sprite(image=pyglet.resource.image('game_background.jpg') , position=(self.anchor_x,self.anchor_y)))# Background Image

        self.scoreLabel = Label("0",position=(880,350),font_name = "Ravie", align = "center",anchor_x = "center")# texto onde mostra o score atual
        self.add(self.scoreLabel)

        self.game_controller = game_controller.game_controller
        self.c_manager =  self.game_controller.c_manager# obtem instancia do gerenciador de colisao

        scale = 0.4
        tmp_block = Block((0,0), '', scale=scale)# para obter as dimencoes da imagem do bloco
        init_pos_x = 224 # meio eixo x da tela
        init_pos_y = tmp_block.height+tmp_block.height/2
        
        for i in range(23):
            blk = Block((init_pos_x, init_pos_y+ (i*tmp_block.height)), block_color='gray', scale=scale, b_type="LeftWall")
            self.add(blk)
            #self.c_manager.add(blk)

            blk = Block((init_pos_x+ (tmp_block.width*17), init_pos_y+ (i*tmp_block.height)), block_color='gray', scale=scale, b_type="RightWall")
            self.add(blk)
            #self.c_manager.add(blk)
        self.c_manager.add(Wall_Rect(init_pos_x+tmp_block.width/2, tmp_block.width, init_pos_y+tmp_block.height/2, 23*tmp_block.height, b_type="LeftWall"))
        self.c_manager.add(Wall_Rect(init_pos_x+tmp_block.width/2 + (tmp_block.width*15), tmp_block.width, init_pos_y, 23*tmp_block.height, b_type="RightWall"))

        for i in range(18):
            blk = Block((init_pos_x+ (i*tmp_block.width),tmp_block.height/2), block_color='gray',scale=scale, b_type="Base")
            self.add(blk)
            #self.c_manager.add(blk)
        self.c_manager.add(Wall_Rect(init_pos_x+tmp_block.width/2, 18*tmp_block.width, init_pos_y+tmp_block.height/2, tmp_block.height, b_type="Base"))


    def update_score(self, score):# atualiza o label mostrando o score
        try:
            self.scoreLabel.element.text = str(score)
        except:
            self.scoreLabel.element.text = "0"
        
        