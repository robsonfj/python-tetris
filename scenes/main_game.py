import cocos
from cocos.layer import Layer
from cocos.scene import Scene
from sprites.block import Block
from layers.keyboard_input import Keyboard_Input
from layers.game_area import Game_Area

class Main_Game(Scene):
    is_event_handler = True
    def __init__(self):
        self.anchor = (0,0)
        self.position = (0,0)
        Scene.__init__(self)
        self.add(Game_Area())
        self.add(Keyboard_Input()) # adiciona layer para obter imput do teclado
        
        
    def on_key_press(self, key, modifiers):
        print(key)