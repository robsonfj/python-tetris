import pyglet
import cocos
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.menu import MenuItem
from cocos.director import director
from cocos.sprite import Sprite
from cocos.text import Label
import game_controller
from layers.ranking import Ranking


class Menu(Scene) :
    def __init__(self):
        Scene.__init__(self)

        self.add(Sprite(image=pyglet.resource.image('background.jpg') , position=(self.anchor_x,self.anchor_y), opacity=85))# Background Image

        menu = cocos.menu.Menu("TETRIS")
        menu.font_title["font_name"] = "Tetrominoes"
        menu.font_title["color"] = (214, 178, 152, 255)
        menu.font_item["font_name"] = "Ravie"
        menu.font_item_selected["font_name"] = "Ravie"
        
        menu_items = [
            MenuItem('Start Game', game_controller.game_controller.init_new_game),
            MenuItem('Ranking', self.show_ranking ),
            MenuItem('Options', None ),
            MenuItem('Quit', game_controller.game_controller.close_scene )
        ]

        menu.create_menu( menu_items )
        layer = Layer()
        layer.add(menu)
        self.add(layer)
        
    def show_ranking(self):
        self.add(Ranking())

    def on_enter(self):
        director.push_handlers(self.on_cocos_resize)
        super(Menu, self).on_enter()

    def on_quit(self):
        return super(Menu, self).on_exit()

    def on_cocos_resize(self, usable_width, usable_height):
        pass
