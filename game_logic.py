import cocos
import pyglet
from pyglet.window.key import symbol_string
import random
import time
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.text import Label
from cocos.actions.base_actions import loop
from cocos.actions import MoveBy
from cocos.actions import RotateBy
from layers.piece import Piece
from layers.piece import piece_types
from scenes.main_game import Main_Game
from scenes.menu import Menu

class Game_Logic:
    def __init__(self):
        pyglet.resource.path = ['assets', 'assets/blocks'] # caminho para imagens e sprites
        pyglet.resource.reindex()
        pyglet.font.add_file('./assets/tetrominoes.ttf')# inicializa fonte
        
        self.pos_piece_next = (874, 500)
        self.pos_piece_start = (425, 512)
        
        
    def init( self,wind_width=800, wind_height=600):
        director.init(width=wind_width, height=wind_height, caption="TETRIS", fullscreen=False, resizable=False)
        
    def run(self):
        director.run(Menu())
    
    def close_game(self):
        director.pop()

    def init_new_game(self):
        self.main_game = Main_Game()# cria cena do jogo principal
        director.push(self.main_game)
        
        self.currentScore = 0
        self.nextPiece = Piece(self.pos_piece_next, self.sort_new_piece())
        self.currPiece = Piece(self.pos_piece_start, self.sort_new_piece()) 
        self.main_game.add(self.nextPiece)
        self.main_game.add(self.currPiece)

        self.main_game.schedule_interval(self.move,1.2)

    def move(self, time_count):
        print("x-",self.currPiece.x)
        print("y-",self.currPiece.y)
        if(self.currPiece.y >= 12):
            action = MoveBy((0,-25),0)
            self.currPiece.do(action)

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
        key_string = symbol_string(key)# obtem o valor em string da tecla pressionada 
        if( key_string == 'UP'):
            action = MoveBy((0,25),0)
            self.currPiece.do(action)
        if( key_string == 'DOWN'):
            self.move(0)
        if(self.currPiece.x >= 275 and key_string == 'LEFT'):
            action = MoveBy((-25,0),0)
            self.currPiece.do(action)
        if(self.currPiece.x <= 500 and key_string == 'RIGHT'):
            action = MoveBy((25,0),0)
            self.currPiece.do(action)
        if(key_string == 'LSHIFT'):
            action = RotateBy(90,0)
            self.currPiece.do(action)

        pass

    def on_key_release(self, key, modifiers): 
        #TODO
        pass

    

game_logic = Game_Logic()