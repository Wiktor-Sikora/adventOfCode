from string import ascii_letters, digits
from math import sqrt

class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        with open(path) as f:
            self.data = [line.rstrip() for line in f]

    def _get_position_of_antennas(self, letter:str) -> list:
        positions = []
        for y, line in enumerate(self.data):
            for x, character in enumerate(line):
                if character == letter:
                    positions.append((y, x))
        
        return positions

    def _is_in_bounds(self, y, x):
        return 0 <= y <= self.bound_y and 0 <= x <= self.bound_x

    def _is_empty(self, y, x):
        if self.data[y][x] == '.':
            return True
        else:
            return False
    
    def _is_close(self, y1, y2, x1, x2):
        if abs(y1-y2) + abs(x1-x2) == 1:
            return True
        else:
            return False
        
    def _get_antinode(self, y1, y2, x1, x2):
        antinode = [y1, x1]
        if y1 > y2:
            antinode[0] = y1 + abs(y1 - y2)
        elif y1 < y2:
            antinode[0] = y1 - abs(y1 - y2)
        if x1 > x2:
            antinode[1] = x1 + abs(x1 - x2)
        elif x1 < x2:
            antinode[1] = x1 - abs(x1 - x2)

        return tuple(antinode)

    def _display_map(self, antinodes):
        for antinode in antinodes:
            self.data[antinode[0]] = self.data[antinode[0]][:antinode[1]] + '#' + self.data[antinode[0]][antinode[1] + 1:]
        
        for line in self.data:
            print(line)

    def puzzle_one(self):
        self.ascii_all = ascii_letters + digits
        self.bound_y = len(self.data) - 1
        self.bound_x = len(self.data[0]) - 1
        
        antinodes = []

        for antenanna_letter in self.ascii_all:
            antenannas_positions = self._get_position_of_antennas(antenanna_letter)

            if len(antenannas_positions) < 2:
                continue

            for first_antenna_index, first_antenna in enumerate(antenannas_positions):
                for second_antenna in antenannas_positions[:first_antenna_index] + antenannas_positions[first_antenna_index + 1:]:
                    if self._is_close(first_antenna[0], second_antenna[0], first_antenna[1], second_antenna[1]):
                        continue

                    antinode = self._get_antinode(first_antenna[0], second_antenna[0], first_antenna[1], second_antenna[1])
                    
                    if self._is_in_bounds(antinode[0], antinode[1]):
                        antinodes.append(antinode)

        return len(set(antinodes))

    def _get_antinodes_in_line(self, y1, y2, x1, x2):
        if y1 > y2:
            distance_y = abs(y1-y2)
        else:
            distance_y = -abs(y1-y2)
        if x1 > x2:
            distance_x = abs(x1-x2)
        else:
            distance_x = -abs(x1-x2)

        n = 1
        antinodes = []
        while True:
            antinode = (y2 + distance_y * n, x2 + distance_x * n)
            if self._is_in_bounds(antinode[0], antinode[1]):
                antinodes.append(antinode)
                n += 1
            else:
                break

        return antinodes


    def puzzle_two(self):
        self.get_data('input.txt')
        self.ascii_all = ascii_letters + digits
        self.bound_y = len(self.data) - 1
        self.bound_x = len(self.data[0]) - 1
        
        antinodes = []

        for antenanna_letter in self.ascii_all:
            antenannas_positions = self._get_position_of_antennas(antenanna_letter)

            if len(antenannas_positions) < 2:
                continue

            for first_antenna_index, first_antenna in enumerate(antenannas_positions):
                for second_antenna in antenannas_positions[:first_antenna_index] + antenannas_positions[first_antenna_index + 1:]:
                    if self._is_close(first_antenna[0], second_antenna[0], first_antenna[1], second_antenna[1]):
                        continue

                    antinodes.extend(self._get_antinodes_in_line(first_antenna[0], second_antenna[0], first_antenna[1], second_antenna[1]))

        return len(set(antinodes))

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())