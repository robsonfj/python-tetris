import cocos
from pyglet.window.key import symbol_string
from cocos.layer import Layer
from cocos.text import Label
from cocos.scene import Scene
from cocos.actions import MoveBy
from cocos.actions import RotateBy
from cocos.collision_model import CollisionManagerGrid
from cocos.actions import CallFunc
from sprites.block import Block
from layers.keyboard_input import Keyboard_Input
from layers.wall_limits import Wall_Limits
from layers.game_info import Game_Info
from layers.pieces_wall import Pieces_Wall
from sprites.piece import Piece
import game_controller

POS_NEW_PIECE = (424, 562.5)# define posicao da nova peca



class Main_Game(Scene):
    is_event_handler = True
    def __init__(self):
        Scene.__init__(self)
        self.anchor = (0,0)
        self.is_colliding_left = False
        self.is_colliding_right = False
        self.is_colliding_base = False
        
        keybd_input = Keyboard_Input()
        keybd_input.on_key_press = self.on_key_press 
        keybd_input.on_key_release = self.on_key_release 
        self.add(Keyboard_Input()) # adiciona layer para obter imput do teclado
        

    def start(self):
        self.currentScore = 0        
        self.game_time = 0
        self.schedule_interval(self.count_time, 1)#inicia timer para contagem do tempo

        self.wall_limits = Wall_Limits()
        self.add(self.wall_limits)# adiciona layer da area do jogo

        self.pieces_wall = Pieces_Wall()
        self.add( self.pieces_wall )# adiciona a a layer para armazenas todas a pecas caidas

        self.c_manager =  game_controller.game_controller.c_manager# obtem instancia do gerenciador de colisao
        self.schedule(self.check_collision) # checa colisao a cada frame

        self.game_info_layer = Game_Info()
        self.add(self.game_info_layer)# adiciona layer de visualizacao de peca a cena

        self.add_next_piece()# inicializa a primeira peca


    def game_over(self):
        self.c_manager.clear()# limpa lista de objetos com colisao
        self.unschedule(self.count_time)
        #self.add(Ranking())

    def add_next_piece(self):
        self.currPiece = self.game_info_layer.obtain_next_piece() # obtem peca inicial(a primeira proxima peca...)
        self.currPiece.position = POS_NEW_PIECE
        self.pieces_wall.add(self.currPiece)# adiciona peca na layer de pecas e blocos 

        self.currPiece.start_fall()
        for (_, block) in self.currPiece.children:# adiciona peca atual ao gerenciador de colisao
            self.c_manager.add(block)    


    def sum_score(self, amount): # soma no score a quantidade passada
        #TODO
        pass

    def count_time(self, time_elapsed):# metodo chamado com o tempo que passou, entao guarda e atualiza na layer o tempo atual do jogo
        #TODO
        pass

    def check_collision(self, time_elapsed):#todo frame checa se a peca possui colisao
        try:
            self.is_colliding_left = False
            self.is_colliding_right = False
            self.is_colliding_base = False
            for (_,block) in self.currPiece.children:
                for (obj, dist) in self.c_manager.ranked_objs_near(block, 5): # retorna lista com objetos que estao com na distancia passada
                    if(not obj.b_type == "Piece"):
                        #print("colission - ", obj.b_type, dist)
                        if(not self.is_colliding_right and obj.b_type == 'Right_Wall'):#colisoes na direita da parede
                            self.is_colliding_right = True
                            
                        if(not self.is_colliding_left and obj.b_type == 'Left_Wall'):#colisoes na esquerda da parede
                            self.is_colliding_left = True

                        if(not self.is_colliding_base and obj.b_type == 'Base_Floor'):#colisoes no chao
                            self.is_colliding_base = True
                            self.piece_must_stop(block.parent)

                        if(obj.b_type == 'Base_Block'):#colisoes na parte base dos blocos
                            if(not self.is_colliding_right and  block.cshape.touches_point(obj.x-25, obj.y)):#colisoes na direita da peca
                                self.is_colliding_right = True
                            if(not self.is_colliding_left and  block.cshape.touches_point(obj.x+25, obj.y)):#colisoes na esquerda da peca
                                self.is_colliding_left = True
                            
                            if(not self.is_colliding_base and block.cshape.touches_point(obj.x, obj.y+25)):
                                self.is_colliding_base = True
                                self.piece_must_stop(block.parent)
                                

        except AttributeError as e:
            print("Error! Main_Game check_collision - ", e)


    def piece_must_stop(self, piece):# executa o necessario para parar a peca e adicionar ao bloco de pecas
       
        piece.stop_fall()

        if(self.currPiece.y >= 550):# finaliza a partida quando nao consegue adicionar mais pecas ao topo
            self.game_over()
            return

        self.sum_score(25)# adiciona o score de uma peca
        
        self.pieces_wall.process_piece(piece)
        self.add_next_piece()
        

    ''' KEYS INPUT '''

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
            self.unschedule(self.currPiece.do_fall)
            self.schedule_interval(self.currPiece.do_fall, 1)
        if(not self.is_colliding_base and key_string == 'DOWN'):
            self.unschedule(self.currPiece.do_fall)
            self.schedule_interval(self.currPiece.do_fall, 0.03)
        if(not self.is_colliding_left and key_string == 'LEFT'):
            self.currPiece.move((-25,0))
        if(not self.is_colliding_right and key_string == 'RIGHT'):
            self.currPiece.move((25,0))
        if(key_string == 'SPACE'):
            self.currPiece.rotate()


    def on_exit(self):
        self.c_manager.clear()# limpa lista de objetos com colisao
        return super().on_exit()