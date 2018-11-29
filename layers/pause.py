import cocos
from pyglet.window.key import symbol_string
from cocos.director import director
from cocos.layer import Layer
from cocos.layer import MultiplexLayer
from cocos.layer import ColorLayer
from cocos.menu import Menu
from cocos.menu import MenuItem
from cocos.euclid import Vector2
#local libs
import game_controller

''' 
Pause uma layer para lidar com o stado pausado do jogo
'''
class Pause(Layer):
    def __init__(self):
        Layer.__init__(self)

        menu = Menu("")
        menu_items = []

        black_lyr = ColorLayer(0, 0, 0,0)
        self.add(black_lyr)
        black_lyr.width = int(director.window.width)
        black_lyr.height = int(director.window.height)
        black_lyr.position = (0, 0)
        black_lyr.opacity = 140

        item = MenuItem('Continuar', self.on_quit)
        menu_items.append(item)
        menu.position = ( 0, -120)
        item.position = ( 0, 150)
        menu.font_title["font_name"] = "Tetrominoes"
        menu.font_title["color"] = (214, 178, 152, 255)
        menu.font_item["font_name"] = "Ravie"
        menu.font_item["font_size"] = 19
        menu.font_item_selected["font_name"] = "Ravie"
        menu.font_item_selected["font_size"] = 22
        menu.title = "PAUSADO"

        menu.create_menu( menu_items )
        menu.on_quit = self.on_quit
        
        self.add(menu)

    def on_quit(self):# ao pressionar ESC executa este metodo
        if(type(self.parent) == MultiplexLayer):
            self.parent.parent.on_unpause()

    def on_enter(self):
        return super().on_enter()

    def on_exit(self):
        return super().on_exit()