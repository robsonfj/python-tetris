from cocos.layer import Layer
from cocos.scene import Scene
from cocos.menu import MenuItem
from main_game_scene import Main_Game
from cocos.director import director
import cocos

class Menu(Scene) :
    def __init__(self):
        Scene.__init__(self)
        menu = cocos.menu.Menu("Menu")
        
        menu_items = []
        menu_items.append( MenuItem('Start Game', self.menu_opt_start) )
        menu_items.append( MenuItem('Options', None ) )
        menu_items.append( MenuItem('Quit', director.pop ) )

        menu.create_menu( menu_items )
        layer = Layer()
        layer.add(menu)
        self.add(layer)
        
    
    def menu_opt_start(self):
        main_game = Main_Game(20,10)
        director.push(main_game)
    
    def on_enter(self):
        director.push_handlers(self.on_cocos_resize)
        super(Menu, self).on_enter()

    def on_cocos_resize(self, usable_width, usable_height):
        pass

# Layer = cocos.layer.Layer
# Scene = cocos.scene.Scene
# Sprite = cocos.sprite.Sprite
# director = cocos.director.director
# Menu = cocos.menu.Menu
# MenuItem = cocos.menu.MenuItem

# director.init(width=window_witdh, height=window_heigth, caption="Hello World", fullscreen=False)

# # glEnable(GL_TEXTURE_2D)
# # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

# layer = Layer()
# scene = Scene(layer)
# sprite = Sprite(pyglet.resource.image("demon.png"), position=(window_witdh/4, window_heigth/4))
# layer.add(sprite)
# layer.is_event_handler =True


# def enter():
#     print ("hahahahah")
#     layer.position =  (100, 100)
            
    
 
# l = []
# l.append( MenuItem('Start', enter ) )
# l.append( MenuItem('Options', None ) )
# l.append( MenuItem('Quit', exit,0 ) )
# menu = Menu("MENU")
# menu.create_menu( l )

# menu_layer = Layer()
# menu_layer.add(menu)
# scene.add(menu_layer)
# scene.add(layer)

