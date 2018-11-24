import cocos
import pyglet
from pyglet.window.key import symbol_string
from cocos.director import director
from cocos.scene import Scene
from cocos.collision_model import CollisionManagerGrid
from cocos.text import Label
from scenes.main_game import Main_Game
from scenes.menu import Menu

class Game_Controller:
    def __init__(self):
        pyglet.resource.path = ['assets', 'assets/blocks'] # caminho para imagens e sprites
        pyglet.resource.reindex()
        pyglet.font.add_file('./assets/tetrominoes.ttf')# inicializa fonte
        
        
    def init( self,wind_width=800, wind_height=600):
        director.init(width=wind_width, height=wind_height, caption="TETRIS", fullscreen=False, resizable=False)
        self.c_manager = CollisionManagerGrid(0,wind_width, 0, wind_height, 25, 25)# inicializa gerenciador de colisao
        
    def run(self):
        director.run(Menu())
    
    def close_game(self):
        director.pop()

    def init_new_game(self):
        self.main_game = Main_Game()# cria cena do jogo principal
        director.push(self.main_game)
        
        self.main_game.start()


    def game_over(self):
        self.c_manager.clear()# limpa lista de objetos com colisao
       

    def on_key_press(self, key, modifiers):
        self.main_game.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.main_game.on_key_release(key, modifiers)
        

game_controller = Game_Controller()