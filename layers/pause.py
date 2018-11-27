import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.layer import ColorLayer
from cocos.menu import Menu
from cocos.menu import MenuItem
#local libs
import game_controller

''' 
Pause uma layer para lidar com o stado pausado do jogo
'''
class Pause(Layer):
    def __init__(self):
        return super().__init__()