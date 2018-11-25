
import random
import time
import pyglet
from sprites.piece import Piece
from sprites.block import Block
from sprites.piece import piece_types
from cocos.layer import Layer
from cocos.sprite import Sprite
import game_controller

class Pieces_Wall(Layer):
    def __init__(self):
        Layer.__init__(self)
        
        self.position = (0,0)# posicao fixa da layer
        self.anchor = (0,0)
        
        self.same_line_blks = {}# vai armazenar lista de blocos com mesma altura ( para remover quando completar a linha)

        self.game_controller = game_controller.game_controller
        self.c_manager =  self.game_controller.c_manager# obtem instancia do gerenciador de colisao
        

        self.schedule_interval(self.check_line, 0.5) # checa se completou uma linha de blocos a cada 500ms

    def add_to_wall(self, block):
        if(type(block) == Block):
            try:
                block.b_type = "Base_Block" # altera o tipo do bloco, agora faz parte da base
                self.add(block)
                self.same_line_blks[block.y].append(block)
                
            except KeyError:# se obteve erro cria uma array e adiciona novamente
                self.same_line_blks[block.y] = []
                self.same_line_blks[block.y].append(block)
            finally:
                self.c_manager.add(block) # adiciona bloco ao gerenciador de colisoes

    def process_piece(self, piece):
        for _ in range(0, len(piece.children)):
            child = piece.children[0][1]
            piece.remove(child)
            child.anchor = (0,0)
            child.position = piece.point_to_world(child.position)
            self.add_to_wall(child)
        piece.kill()

    def check_line(self, time_elapsed):
        try:
            removed_lines = []
            for (key, value) in self.same_line_blks.items():
                if(len(value) >= 16):# se a quantidade de blocos em uma linha for 16 ou maior elimina a linha e abaixa as pecas superiores
                    for block in value:
                        block.kill()
                        self.c_manager.remove_tricky(block)
                    removed_lines.append(key)

            for value in removed_lines:# para as linhas de blocos acima, mover uma linha para baixo
                self.parent.sum_score(375)# adiciona o score de uma linha
                lines = self.same_line_blks.keys()
                for line in lines:
                    if(line > value):
                        self.same_line_blks[line-25] = self.same_line_blks[line]
                        for block in self.same_line_blks[line-25]:
                            block.y -= 25 # mover uma linha para baixo

                self.same_line_blks.pop(max(lines))# ultima linha agora ficou duplicada, entao remove a ultima linha da lista
                    

        except Exception as e:
            print("Error! Pieces_Wall check_line - ",e)
    