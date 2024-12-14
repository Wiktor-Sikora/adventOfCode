from time import sleep
import os

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

    def _check_ahead(self):
        '''returns False if it's end of the map'''

        if self.direction == '^':
            if self.current_position_y == 0:
                return False
            elif self.data[self.current_position_y - 1][self.current_position_x] == '#':
                self.direction = '>'
                return self._check_ahead()
        elif self.direction == '>':
            if self.current_position_x == self.max_position_x:
                return False
            elif self.data[self.current_position_y][self.current_position_x  + 1] == '#':
                self.direction = 'v'
                return self._check_ahead()
        elif self.direction == 'v':
            if self.current_position_y == self.max_position_y:
                return False
            elif self.data[self.current_position_y + 1][self.current_position_x] == '#':
                self.direction = '<'
                return self._check_ahead()
        else: # <
            if self.current_position_x == 0:
                return False
            elif self.data[self.current_position_y][self.current_position_x - 1] == '#':
                self.direction = '^'
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
            self.current_position_x -= 1

    def puzzle_one(self):
        self.current_position_x, self.current_position_y = self._get_starting_position()
        self.max_position_x = len(self.data[0]) - 1
        self.max_position_y = len(self.data) - 1
        self.direction = '^'
        
        positions_visited = [(self.current_position_x, self.current_position_y)]
        while self._check_ahead():
            self._guard_walk()
            positions_visited.append((self.current_position_x, self.current_position_y))

        return len(set(positions_visited))

    def _swap(self, position:int, string:str, swap_to:str):
        return string[:position] + swap_to + string[position + 1:]

    def _place_obstacle(self):
        if self.direction == '^':
            self.data[self.current_position_y - 1] = self._swap(self.current_position_x, self.data[self.current_position_y - 1], '#')
            return self.current_position_y - 1, self.current_position_x
        elif self.direction == '>':
            self.data[self.current_position_y] = self._swap(self.current_position_x + 1, self.data[self.current_position_y], '#')
            return self.current_position_y, self.current_position_x + 1
        elif self.direction == 'v':
            self.data[self.current_position_y + 1] = self._swap(self.current_position_x, self.data[self.current_position_y + 1], '#')
            return self.current_position_y + 1, self.current_position_x
        else: # <
            self.data[self.current_position_y] = self._swap(self.current_position_x - 1, self.data[self.current_position_y], '#')
            return self.current_position_y, self.current_position_x - 1

    def _remove_obstacle(self, y:int, x:int):
        self.data[y] = self._swap(x, self.data[y], '+')

    def _display_map(self):
        for index, line in enumerate(self.data):
            if self.current_position_y == index:
                print(self._swap(self.current_position_x, line, swap_to=self.direction))
            else:
                print(line)
    
    def _clear_map(self):
        os.system('clear')

    def puzzle_two(self):
        self.current_position_x, self.current_position_y = self._get_starting_position()
        self.max_position_x = len(self.data[0]) - 1
        self.max_position_y = len(self.data) - 1
        self.direction = '^'

        answer = []
        while self._check_ahead():
            obstacle_y, obstacle_x = self._place_obstacle()
            direction_at_obstacle = self.direction
            position_x_at_obstacle = self.current_position_x
            position_y_at_obstacle = self.current_position_y
            steps = 0
            while self._check_ahead():
                self._guard_walk()
                steps += 1
                if steps > 20000:
                    answer.append((obstacle_x, obstacle_y))
                    
                    break
            
            self._remove_obstacle(obstacle_y, obstacle_x)
            if answer[-1] == ((obstacle_x, obstacle_y)):
                self.data[obstacle_y] = self._swap(obstacle_x, self.data[obstacle_y], '+')
            self.current_position_x = position_x_at_obstacle
            self.current_position_y = position_y_at_obstacle
            self.direction = direction_at_obstacle
            self._guard_walk()
            self._clear_map()
            self._display_map()
            # sleep(0.03)

        print(answer)
        print(len(answer))
        return len(set(answer))

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())