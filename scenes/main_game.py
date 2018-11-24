import cocos
from pyglet.window.key import symbol_string
from cocos.layer import Layer
from cocos.text import Label
from cocos.scene import Scene
import cocos.collision_model as collision_model
from sprites.block import Block
from layers.keyboard_input import Keyboard_Input
from layers.game_area import Game_Area
from layers.next_piece import Next_Piece
from sprites.piece import Piece

POS_NEW_PIECE = (425, 512)# define posicao da nova peca


class Main_Game(Scene):
    is_event_handler = True
    def __init__(self):
        self.anchor = (0,0)
        self.position = (0,0)
        Scene.__init__(self)
        
        self.blocks = []
        
        self.game_area = Game_Area()
        self.add(self.game_area)# adiciona layer da area do jogo

        keybd_input = Keyboard_Input()
        keybd_input.on_key_press = self.on_key_press 
        keybd_input.on_key_release = self.on_key_release 
        self.add(Keyboard_Input()) # adiciona layer para obter imput do teclado
        
        self.c_manager = collision_model.CollisionManager# inicializa gerenciador de colisao
        
        self.schedule_interval(self.check_collision, 0.2) # checa colisao a cada 200ms

    def start(self):
        self.currentScore = 0
        self.nextPieceLayer = Next_Piece()
        self.add(self.nextPieceLayer)# adiciona layer de visualizacao de peca a cena

        self.currPiece = self.nextPieceLayer.get_next_piece() # obtem peca inicial(a primeira proxima peca...)
        self.currPiece.position = POS_NEW_PIECE
        self.add(self.currPiece)# adiciona peca atual ao cena
        
        self.currPiece.start_fall()
        self.c_manager.add(self.currPiece)# adiciona peca atual ao gerenciador de colisao
    

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
        self.game_area.update_score(self.currentScore) 


        #for obj in self.c_manager.iter_colliding(self.currPiece):
            #print("colission", obj)
        pass