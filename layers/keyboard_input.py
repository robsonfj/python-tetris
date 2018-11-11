
from cocos.layer import Layer

class Keyboard_Input(Layer):
    is_event_handler = True

    def __init__(self):
        super(Keyboard_Input, self).__init__()

    def on_key_press(self, key, modifiers):
        #game_logic.on_key_press(key, modifiers)
        pass

    def on_key_release(self, key, modifiers):
        #game_logic.on_key_release(key, modifiers)
        pass