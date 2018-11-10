import pyglet
from cocos.sprite import Sprite
from cocos.layer import Layer
from cocos.text import Label

class Keys(Layer):
    def __init__(self,position):
        Layer.__init__(self)
        arrows = Sprite(image=pyglet.resource.image('all-keys.png') , position=position, scale=0.5)
        arrows.position = (position[0]+ arrows.width + 500, position[1] + arrows.height + -60)
        label_enter = Label("GIRAR PECA", position=(arrows.position[0] + arrows.width + -220, arrows.position[1] + arrows.height + -7), font_name="Tetrominoes", bold=True)
        label_arrow_down = Label("Acelerar peca para baixo", position=(arrows.position[0] + arrows.width -270 , arrows.position[1] + arrows.height + -170), font_name="Tetrominoes", bold=True)
        label_arrow_left = Label("Mover para esquerda", position=(arrows.position[0] , arrows.position[1]), font_name="Tetrominoes", bold=True)
        label_arrow_right = Label("Mover para direita", position=(arrows.position[0] , arrows.position[1]), font_name="Tetrominoes", bold=True)
        
        self.add(label_enter)
        self.add(label_arrow_down)
        self.add(label_arrow_left)
        self.add(label_arrow_right)
        self.add(arrows)


        