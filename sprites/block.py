import pyglet
from cocos.sprite import Sprite
from cocos.euclid import Vector2
from cocos import collision_model

def get_img_by_color(color):
    if(color == ''): 
        color = 'gray'
    img_name = color + '.png'
    return pyglet.resource.image(img_name)

class Block(Sprite):
    def __init__(self, position, block_color, scale=1, b_type = ""):
        self.block_color = block_color
        self.b_type = b_type

        image = get_img_by_color(block_color)
        Sprite.__init__(self,image=image , position=position, scale=scale)
        self.anchor = (self.width/2, self.height/2)
        
        if(not b_type == ''):
            #retangulo para calculo de colisao
            self.cshape = collision_model.AARectShape(Vector2(self.x + self.anchor[0], self.y + self.anchor[1]), self.width/2, self.height/2)

    def set_cshape_center(self, center):
        self.cshape.center = Vector2(center[0], center[1])