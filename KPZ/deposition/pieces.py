import random

class PieceMaker(object):
    def __init__(self):
        return

    def create_random_tetris_piece(self, top_left_coord):
        pass

    def create_simple_block(self, coord):
        return Piece(set(coord))

    def create_2b1_block(self, coord):
        coords = set([coord, coord + (0,1)])
        return Piece(coords)

class Piece(object):
    def __init__(self, coords):
        self._indices = coords
         

    def move_down(self):
        self._indices = self.get_indices('down')
        return self._indices
        

    def get_indices(self, move = None):

        step = (0,0)
        if not move:
            return self._indices
        elif move == 'down':
            step = (1,0)
        else:
            return self._indices
            
        moved_coords = [x + step for x in self._indices]
        return set(moved_coords)
### initialize types of pieces here