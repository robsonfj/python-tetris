import os
import pyglet
from cocos.sprite import Sprite

def get_img_by_color(color):
    return pyglet.resource.image('red.png')

class Block(Sprite):
    def __init__(self, position, color):
        self.chosen_color = color
        
        image = get_img_by_color(self.color)
        Sprite.__init__(self,image=image , position=position, rotation=0, scale=0.5)
        
