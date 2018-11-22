import cocos
from cocos.director import director
from scenes.menu import Menu
import pyglet
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.text import Label


class Game_Logic:
    def __init__(self):
        self.reset_matrix()
        
    def init(self,wind_width=800, wind_height=600):
        pyglet.resource.path = ['assets', 'assets/blocks'] # caminho para imagens e sprites
        pyglet.resource.reindex()
        pyglet.font.add_file('./assets/tetrominoes.ttf')# inicializa fonte

        director.init(width=wind_width, height=wind_height, caption="TETRIS", fullscreen=False, resizable=False)
        
    def run(self):
        director.run(Menu())

    def init_new_game(self):
        self.reset_matrix()
        self.currentScore = 0
        self.nextPiece = self.sort_new_piece()
        self.currPiece = self.sort_new_piece()
        


    def reset_matrix(self):
        self.blocksM = []
        for _ in range(20):
            column = []
            for _ in range(10):
                column.append(0)
            self.blocksM.append(column)

    def sort_new_piece(self):
        #TODO
        return 0
       
    def on_key_press(self, key, modifiers):
         #TODO
        pass

    def on_key_release(self, key, modifiers): 
        #TODO
        pass

game_logic = Game_Logic()