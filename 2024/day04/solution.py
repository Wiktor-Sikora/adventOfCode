from time import time

class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        self.data = []
        with open(path) as f:
            self.data = [line.rstrip() for line in f]

    def _horizontal_search(self):
        return sum([line.count('XMAS') + line.count('SAMX') for line in self.data])

    def _vertical_search(self):
        answer = 0

        pointer = 0
        end = len(self.data) - 3
        row_length = len(self.data[0])
        while pointer < end:
            for column_index in range(row_length):
                if self.data[pointer][column_index] == 'X':
                    if self.data[pointer + 1][column_index] != 'M':
                        continue
                    if self.data[pointer + 2][column_index] != 'A':
                        continue
                    if self.data[pointer + 3][column_index] == 'S':
                        answer += 1    
                elif self.data[pointer][column_index] == 'S':
                    if self.data[pointer + 1][column_index] != 'A':
                        continue
                    if self.data[pointer + 2][column_index] != 'M':
                        continue
                    if self.data[pointer + 3][column_index] == 'X':
                        answer += 1    

            pointer += 1
        return answer

    def _diagonal_search(self):
        answer = 0
        pointer = 0
        end = len(self.data) - 3
        row_length_right = len(self.data[0]) - 3
        row_length_left = len(self.data[0])
        while pointer < end:
            # searching for \
            for column_index in range(row_length_right):
                if self.data[pointer][column_index] == 'X':
                    if self.data[pointer + 1][column_index + 1] != 'M':
                        continue
                    if self.data[pointer + 2][column_index + 2] != 'A':
                        continue
                    if self.data[pointer + 3][column_index + 3] == 'S':
                        answer += 1    
                elif self.data[pointer][column_index] == 'S':
                    if self.data[pointer + 1][column_index + 1] != 'A':
                        continue
                    if self.data[pointer + 2][column_index + 2] != 'M':
                        continue
                    if self.data[pointer + 3][column_index + 3] == 'X':
                        answer += 1
            # searching for /
            for column_index in range(3, row_length_left):
                if self.data[pointer][column_index] == 'X':
                    if self.data[pointer + 1][column_index - 1] != 'M':
                        continue
                    if self.data[pointer + 2][column_index - 2] != 'A':
                        continue
                    if self.data[pointer + 3][column_index - 3] == 'S':
                        answer += 1    
                elif self.data[pointer][column_index] == 'S':
                    if self.data[pointer + 1][column_index - 1] != 'A':
                        continue
                    if self.data[pointer + 2][column_index - 2] != 'M':
                        continue
                    if self.data[pointer + 3][column_index - 3] == 'X':
                        answer += 1
            pointer += 1
        return answer

    def puzzle_one(self):
        answer = 0
        
        answer += self._horizontal_search()
        answer += self._vertical_search()
        answer += self._diagonal_search()
        
        return answer

    def puzzle_two(self):
        pass

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())