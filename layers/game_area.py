import pyglet
from cocos.sprite import Sprite
from cocos.layer import Layer
from cocos.text import Label
from sprites.block import Block
from cocos.director import director

class Game_Area(Layer):
    def __init__(self):
        Layer.__init__(self)

        self.add(Sprite(image=pyglet.resource.image('game_background.jpg') , position=(self.anchor_x,self.anchor_y)))# Background Image
        
        tmp_block = Block((0,0), '')# para obter as dimencoes da imagem do bloco
        init_pos_x = 224 # meio eixo x da tela
        init_pos_y = tmp_block.height+tmp_block.height/2
        for i in range(23):
            self.add(Block((init_pos_x, init_pos_y+ (i*tmp_block.height)), block_color='gray'))
            self.add(Block((init_pos_x+ (tmp_block.width*17), init_pos_y+ (i*tmp_block.height)), block_color='gray'))
        for i in range(18):
            self.add(Block((init_pos_x+ (i*tmp_block.width),tmp_block.height/2), block_color='gray'))

        