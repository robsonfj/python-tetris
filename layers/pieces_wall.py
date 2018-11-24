
import random
import time
import pyglet
from sprites.piece import Piece
from sprites.block import Block
from sprites.piece import piece_types
from cocos.layer import Layer
from cocos.sprite import Sprite


class Pieces_Wall(Layer):
    def __init__(self):
        Layer.__init__(self)
        
        self.position = (0,0)# posicao fixa da layer
        self.anchor = (0,0)
        
        self.same_line_blks = {0:[]}# vai armazenar lista de blocos com mesma altura ( para remover quando completar a linha)

        self.schedule_interval(self.check_line, 0.5) # checa se completou uma linha de blocos a cada 500ms

    def add_to_wall(self, blocks):
        try:
            for block in blocks:
                if(type(block) == Block):
                    self.add(block)
                    self.same_line_blks[round(block.y, 0)].append(block)
        except:
            print("Error! Pieces_Wall add_to_wall")

    def check_line(self, time_elapsed):
        try:
            removed_pos_y = 0
            count = 0 # contagem de linhas ja movidas
            for (key, value) in self.same_line_blks.items():
                if(len(value) >= 16):# se a quantidade de blocos em uma linha for 16 ou maior elimina a linha e abaixa as pecas superiores
                    for block in value:
                        block.kill()
                    removed_pos_y = key
                if(not removed_pos_y == 0 and key > removed_pos_y):
                    self.same_line_blks[removed_pos_y + (25*count)] = self.same_line_blks[key]
                    for block in value:
                        block.y -= 25 # mover uma linha para baixo
                    count += 1

        except:
            print("Error! Pieces_Wall check_line")

    def removed_line(self, pos_y):
        try:
            for (key, value) in self.same_line_blks.items():
                if(key > pos_y):
                    
                    
        except:
            print("Error! Pieces_Wall check_line")
        
    