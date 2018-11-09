from block_sprite import Block
from cocos.layer import Layer
from cocos.actions.interval_actions import MoveBy

class Piece(Layer):
    def __init__(self, position, p_type):
        Layer.__init__(self)

        self.position = position
        self.p_type = p_type
        

        block1 = Block(position, 'red')
        block2 = Block((position[0]+32, position[1]), 'red')
        block3 = Block((position[0]+32, position[1]+32), 'red')
        block4 = Block((position[0]+64, position[1]+32), 'red')
        
        self.add(block1)
        self.add(block2)
        self.add(block3)
        self.add(block4)

        action = MoveBy((0,-700), 1)
        self.do(action)