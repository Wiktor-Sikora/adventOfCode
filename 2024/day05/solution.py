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
            print(counted_rules)
            if self.rules[rule_index][0] != self.rules[rule_index - 1][0]:
                counted_rules[self.rules[rule_index - 1][0]] = (self.rules[rule_index - 1][0], first_index, rule_index - 1)
                first_index = rule_index
        return counted_rules


    def puzzle_one(self):
        self.get_data()
        counted_rules = self._get_counted_rules()
        print(counted_rules)

        for line in self.pages:
            for page in line:
                # print(self.rules[self._rules_binary_search(page)])


    def puzzle_two(self):
        pass

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())