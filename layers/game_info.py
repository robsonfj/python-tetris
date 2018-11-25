
import time
from sprites.piece import Piece
from sprites.piece import piece_types
from cocos.layer import Layer
from cocos.text import Label
from cocos.sprite import Sprite
from cocos.actions import CallFunc

POS_NX_PIECE = (874, 500)# define posicao fixa da proxima peca

'''
Classe filha de Layer armazena e atualiza as informacoes de jogo como proxima peca, score_label, time_label
'''
class Game_Info(Layer):
    def __init__(self):
        Layer.__init__(self)
        
        self.position = (0,0)## posicao fixa da layer
        self.anchor = (0,0)

        self.score_label = Label("0",position=(880,350),font_name = "Ravie", align = "center",anchor_x = "center")# texto onde mostra o score atual
        self.add(self.score_label)

        self.time_label = Label("00:00",position=(880,250),font_name = "Ravie", align = "center",anchor_x = "center")# texto onde mostra o score atual
        self.add(self.time_label )
        
        self.next_piece = Piece(POS_NX_PIECE)
        self.add(self.next_piece)

    def obtain_next_piece(self): # obtem proxima peca armazenada e programa para obter uma nova peca
        piece = self.next_piece
        self.remove(self.next_piece)
        self.schedule(self.new_next_piece)
        return piece

    def new_next_piece(self, elapsed): # obtem proxima peca e armazena
        self.unschedule(self.new_next_piece)
        self.next_piece = Piece(POS_NX_PIECE)
        self.add(self.next_piece)

    def update_score(self, score):# atualiza o label mostrando o score
        try:
            self.score_label.element.text = str(score)
        except:
            self.score_label.element.text = "0"
    
    def update_time(self, secs):# atualiza o label mostrando o tempo
        try:
            date = time.localtime(secs)
            self.time_label.element.text = (date.tm_min < 10 and "0"+str( date.tm_min) or str( date.tm_min)) +":"+ (date.tm_sec < 10 and "0"+ str(date.tm_sec) or str(date.tm_sec))
        except:
            self.time_label.element.text = "00:00"