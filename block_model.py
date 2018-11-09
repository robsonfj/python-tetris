import os
import pyglet
from cocos.sprite import Sprite
from cocos.actions.interval_actions import MoveBy

class Block:
    def __init__(self, position, color):
        self.pos = position
        self.color = color
        
        #try:
            #self.blockImg = #colors_path[color]
        #except KeyError:
            #self.blockImg = colors_path["red"] # default color red

        self.sprite = Sprite(image=pyglet.resource.image('red.png') , position=self.pos, rotation=0, scale=0.5)
        action = MoveBy((0,-700), 1)
        
        self.sprite.do(action)



    def setPos(self, position):
        self.pos = position
        self.sprite.position = position
        
