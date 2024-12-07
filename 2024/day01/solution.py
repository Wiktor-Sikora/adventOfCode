def get_data(path):
    list_1 = []
    list_2 = []
    f = open(path)
    for line in f.readlines():
        list_1.append(int(line.split('   ')[0]))
        list_2.append(int(line.split('   ')[1]))

    f.close()
    return list_1, list_2

def solution(list_1, list_2):
    total_distance = 0
    list_1.sort()
    list_2.sort()

    for index in range(len(list_1)):
        total_distance += abs(list_1[index] - list_2[index])
    
    return total_distance

if __name__ == '__main__':
    list_1, list_2 = get_data('input.txt')
    print(solution(list_1, list_2))