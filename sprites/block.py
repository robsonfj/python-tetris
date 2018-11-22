import pyglet
from cocos.sprite import Sprite


def get_img_by_color(color):
    if(color == ''): 
        color = 'gray'
    img_name = color + '.png'
    return pyglet.resource.image(img_name)

class Block(Sprite):
    def __init__(self, position, block_color):
        self.block_color = block_color
        
        image = get_img_by_color(block_color)
        Sprite.__init__(self,image=image , position=position, rotation=0, scale=0.4)
        
