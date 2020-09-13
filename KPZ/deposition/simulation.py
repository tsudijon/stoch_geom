import numpy as np



class board(object):
    def __init__(self, size = (1000,20)):
        self._size = size
        self._pieces = []
        self._board = np.zeros(size)
        self._used_indices = set() 

        #### set the bottom row to be used
        for i in range(self._size[1]):
            self._used_indices.add((self._size[0]-1,i))
        
        
    def update(self):
        self._move_board()
        self._initialize_pieces()
        
    def _move_board(self):
        ### move all pieces downwards: update board and pieces?

        ### update pieces if collision
        for piece in self._pieces:
            if self._check_collision(piece):
                self._used_indices.union(piece.get_indices())
            else:
                piece.move_down()

        pass 

    def _initialize_pieces(self):
        ### add pieces with some probability
        ### check for collisions with new pieces?
        pass

    def _check_collision(self, piece):
        pass


if __name__ == "__main__":
    ### create board here
    pass