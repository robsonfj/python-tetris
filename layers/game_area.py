import pyglet
import cocos
import time
from cocos.euclid import Vector2
from cocos.text import Label
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.layer import ColorLayer
#local libs
from sprites.block import Block
from sprites.piece import Piece
from sprites.block import Block
import game_controller

BLOCK_WALL = 'block_wall'

class Pieces_Wall(Layer):
    def __init__(self):
        Layer.__init__(self)
        
        self.position = Vector2()# posicao fixa da layer
        self.anchor = Vector2()
        
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
            child.anchor = Vector2()
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
                self.parent.sum_score(377)# adiciona o score de uma linha
                lines = self.same_line_blks.keys()
                for line in lines:
                    if(line > value):
                        self.same_line_blks[line-25] = self.same_line_blks[line]
                        for block in self.same_line_blks[line-25]:
                            block.y -= 25 # mover uma linha para baixo

                self.same_line_blks.pop(max(lines))# ultima linha agora ficou duplicada, entao remove a ultima linha da lista
                    

        except Exception as e:
            print("Error! Pieces_Wall check_line - ",e)
    


class Wall_Limits(Layer):
    def __init__(self):
        Layer.__init__(self)
        self.anchor = Vector2()
        self.add(Sprite(image=pyglet.resource.image('background-tetris.png'), anchor=self.anchor))# Background Image

        self.game_controller = game_controller.game_controller
        self.c_manager =  self.game_controller.c_manager# obtem instancia do gerenciador de colisao

        tmp_block = Block(Vector2(), '')# para obter as dimencoes da imagem do bloco
        init_pos_x = 250 # meio eixo x da tela
        init_pos_y = tmp_block.height/2
        
        for i in range(23):
            blk = Block((init_pos_x-tmp_block.width, init_pos_y+ (i*tmp_block.height)), block_color=BLOCK_WALL, b_type="Left_Wall")
            blk.anchor = (blk.width/2, blk.height/2)
            self.add(blk)

            blk = Block((init_pos_x+ (tmp_block.width*16), init_pos_y+ (i*tmp_block.height)), block_color=BLOCK_WALL, b_type="Right_Wall")
            blk.anchor = (blk.width/2, blk.height/2)
            self.add(blk)
            
        self.c_manager.add(Collision_Rect(init_pos_x - tmp_block.width*1.5 , tmp_block.width, init_pos_y, 23*tmp_block.height, b_type="Left_Wall", layr=self))
        self.c_manager.add(Collision_Rect(init_pos_x - tmp_block.width/2 + (tmp_block.width*16), tmp_block.width, init_pos_y, 23*tmp_block.height, b_type="Right_Wall", layr=self))

        for i in range(16):
            blk = Block((init_pos_x+ (i*tmp_block.width),init_pos_y), block_color=BLOCK_WALL, b_type="Base_Floor")
            blk.anchor = (blk.width/2, blk.height/2)
            self.add(blk)
            
        self.c_manager.add(Collision_Rect(init_pos_x-tmp_block.width/2, 16*tmp_block.width, init_pos_y-tmp_block.height/2, tmp_block.height, b_type="Base_Floor", layr=self))


class Collision_Rect():
     def __init__(self, x, width, y, height, b_type, layr):
         self.x = x
         self.width = width
         self.y = y
         self.height = height
         self.b_type = b_type
         blk = ColorLayer(255, 255, 255,255, width=width, height=height)
         blk.position = (x,y)
         blk.anchor = (width/2, height/2)
         #layr.add(blk)
         self.cshape = cocos.collision_model.AARectShape(Vector2(x + width/2, y + height/2), width/2, height/2)
