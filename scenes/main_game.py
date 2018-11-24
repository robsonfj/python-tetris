import cocos
from pyglet.window.key import symbol_string
from cocos.layer import Layer
from cocos.text import Label
from cocos.scene import Scene
from cocos.collision_model import CollisionManagerGrid
from sprites.block import Block
from layers.keyboard_input import Keyboard_Input
from layers.wall_limits import Wall_Limits
from layers.game_info import Game_Info
from sprites.piece import Piece
import game_controller

POS_NEW_PIECE = (424, 512)# define posicao da nova peca


class Main_Game(Scene):
    is_event_handler = True
    def __init__(self):
        Scene.__init__(self)
        self.anchor = (0,0)
        self.is_coliding_left = False
        self.is_coliding_right = False
        self.is_coliding_base = False

        self.game_controller = game_controller.game_controller
        self.c_manager =  self.game_controller.c_manager# obtem instancia do gerenciador de colisao
        
        self.wall_limits = Wall_Limits()
        self.add(self.wall_limits)# adiciona layer da area do jogo

        keybd_input = Keyboard_Input()
        keybd_input.on_key_press = self.on_key_press 
        keybd_input.on_key_release = self.on_key_release 
        self.add(Keyboard_Input()) # adiciona layer para obter imput do teclado
                
        self.schedule(self.check_collision) # checa colisao a cada 400ms

    def start(self):
        self.currentScore = 0
        self.info_layer = Game_Info()
        self.add(self.info_layer)# adiciona layer de visualizacao de peca a cena

        self.add_new_piece()
        

    def add_new_piece(self):
        self.currPiece = self.info_layer.get_next_piece() # obtem peca inicial(a primeira proxima peca...)
        self.currPiece.position = POS_NEW_PIECE
        self.add(self.currPiece)# adiciona peca a cena

        self.currPiece.start_fall()
        for (_, block) in self.currPiece.children:# adiciona peca atual ao gerenciador de colisao
            self.c_manager.add(block)


    def time_delay(self, time_elapsed, key_string):# executado depois de um certo delay
        self.unschedule(self.time_delay)
        self.schedule_interval(self.key_action, 0.1, key_string)# move a peca a cada 100ms enquanto a tecla ainda estiver pressionada


    def on_key_press(self, key, modifiers):
        key_string = symbol_string(key)# obtem o valor em string da tecla pressionada 

        self.key_action(0, key_string)#executa uma acao da tecla quando pressionado
        self.schedule_interval(self.time_delay, 0.6, key_string)# espera 600ms antes de comecar a mover a peca rapidamente

    def on_key_release(self, key, modifiers):# quando a tecla deixa de ser pressionada ele para de mover a peca rapidamente
        self.unschedule(self.key_action)
        self.unschedule(self.time_delay)
        
    def key_action(self, time_elapsed, key_string):
        if( key_string == 'UP'):
            self.currPiece.move((0,25))
        if(not self.is_coliding_base and key_string == 'DOWN'):
            self.currPiece.move((0,-25))
        if(not self.is_coliding_left and key_string == 'LEFT'):
            self.currPiece.move((-25,0))
        if(not self.is_coliding_right and key_string == 'RIGHT'):
            self.currPiece.move((25,0))
        if(key_string == 'SPACE'):
            self.currPiece.rotate()


    def check_collision(self, time_elapsed):
        
        self.is_coliding_left = False
        self.is_coliding_right = False
        self.is_coliding_base = False
        for (_,block) in self.currPiece.children:
            for (obj, dist) in self.c_manager.objs_near_wdistance(block, 25):
                if(not obj.b_type == "Piece"):
                    print("colission - ", obj.b_type, dist)
                    if( obj.b_type == 'RightWall'):
                        self.is_coliding_right = True
                    if(obj.b_type == 'LeftWall'):
                        self.is_coliding_left = True
                    if(obj.b_type == 'Base'):
                        self.is_coliding_base = True
                        block.parent.stop_fall()

        