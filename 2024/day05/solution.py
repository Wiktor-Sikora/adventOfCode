class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        with open(path) as f:
            lines = f.readlines()
            self.rules = [tuple(map(int, line.rstrip().split('|'))) for line in lines[:lines.index('\n')]]
            self.pages = [list(map(int, line.rstrip().split(','))) for line in lines[lines.index('\n') + 1:]]

    def _binary_check_if_rule_exists(self, value_1:int, value_2:int):
        value_to_search = int(f'{value_1}{value_2}') 
        start = 0
        end = len(self.rules) - 1
        middle = 0
        while start <= end:
            middle = (start + end) // 2
            
            if int(f'{self.rules[middle][0]}{self.rules[middle][1]}') < value_to_search:
                start = middle + 1
            
            elif int(f'{self.rules[middle][0]}{self.rules[middle][1]}') > value_to_search:
                end = middle - 1 
            
            else:
                return True
        
        return False 

    def _get_rules_for_case(self, line:list):
        rules_for_case = []
        for number_1 in line:
            for number_2 in line:
                if self._binary_check_if_rule_exists(number_1, number_2):
                    rules_for_case.append((number_1, number_2))

        return rules_for_case

    def _is_line_valid(self, line:list, rules_for_case:list):
        for rule in rules_for_case:
            first_number_index = line.index(rule[0])
            second_number_index = line.index(rule[1])

            if first_number_index > second_number_index:
                return False
        return True

    def puzzle_one(self):
        self.get_data()
        self.rules.sort(key=lambda rule: int(str(rule[0]) + str(rule[1])))
        answer = 0

        for line in self.pages:
            current_rules = self._get_rules_for_case(line)
            if self._is_line_valid(line, current_rules):
                answer += line[len(line) // 2]
        
        return answer

    def puzzle_two(self):
        self.get_data()
        self.rules.sort(key=lambda rule: int(str(rule[0]) + str(rule[1])))
        answer = 0
        
        for line in self.pages:
            current_rules = self._get_rules_for_case(line)

            if self._is_line_valid(line, current_rules):
                continue

            for rule in current_rules:
                first_number_index = line.index(rule[0])
                second_number_index = line.index(rule[1])

                if first_number_index > second_number_index:
                    line.pop(first_number_index)
                    line.insert(second_number_index, rule[0])

            answer += line[len(line) // 2]
        return answer

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())