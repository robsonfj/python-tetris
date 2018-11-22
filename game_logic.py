import cocos
import pyglet
import random
import time
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.text import Label
from layers.piece import Piece
from layers.piece import piece_types
from scenes.main_game import Main_Game
from scenes.menu import Menu

class Game_Logic:
    def __init__(self):
        pyglet.resource.path = ['assets', 'assets/blocks'] # caminho para imagens e sprites
        pyglet.resource.reindex()
        pyglet.font.add_file('./assets/tetrominoes.ttf')# inicializa fonte
        
        self.pos_piece_next = (435, 245)
        self.pos_piece_start = (210, 270)
        
    def init( self,wind_width=800, wind_height=600):
        director.init(width=wind_width, height=wind_height, caption="TETRIS", fullscreen=False, resizable=False)
        
    def run(self):
        director.run(Menu())

    def init_new_game(self):
        self.main_game = Main_Game()# cria cena do jogo principal
        director.push(self.main_game)

        self.currentScore = 0
        self.nextPiece = Piece(self.pos_piece_next, self.sort_new_piece())
        self.currPiece = Piece(self.pos_piece_start, self.sort_new_piece()) 
        self.main_game.add(self.nextPiece)
        self.main_game.add(self.currPiece)

    def sort_new_piece(self):
        count = 1
        random.seed(time.time())
        chosen = random.randint(1, len(piece_types.keys()))
        for key, _ in piece_types.items():
            if(count >= chosen):
                return key
            count += 1
        return "square"
       
    def on_key_press(self, key, modifiers):
         #TODO
        pass

    def on_key_release(self, key, modifiers): 
        #TODO
        pass

    def close_game(self):
        director.pop()

game_logic = Game_Logic()