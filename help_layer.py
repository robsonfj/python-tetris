import pyglet
from cocos.sprite import Sprite
from cocos.layer import Layer
from cocos.text import Label

class Keys(Layer):
    def __init__(self,position):
        Layer.__init__(self)
        arrows = Sprite(image=pyglet.resource.image('keyboard-arrows.png') , position=position, scale=0.4)
        arrows.position = position
        enter = Sprite(image=pyglet.resource.image('enter-button.png') , position=position, scale=0.2)
        enter.position = (position[0]+ arrows.width + 20, position[1] + arrows.height + 40)
        label_enter = Label("Girar peca", position=(enter.position[0] + enter.width + 5, enter.position[1]), font_name="Tetrominoes")
        label_arrow_down = Label("Acelerar peca para baixo", position=(arrows.position[0] , arrows.position[1]))
        label_arrow_left = Label("Mover para esquerda", position=(arrows.position[0] , arrows.position[1]))
        label_arrow_right = Label("Mover para direita", position=(arrows.position[0] , arrows.position[1]))
        
        self.add(label_enter)
        self.add(label_arrow_down)
        self.add(label_arrow_left)
        self.add(label_arrow_right)
        self.add(arrows)
        self.add(enter)

        