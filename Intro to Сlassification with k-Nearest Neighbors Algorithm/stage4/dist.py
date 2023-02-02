def euclidean_distance(point_1, point_2):
    sum_squared_distance = 0
    for i in range(len(point_1)):
        sum_squared_distance += (point_1[i] - point_2[i]) ** 2
    return sum_squared_distance ** 0.5


def calc_dists(x):
    dists = [euclidean_distance(x, x_train) for x_train in runners]
    return dists


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

    test_vector = [424, 40, 1.42, 'nothing']
    test_vector[0] = min_max_scaling(test_vector[0], sum_kilometers)
    test_vector[1] = min_max_scaling(test_vector[1], age)
    test_vector.extend(dictionary_vectors[test_vector[3]])
    test_vector.pop(3)

    print(calc_dists(test_vector))

    # print("""[0.2812106966355265, 1.4991706027951892, 0.3873684238031154, 0.6039499515901134, 0.7647937207067647, 1.579307855293723, 1.5958039687009598, 1.6457031105319977, 0.8894684753340013, 1.6471355362092108]""")