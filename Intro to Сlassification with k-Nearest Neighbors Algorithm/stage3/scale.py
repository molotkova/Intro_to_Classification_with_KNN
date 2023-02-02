
def min_max_scaling(number, lst):
    return (number - min(lst)) / (max(lst) - min(lst))


if __name__ == '__main__':

    runners: list[list[str and int]] = []

    with open('../Data/data_about_marathon_runners.txt') as file:
        for line in file:
            runners.append(line.strip().split(','))

    cross_training = sorted(set([lst[4] for lst in runners]))

    dictionary_vectors: dict[str, list[int]] = {}
    for i, el in enumerate(cross_training):
        string = '0' * i + '1' + (len(cross_training) - i - 1) * '0'
        lst = [int(n) for n in string]
        dictionary_vectors[el] = lst

    y_train = []
    for lst in runners:
        if lst[0] == 'Yes':
            y_train.append(1)
        else:
            y_train.append(0)

        lst[1] = float(lst[1])
        lst[2] = int(lst[2])
        lst[3] = float(lst[3])

        vector = dictionary_vectors[lst[4]]
        lst.extend(vector)
        lst.pop(4)
        lst.pop(0)

    sum_kilometers = [lst[0] for lst in runners]
    age = [lst[1] for lst in runners]
    for i in range(len(runners)):
        runners[i][0] = min_max_scaling(runners[i][0], sum_kilometers)
        runners[i][1] = min_max_scaling(runners[i][1], age)

    print(runners)

#     print("""[[0.5530776092774308, 0.3333333333333333, 1.33, 0, 0, 0, 1], [0.2925958965209634, 0.6666666666666666, 1.44, 0, 1, 0, 0], [0.5700267618198036, 0.16666666666666666, 1.37, 0, 0, 0, 1], [1.0, 0.0, 1.18, 0, 0, 0, 1], [0.4272970561998215, 0.1, 0.86, 0, 0, 0, 1], [0.247992863514719, 0.23333333333333334, 1.82, 1, 0, 0, 0], [0.06244424620874219, 0.5333333333333333, 1.66, 1, 0, 0, 0], [0.17484388938447812, 0.13333333333333333, 1.9, 0, 0, 1, 0], [0.2613737734165923, 1.0, 1.96, 0, 0, 0, 1], [0.0, 0.43333333333333335, 1.78, 0, 0, 1, 0]]
# """)
