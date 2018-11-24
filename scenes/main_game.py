import cocos
import random
import time
from pyglet.window.key import symbol_string
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.collision_model import CollisionManager
from sprites.block import Block
from layers.keyboard_input import Keyboard_Input
from layers.game_area import Game_Area
from layers.piece import Piece
from layers.piece import piece_types

class Main_Game(Scene):
    is_event_handler = True
    def __init__(self):
        self.anchor = (0,0)
        self.position = (0,0)
        Scene.__init__(self)
        
        self.blocks = []
        self.pos_piece_next = (874, 500)
        self.pos_piece_start = (425, 512)

        self.game_area = Game_Area()
        self.add(self.game_area)
        keybd_input = Keyboard_Input()
        keybd_input.on_key_press = self.on_key_press 
        keybd_input.on_key_release = self.on_key_release 
        self.add(Keyboard_Input()) # adiciona layer para obter imput do teclado
        
        self.collision_manager = CollisionManager()
        self.schedule_interval(self.check_collision, 1)
        
    def on_key_press(self, key, modifiers):
        print(key)

    def start(self):
        self.currentScore = 0
        self.nextPiece = Piece(self.pos_piece_next, self.sort_new_piece())
        self.currPiece = Piece(self.pos_piece_start, self.sort_new_piece()) 
        self.add(self.nextPiece)
        self.add(self.currPiece)

        self.currPiece.start_fall()

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
        key_string = symbol_string(key)# obtem o valor em string da tecla pressionada 
        if( key_string == 'UP'):
            self.currPiece.move((0,25))
        if( key_string == 'DOWN'):
            self.currPiece.move((0,-25))
        if(self.currPiece.x > 250 and key_string == 'LEFT'):
            self.currPiece.move((-25,0))
        if(self.currPiece.x < 625 and key_string == 'RIGHT'):
            self.currPiece.move((25,0))
        if(key_string == 'SPACE'):
            self.currPiece.rotate()

    def on_key_release(self, key, modifiers): 
        #TODO
        pass

    def check_collision(self, time_elapsed):
        self.currentScore += 15
        self.game_area.score.element.text = str(self.currentScore)


        #for obj in CollisionManager.iter_colliding (self.currPiece):
            #print("colission", obj)
        pass