from re import findall

class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        with open(path) as f:
            self.data = f.readlines()

    def puzzle_one(self):
        self.data = ''.join(self.data)
        regex = r'(?:mul\()(\d{1,3})(?:\,)(\d{1,3})(?:\))'
        return sum([int(element[0]) * int(element[1]) for element in findall(regex, self.data)])

    def puzzle_two(self):
        self.data = ''.join(self.data)
        answer = 0
        regex = r'(?:mul\()(\d{1,3})(?:\,)(\d{1,3})(?:\))'

        do_index = 0
        dont_index = self.data.index("don't()")
        try: 
            while True:
                answer += sum([int(element[0]) * int(element[1]) for element in findall(regex, self.data[do_index:dont_index])])
                do_index = self.data.index('do()', dont_index + 6)
                dont_index = self.data.index("don't", do_index + 4)
        except ValueError: # no more don't in substring
            return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())
