
from cocos.layer import Layer
import game_controller

class Keyboard_Input(Layer):
    is_event_handler = True

    def __init__(self):
        super(Keyboard_Input, self).__init__()

    def on_key_press(self, key, modifiers):
        game_controller.game_controller.on_key_press(key, modifiers)
        
    def on_key_release(self, key, modifiers):
        game_controller.game_controller.on_key_release(key, modifiers)
        