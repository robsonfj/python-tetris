import pyglet
from cocos.sprite import Sprite
from cocos.euclid import Vector2
from cocos import collision_model
from cocos.layer import ColorLayer

def get_img_by_color(color):
    if(color == ''): 
        color = 'block_template'
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
            pos = self.point_to_world((self.x-self.width/2, self.y-self.height/2))
            self.cshape = collision_model.AARectShape( pos , self.width/2, self.height/2)
            self.color_col = ColorLayer(255,0,255,255, int(self.width), int(self.height))
            self.color_col.position = self.cshape.center
            self.add(self.color_col,z=10)

    def update_cshape_center(self, vector):
        pos = (vector.x-self.width/2, vector.y-self.height/2)
        self.cshape.rx = self.width/2
        self.cshape.ry = self.height/2
        self.cshape.center = pos
        self.color_col.position = pos
        self.color_col.width = self.width/2
        self.color_col.height= self.height/2