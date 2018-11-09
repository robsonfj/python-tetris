from block_model import Block
from cocos.layer import Layer

class Piece:
    def __init__(self, position, p_type):
        self.pos = position
        self.p_type = p_type
        self.layer = Layer()

        block1 = Block(position, 'red')
        block2 = Block((position[0]+32, position[1]), 'red')
        block3 = Block((position[0]+32, position[1]+32), 'red')
        block4 = Block((position[0]+64, position[1]+32), 'red')
        self.blocks = [block1,block2,block3,block4]
        self.layer.add(block1.sprite)
        self.layer.add(block2.sprite)
        self.layer.add(block3.sprite)
        self.layer.add(block4.sprite)