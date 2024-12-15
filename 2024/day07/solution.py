import binascii


class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        self.data = []
        with open(path) as f:
            for line in f:
                items = line.rstrip().split(': ')
                self.data.append((int(items[0]), tuple(map(int, items[1].split(' ')))))

    def _is_possible(self, number:int, current_number:int, factors:list):
        if len(factors) > 1:
            if current_number + factors[0] > number:
                return False
            elif current_number * factors[0] == number or current_number + factors[0] == number:
                return True
            else:
                return self._is_possible(number, current_number + factors[0], factors[1:]) or self._is_possible(number, current_number * factors[0], factors[1:])
        elif current_number * factors[0] == number or current_number + factors[0] == number:
            return True
        else:
            return False

    def puzzle_one(self):
        return sum(line[0] for line in self.data if self._is_possible(line[0], line[1][0], line[1][1:]))

    def _is_possible_2(self, number:int, current_number:int, factors:list):
        if len(factors) > 1:
            if current_number + factors[0] > number:
                return False
            elif current_number * factors[0] == number or\
                 current_number + factors[0] == number or\
                 int(f'{current_number}{factors[0]}') == number:
                return True
            else:
                return self._is_possible_2(number, current_number + factors[0], factors[1:]) or\
                       self._is_possible_2(number, current_number * factors[0], factors[1:]) or\
                       self._is_possible_2(number, int(f'{current_number}{factors[0]}'), factors[1:])
        elif current_number * factors[0] == number or current_number + factors[0] == number or int(f'{current_number}{factors[0]}') == number:
            return True
        else:
            return False

    def puzzle_two(self):
        return sum(line[0] for line in self.data if self._is_possible_2(line[0], line[1][0], line[1][1:]))

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())