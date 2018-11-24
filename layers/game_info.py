
import random
import time
import pyglet
from sprites.piece import Piece
from sprites.piece import piece_types
from cocos.layer import Layer
from cocos.text import Label
from cocos.sprite import Sprite

def sort_new_piece():
        count = 1
        random.seed(time.time())
        chosen = random.randint(1, len(piece_types.keys()))
        for key, _ in piece_types.items():
            if(count >= chosen):
                return key
            count += 1
        return "square"

POS_NX_PIECE = (874, 500)# define posicao fixa da proxima peca

class Game_Info(Layer):
    def __init__(self):
        Layer.__init__(self)
        
        self.position = (0,0)## posicao fixa da layer
        self.anchor = (0,0)

        self.score_label = Label("0",position=(880,350),font_name = "Ravie", align = "center",anchor_x = "center")# texto onde mostra o score atual
        self.add(self.score_label)

        self.time_label = Label("00:00",position=(880,250),font_name = "Ravie", align = "center",anchor_x = "center")# texto onde mostra o score atual
        self.add(self.time_label )
        
        self.next_piece = Piece(POS_NX_PIECE, sort_new_piece())
        self.add(self.next_piece)
        self.update_time(122)

    def get_next_piece(self):
        piece = self.next_piece
        self.remove(self.next_piece)
        self.next_piece = Piece(POS_NX_PIECE, sort_new_piece())
        self.add(self.next_piece)
        return piece

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