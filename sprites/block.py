import pyglet
from cocos.sprite import Sprite
from cocos.euclid import Vector2
from cocos import collision_model
from cocos.layer import ColorLayer
import game_controller

def get_img_by_color(color):
    if(color == ''): 
        color = 'block_template'
    img_name = color + '.png'
    return pyglet.resource.image(img_name)

class Block(Sprite):
    def __init__(self, position:Vector2, block_color, scale=1, b_type = ""):
        self.block_color = block_color
        self.b_type = b_type

        image = get_img_by_color(block_color)
        Sprite.__init__(self,image=image , position=position, scale=scale)
        
        if(not b_type == ''):
            #retangulo para calculo de colisao, como coodenadas realtivas a layer do jogo principal
            pos = game_controller.game_controller.main_game.point_to_local((self.x, self.y))
            self.cshape = collision_model.AARectShape( pos , self.width/2, self.height/2)
            self.color_col = ColorLayer(255,0,255,255, int(self.width), int(self.height))
            self.color_col.position = (self.cshape.center.x - self.width/2, self.cshape.center.y - self.height/2)
            #game_controller.game_controller.main_game.add(self.color_col,z=1)#TODO REMOVER blocos para avaliacao de colisao

    def update_cshape_center(self, vector:Vector2):
        self.cshape.center = vector
        self.color_col.position =(vector.x-self.width/2, vector.y-self.height/2)
        self.color_col.width = int(self.width)
        self.color_col.height= int(self.width)