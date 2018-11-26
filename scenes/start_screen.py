import pyglet
import cocos
from cocos.layer import Layer
from cocos.layer import MultiplexLayer
from cocos.layer import ColorLayer
from cocos.scene import Scene
from cocos.menu import Menu
from cocos.menu import MenuItem
from cocos.director import director
from cocos.sprite import Sprite
from cocos.text import Label
#local libs
from layers.ranking import Ranking
from layers.keyboard_input import Keyboard_Input
import game_controller


class Start_Screen(Scene) :
    def __init__(self):
        Scene.__init__(self)
        self.add(Sprite(image=pyglet.resource.image('background.png') , position=(self.anchor_x,self.anchor_y), scale=0.4))# Background Image
        
        black_fade = ColorLayer(0, 0, 0, 0)
        black_fade.opacity = 120
        self.add(black_fade)

        menu = Menu("TETRIS")
        menu.font_title["font_name"] = "Tetrominoes"
        menu.font_title["color"] = (214, 178, 152, 255)
        menu.font_item["font_name"] = "Ravie"
        menu.font_item_selected["font_name"] = "Ravie"
        
        menu_items = [
            MenuItem('Start Game', game_controller.game_controller.init_new_game),
            MenuItem('Ranking', self.show_ranking ),
            MenuItem('Quit', game_controller.game_controller.close_scene )
        ]
        menu.menu_hmargin = 10
        menu.create_menu( menu_items )
        
        menu.on_quit = self.on_quit

        self.menu_lyr = Layer()
        self.menu_lyr.add(menu)
        self.rank = Ranking()
        self.multi_layer = MultiplexLayer(self.menu_lyr, self.rank)
        self.add(self.multi_layer)
        
    def show_ranking(self):
        self.multi_layer.switch_to(1)
        self.rank.show_rank()

    def on_rank_exit(self):
        self.multi_layer.switch_to(0)

    def on_quit(self):# ao pressionar ESC executa este metodo
        game_controller.game_controller.close_scene()

