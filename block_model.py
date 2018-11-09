import os
import pyglet
import pathlib
from cocos.sprite import Sprite
from cocos.actions.interval_actions import MoveBy

block_img_path = pathlib.Path('./assets/blocks')

colors_path = {"blue":os.path.join(block_img_path,"blue.png"),
               "darkgray":os.path.join(block_img_path,"darkgray.png"),
               "gray":os.path.join(block_img_path,"gray.png"),
               "green":os.path.join(block_img_path,"green.png"),
               "lightblue":os.path.join(block_img_path,"lightblue.png"),
               "orange":os.path.join(block_img_path,"orange.png"),
               "pink":os.path.join(block_img_path,"pink.png"),
               "purple":os.path.join(block_img_path,"purple.png"),
               "red":block_img_path/"red.png",
               "red2":os.path.join(block_img_path,"red2.png"),
               "white":os.path.join(block_img_path,"white.png")
             }

class Block:
    def __init__(self, position, color):
        self.pos = position
        self.color = color
        
        try:
            self.blockImg = colors_path[color]
        except KeyError:
            self.blockImg = colors_path["red"] # default color red

        self.sprite = Sprite(image=pyglet.resource.image('red.png'), position=self.pos, rotation=0, scale=0.5)
        action = MoveBy((0,-700), 1)
        
        self.sprite.do(action)
        

    def setPos(self, position):
        self.pos = position
        self.sprite.position = position
        
