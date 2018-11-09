import pyglet
from cocos.sprite import Sprite

class Key:
    def __init__(self,position):
        self.pos = position
        self.sprite = Sprite(image=pyglet.resource.image('enter-button.png') , position=self.pos, rotation=0, scale=0.5)
        self.sprite.position = (11,10)
        self.sprite2 = Sprite(image=pyglet.resource.image('keyboard-arrows.png') , position=self.pos, rotation=0, scale=0.5)
        self.sprite2.position = (15,10)