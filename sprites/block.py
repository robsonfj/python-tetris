import pyglet
from cocos.sprite import Sprite
import cocos.euclid as eu
import cocos.collision_model as collision_model

def get_img_by_color(color):
    if(color == ''): 
        color = 'gray'
    img_name = color + '.png'
    return pyglet.resource.image(img_name)

class Block(Sprite):
    def __init__(self, position, block_color, b_type="", scale=1):
        self.block_color = block_color
        self.b_type = b_type

        image = get_img_by_color(block_color)
        Sprite.__init__(self,image=image , position=position, rotation=0, scale=scale)
        self.anchor = (self.width/2, self.height/2)

        #retangulo para calculo de colisao
        self.cshape = collision_model.AARectShape(eu.Vector2(self.width/2, self.height/2), self.width/2, self.height/2)