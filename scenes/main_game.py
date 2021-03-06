import cocos
import time
import pyglet
from pyglet.window.key import symbol_string
from cocos.layer import Layer
from cocos.layer import MultiplexLayer
from cocos.text import Label
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.actions import MoveBy
from cocos.actions import RotateBy
from cocos.collision_model import CollisionManagerGrid
from cocos.actions import CallFunc
from cocos.euclid import Vector2
#local libs
from sprites.block import Block
from layers.keyboard_input import Keyboard_Input
from layers.game_area import Wall_Limits
from layers.game_info import Game_Info
from layers.game_area import Pieces_Wall
from layers.ranking import Ranking
from sprites.piece import Piece
from layers.pause import Pause
import game_controller


POS_NEW_PIECE = (424, 562.5)# define posicao da nova peca


class Main_Game(Scene):
    is_event_handler = True
    def __init__(self):
        Scene.__init__(self)
        self.anchor = Vector2()


    def start(self):
        #variaveis a serem resetadas com u jogo novo
        self.is_game_over = False
        self.is_colliding_left = False
        self.is_colliding_right = False
        self.is_colliding_base = False
        self.currentScore = 0        
        self.game_time = 0

        self.c_manager =  game_controller.game_controller.c_manager# obtem instancia do gerenciador de colisao

        self.keybd_input = Keyboard_Input()# iniciaiza o layer de input do teclado
        self.wall_limits = Wall_Limits()# iniciaiza o layer para as delimitacoes do jogo
        self.pieces_wall = Pieces_Wall()# iniciaiza o layer de bloco de pecas
        self.game_info_layer = Game_Info()# iniciaiza o layer de informacoes do jogo (informacoes no canto direito)
        self.game_over_lyr = Ranking(is_game_over=True)# iniciaiza o layer de game over para mostrar ranking
        self.pause_lyr = Pause()# iniciaiza o layer de pause do game
        # iniciaiza o layer multiplo para alternar entre layer do input,mostrar o game over e pause
        self.multi_layer = MultiplexLayer(Layer(), self.game_over_lyr, self.pause_lyr)

        self.add(self.wall_limits)# adiciona layer
        self.add(self.game_info_layer)# adiciona layer
        self.add(self.pieces_wall)# adiciona a a layer
        self.add(self.keybd_input)# adiciona layer
        self.add(self.multi_layer)# adiciona layer

        self.add_next_piece()# inicializa a primeira peca

        self.start_timer()
        

    def start_timer(self):
        self.schedule_interval(self.count_time, 1)#inicia timer para contagem do tempo
    def stop_timer(self):
        self.unschedule(self.count_time)#remove contagem do tempo

    def game_over(self):
        self.is_game_over = True
        self.c_manager.clear()# limpa lista de objetos com colisao
        self.unschedule(self.count_time)
        self.multi_layer.switch_to(1)
        self.game_over_lyr.show_rank()


    def add_next_piece(self):
        self.currPiece = self.game_info_layer.obtain_next_piece() # obtem peca inicial(a primeira proxima peca...)
        self.currPiece.position = POS_NEW_PIECE
        self.pieces_wall.add(self.currPiece)# adiciona peca na layer de pecas e blocos 

        self.currPiece.start_fall()
        for (_, block) in self.currPiece.children:# adiciona peca atual ao gerenciador de colisao
            self.c_manager.add(block)    


    def sum_score(self, amount): # soma no score a quantidade passada
        self.currentScore += amount
        self.game_info_layer.update_score(self.currentScore)

    def count_time(self, time_elapsed):# metodo chamado com o tempo que passou (1s), entao guarda e atualiza na layer o tempo atual do jogo
        self.game_time += time_elapsed
        self.game_info_layer.update_time(self.game_time) 


    def piece_must_stop(self):# executa o necessario para parar a peca e adicionar ao bloco de pecas

        self.currPiece.stop_fall()# para a peca
        self.currPiece.update_blk_cshape()# atualiiza a colisao para a ultima posicao da peca apos terminar de cair

        if(self.currPiece.y >= 525):# finaliza a partida quando nao consegue adicionar mais pecas ao topo
            self.game_over()
            return

        self.sum_score(27)# adiciona o score de uma peca
        
        self.pieces_wall.process_piece(self.currPiece)
        self.add_next_piece()
        
    def on_pause(self):
        self.pause()
        self.stop_timer()
        self.currPiece.stop_fall()
        self.multi_layer.switch_to(2)
        
    def on_unpause(self):
        self.resume()
        self.start_timer()
        self.currPiece.start_fall()
        self.multi_layer.switch_to(0)

    def on_rank_exit(self):
        if(self.is_game_over):
            game_controller.game_controller.close_scene()



    def on_exit(self):
        self.remove(self.wall_limits)# adiciona layer
        self.remove(self.game_info_layer)# adiciona layer
        self.remove(self.pieces_wall)# adiciona a a layer
        self.remove(self.keybd_input)# adiciona layer
        self.remove(self.multi_layer)# adiciona layer
        self.c_manager.clear()# limpa lista de objetos com colisao

        if(self.is_game_over):# quando acontece um game over adiciona a pontuacao ao rank
            score = self.currentScore
            plyr_name = self.game_over_lyr.player_name
            time_str = self.game_info_layer.get_time_str()
            self.game_over_lyr.add_rank({score:(plyr_name, time_str)})

        return super().on_exit()

    def on_enter(self):
        self.start()
        return super().on_enter()

    ''' KEYS INPUT '''
    def key_action(self, time_elapsed, key_string):# para cada tecla executa a acao especifica
        
        if(key_string ==  'P' or key_string ==  'ESCAPE'):
            self.on_pause()

        if(not self.is_colliding_base and key_string == 'DOWN'):
            self.unschedule(self.currPiece.do_fall)
            self.schedule_interval(self.currPiece.do_fall, 0.03)

        if(not self.is_colliding_left and key_string == 'LEFT'):
            self.currPiece.move(Vector2(-25,0))

        if(not self.is_colliding_right and key_string == 'RIGHT'):
            self.currPiece.move(Vector2(25,0))

        if(key_string == 'SPACE'):
            self.currPiece.rotate()


    def time_delay(self, time_elapsed, key_string):# executado depois de um certo delay
        self.unschedule(self.time_delay)
        self.schedule_interval(self.key_action, 0.1, key_string)# move a peca a cada 100ms enquanto a tecla ainda estiver pressionada

    def on_key_press(self, key, modifiers):
        key_string = symbol_string(key)# obtem o valor em string da tecla pressionada 

        self.key_action(0, key_string)#executa uma acao da tecla quando pressionado
        self.schedule_interval(self.time_delay, 0.3, key_string)# espera 300ms antes de comecar a mover a peca rapidamente

    def on_key_release(self, key, modifiers):# quando a tecla deixa de ser pressionada ele para de mover a peca rapidamente
        self.unschedule(self.key_action)
        self.unschedule(self.time_delay)
        