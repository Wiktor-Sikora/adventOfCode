class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        with open(path) as f:
            lines = f.readlines()
            self.rules = [tuple(map(int, line.rstrip().split('|'))) for line in lines[:lines.index('\n')]]
            self.pages = [list(map(int, line.rstrip().split(','))) for line in lines[lines.index('\n') + 1:]]

    def _get_counted_rules(self):
        counted_rules = [None for _ in range(0, 100)]

        first_index = 0
        for rule_index in range(1, len(self.rules)):
            if self.rules[rule_index][0] != self.rules[rule_index - 1][0]:
                counted_rules[self.rules[rule_index - 1][0]] = (first_index, rule_index - 1)
                first_index = rule_index
        return counted_rules

    def _get_index(self, value:int, iterable:list):
        for index in range(len(iterable) - 1):
            if iterable[index] == value:
                return index
        else:
            return False

    def _is_line_valid(self, line:list):
        for index, number in enumerate(line):
            for rule in self.rules[self.counted_rules[number][0]:self.counted_rules[number][1]]:
                second_number_index = self._get_index(rule[1], line)
                if not second_number_index:
                    continue
                elif index > second_number_index:
                    return False
        return True

    def puzzle_one(self):
        self.get_data()
        self.counted_rules = self._get_counted_rules()

        return sum([line[len(line) // 2] for line in self.pages if self._is_line_valid(line)])

    def _correct_ordering(self, line):
        pass

    def puzzle_two(self):
        self.get_data()
        self.counted_rules = self._get_counted_rules
        answer = 0

        for line in self.pages:
            if self._is_line_valid(line):
                continue
            
            line = self._correct_ordering(line)
            
            answer += line[len(line) // 2]

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())