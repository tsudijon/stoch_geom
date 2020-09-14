import numpy as np
from pieces import Piece, PieceMaker
import random
import pygame

class Board(object):
    def __init__(self, size = (500,10)):
        self._size = size
        self._pieces = []
        self._board = np.zeros(size)
        self._used_indices = set() 
        self.zoom = 20

        self._piece_factory = PieceMaker()

        #### set the bottom row to be used
        for i in range(self._size[1]):
            self._used_indices.add((self._size[0]-1,i))
        
        
    def update(self):
        self.move_board()
        self.initialize_piece()      

        
    def move_board(self):
        ### move all pieces downwards: update board and pieces?
        ### update pieces if collision
        for piece in self._pieces:
            if self.check_collision(piece):
                self._used_indices = self._used_indices.union(piece.get_indices())
                self._pieces.remove(piece)
            else:
                piece.move_down()


    def initialize_piece(self):
        ### add pieces with some probability
        ### check for collisions with new pieces?
        coord = (0,random.randrange(0, self._size[1]-1))
        self._pieces.append(self._piece_factory.create_2b1_block(coord))

    def check_collision(self, piece):
        ### also check for OOB but should be OK
        if not self._check_in_bounds(piece.get_indices('down')):
            return False

        if self._used_indices.intersection(piece.get_indices('down')):
            return False
        else:
            return True
        ###

    def _check_in_bounds(self, piece):
        ### TODO: not implemented yet
        return True    

    #########################
    ### drawing functions ###
    #########################




if __name__ == "__main__":
    ### create board here
    pass