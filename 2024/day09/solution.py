class Solution:
    def __init__(self):
        self.get_data()
        
    def get_data(self, path='input.txt'):
        with open(path) as f:
            self.data = tuple(map(int, f.readline()))

    def puzzle_one(self):
        # self.get_data('example'.txt')
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

        while True:
            if parsed_data[end_index] == '.':
                end_index -= 1
            elif end_index < last_free_index:
                break
            else:
                parsed_data[last_free_index] = parsed_data[end_index]
                # parsed_data[end_index] = '.'
                end_index -= 1
                last_free_index = parsed_data.index('.', last_free_index)

        return sum([index * parsed_data[index] for index in range(end_index+1)])

    def _get_index_of_free_space(self, iter:list, start:int, end:int, length:int):
        for item in range(start, end):
            if iter[item][1] == 0 and iter[item][0] >= length:
                return item
        else:
            return None

    def puzzle_two(self):
        self.get_data('example.txt')
        # counted_free_space = []
        counted_data = []
        
        is_free_space = False
        current_id = 0
        for number in self.data:
            if number == 0:
                is_free_space = not is_free_space
                continue

            if is_free_space:
                # number, is_free, start, end
                counted_data.append([number, 0])
            else:
                # 'id' * number, is_free, start, end 
                counted_data.append((str(current_id) * number, 1))
                current_id += 1

            is_free_space = not is_free_space
        
        
        end_index = len(counted_data) - 1
        while counted_data[end_index][1] == 0:
            end_index -= 1

        while end_index > 1:
            if counted_data[end_index][1] == 0:
                end_index -= 1
                continue

            end_index_length = len(counted_data[end_index][0])
            free_index = self._get_index_of_free_space(counted_data, 1, end_index - 1, end_index_length)
            if not free_index:
                end_index -= 1
            elif counted_data[free_index][0] == end_index_length:
                counted_data.insert(free_index, counted_data[end_index])
                counted_data.pop(free_index + 1)
                counted_data.pop(end_index)
                counted_data.insert(end_index, (end_index_length, 0))
                end_index -= 1
            else:
                counted_data[free_index][0] -= end_index_length
                counted_data.insert(free_index, counted_data[end_index])
                counted_data.pop(end_index + 1)
                counted_data.insert(end_index + 1, (end_index_length, 0))
                end_index -= 1

        answer = 0
        item_id = 0
        print(counted_data)
        for item in counted_data:
            if item[1] == 0:
                item_id += 1
                continue
            
            for number in item[0]:
                print(f'{number}*{item_id}', end=' ')
                answer += int(number) * item_id
                item_id += 1

        return answer

        

if __name__ == '__main__':
    solution = Solution()
    print(solution.puzzle_one())
    print(solution.puzzle_two())