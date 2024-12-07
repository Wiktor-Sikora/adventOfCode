def get_data(path):
    list_1 = []
    list_2 = []
    f = open(path)
    for line in f.readlines():
        list_1.append(int(line.split('   ')[0]))
        list_2.append(int(line.split('   ')[1]))

    f.close()
    return list_1, list_2

def get_counted_list(array, end):
    counted_list = [0 for _ in range(end)]

    for number in array:
        counted_list[number - 1] += 1
    
    return counted_list

def solution(list_1, list_2):
    similarity_score = 0

    list_1_max = max(list_1)
    list_2_max = max(list_2)
    if list_1_max > list_2_max:
        counted_list_2 = get_counted_list(list_2, list_1_max)
    else:
        counted_list_2 = get_counted_list(list_2, list_2_max)

    for number in list_1:
        similarity_score += number * counted_list_2[number - 1]

    return similarity_score

if __name__ == '__main__':
    list_1, list_2 = get_data('input.txt')
    print(solution(list_1, list_2))