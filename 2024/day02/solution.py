class Solution:
    def __init__(self):
        self.get_data()

    def get_data(self, path='input.txt'):
        with open(path) as f:
            self.data = [list(map(int, line.split())) for line in f.readlines()]

    def puzzle_one(self):
        safe = 0
        for report in self.data:
            if report[1] > report[0]:
                increasing = True
            else:
                increasing = False

            for index in range(1, len(report)):
                difference = abs(report[index - 1] - report[index])
                if (difference == 0 or difference > 3) or \
                    (report[index - 1] > report[index] and increasing) or \
                    (report[index - 1] < report[index] and not increasing):
                    break
            else:
                safe += 1

        return safe
    
    def _check_if_safe(self, report):
        if report[1] > report[0]:
            increasing = True
        else:
            increasing = False

        for index in range(1, len(report)):
            difference = abs(report[index - 1] - report[index])
            if (difference == 0 or difference > 3) or \
                (report[index - 1] > report[index] and increasing) or \
                (report[index - 1] < report[index] and not increasing):
                return False
        return True

    def puzzle_two(self):
        safe = 0
        for report in self.data:
            for index in range(len(report)):
                current_value = report[index]
                report.pop(index)
                if self._check_if_safe(report):
                    safe += 1
                    break
                else:
                    report.insert(index, current_value)
                    
        return safe

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())