
import random
import time
import pyglet
from sprites.piece import Piece
from sprites.piece import piece_types
from cocos.layer import Layer
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

class Next_Piece(Layer):
    def __init__(self):
        Layer.__init__(self)
        
        self.position = (0,0)## posicao fixa da layer
        self.anchor = (0,0)
        
        self.next_piece = Piece(POS_NX_PIECE, sort_new_piece())
        self.add(self.next_piece)

    def get_next_piece(self):
        piece = self.next_piece
        self.remove(self.next_piece)
        self.next_piece = Piece(POS_NX_PIECE, sort_new_piece())
        self.add(self.next_piece)
        return piece

    