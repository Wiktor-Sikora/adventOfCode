from time import sleep
from os import system
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

    def _turn(self):
        match self.direction:
            case '^':
                self.direction = '>'
            case '>':
                self.direction = 'v'
            case 'v':
                self.direction = '<'
            case '<':
                self.direction = '^'

    def _check_for_end(self):
        if self.direction == '^' and self.position_y == 0:
            return True
        elif self.direction == '>' and self.position_x == self.max_x:
            return True
        elif self.direction == 'v' and self.position_y == self.max_y:
            return True
        elif self.direction == '<' and self.position_x == 0:
            return True
        else:
            return False
    
    def _check_for_obstacle(self):
        if self.direction == '^' and self.data[self.position_y - 1][self.position_x] == '#':
            return True
        elif self.direction == '>' and self.data[self.position_y][self.position_x + 1] == '#':
            return True
        elif self.direction == 'v' and self.data[self.position_y + 1][self.position_x] == '#':
            return True
        elif self.direction == '<' and self.data[self.position_y][self.position_x - 1] == '#':
            return True
        else:
            return False

    def _walk(self):
        match self.direction:
            case '^':
                self.position_y -= 1
            case '>':
                self.position_x += 1
            case 'v':
                self.position_y += 1
            case '<':
                self.position_x -= 1

    def _swap(self, position_y:int, position_x:int, swap_to:str):
        self.data[position_y] = self.data[position_y][:position_x] + swap_to + self.data[position_y][position_x + 1:]

    def _display_map(self):
        for line in self.data:
            print(line)

    def puzzle_one(self):        
        self.position_x, self.position_y = self._get_starting_position() 
        self.direction = self.data[self.position_y][self.position_x]
        self.max_y = len(self.data) - 1
        self.max_x = len(self.data[0]) - 1
        
        while not self._check_for_end():
            self._swap(self.position_y, self.position_x, 'X')

            while self._check_for_obstacle():
                self._turn()

            self._walk()

        return sum([line.count('X') for line in self.data]) + 1

    def _place_obstacle(self):
        match self.direction:
            case '^':
                self._swap(self.position_y - 1, self.position_x, '#')
                return self.position_y - 1, self.position_x
            case '>':
                self._swap(self.position_y, self.position_x + 1, '#')
                return self.position_y, self.position_x + 1
            case 'v':
                self._swap(self.position_y + 1, self.position_x, '#')
                return self.position_y + 1, self.position_x
            case '<':
                self._swap(self.position_y, self.position_x - 1, '#')
                return self.position_y, self.position_x - 1

    def _get_position_ahead(self):
        match self.direction:
            case '^':
                return self.position_y - 1, self.position_x
            case '>':
                return self.position_y, self.position_x + 1
            case 'v':
                return self.position_y + 1, self.position_x
            case '<':
                return self.position_y, self.position_x - 1

    def puzzle_two(self):
        self.get_data('example.txt')

        self.position_x, self.position_y = self._get_starting_position() 
        self.direction = self.data[self.position_y][self.position_x]
        self.max_y = len(self.data) - 1
        self.max_x = len(self.data[0]) - 1

        while not self._check_for_end():
            position_ahead_y, position_ahead_x = self._get_position_ahead()
            obstacle_y, obstacle_x = self._place_obstacle()
            position_y_before = self.position_y
            position_x_before = self.position_x
            direction_before = self.direction
            turns = []

            while not self._check_for_end():
                while self._check_for_obstacle():
                    turns.append((self.position_y, self.position_x))
                    self._turn()
                
                    if len(turns) > 7 and all(_ in turns[-4:] for _ in turns[-4:]):
                        self._swap(obstacle_y, obstacle_x, 'O')
                        break

                self._walk()

            turns.clear()
            self.position_x = position_x_before
            self.position_y = position_y_before
            self.direction = direction_before

            while self._check_for_obstacle():
                self._turn()

            self._walk()
        self._display_map()
        return sum([line.count('O') for line in self.data])

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())