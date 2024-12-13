class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        with open(path) as f:
            self.data = [line.rstrip() for line in f]

    def _get_starting_position(self):
        for position_y, line in enumerate(self.data):
            if '^' in line:
                return line.index('^'), position_y

    def _change_direction(self):
        if self.direction == '^':
            self.direction = '>'
        elif self.direction == '>':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '<'
        else:
            self.direction = '^'

    def _check_ahead(self):
        ''' returns False if it's end of the map'''

        if self.direction == '^':
            if self.current_position_y == 0:
                return False
            elif self.data[self.current_position_y + 1][self.current_position_x] == '#':
                self._change_direction()
                return self._check_ahead()
        elif self.direction == '>':
            if self.current_position_x == self.max_position_x:
                return False
            elif self.data[self.current_position_y][self.current_position_x  + 1] == '#':
                self._change_direction()
                return self._check_ahead()
        elif self.direction == 'v':
            if self.current_position_y == self.max_position_y:
                return False
            elif self.data[self.current_position_y - 1][self.current_position_x] == '#':
                self._change_direction()
                return self._check_ahead()
        else: # <
            if self.current_position_x == 0:
                return False
            elif self.data[self.current_position_y][self.current_position_x - 1] == '#':
                self._change_direction()
                return self._check_ahead()
        return True


    def _guard_walk(self):
        if self.direction == '^':
            self.current_position_y -= 1
        elif self.direction == '>':
            self.current_position_x += 1
        elif self.direction == 'v':
            self.current_position_y += 1
        else:
            self.current_position_y -= 1

    def puzzle_one(self):
        self.current_position_x, self.current_position_y = self._get_starting_position()
        self.max_position_x = len(self.data[0]) - 1
        self.max_position_y = len(self.data) - 1
        self.direction = '^'
        
        positions_visited = []   
        while True:
            if not self._check_ahead():
                break
            self._guard_walk()

        return len(set(positions_visited))




    def puzzle_two(self):
        self.get_data()
        pass

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())