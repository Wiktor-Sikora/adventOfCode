class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        with open(path) as f:
            self.data = tuple(map(int, f.readline()))

    def puzzle_one(self):
        self.get_data('example.txt')
        parsed_data = []

        is_free_space = False
        current_id = 0
        for number in self.data:
            if is_free_space:
                for _ in range(number):
                    parsed_data.append('.')

            else:
                for _ in range(number):
                    parsed_data.extend(tuple(map(int, str(current_id).split())))
            
                current_id += 1

            is_free_space = not is_free_space

        last_free_index = parsed_data.index('.')
        end_index = len(parsed_data) - 1
        print(parsed_data)
        while True:
            if parsed_data[end_index] == '.':
                end_index -= 1
            elif end_index < last_free_index:
                break
            else:
                parsed_data[last_free_index] = parsed_data[end_index]
                parsed_data[end_index] = '.'
                end_index -= 1
                last_free_index = parsed_data.index('.')
            print(parsed_data)
        print(parsed_data)

        return sum([index * parsed_data[index] for index in range(len(parsed_data) - 1)])

    def puzzle_two(self):
        pass

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())