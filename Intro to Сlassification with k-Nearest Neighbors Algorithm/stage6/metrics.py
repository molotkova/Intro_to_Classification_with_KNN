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

def binary_classification_metrics(pred, true):
    TP = 0  # Should be positive and is positive
    FP = 0  # Should be negative and is positive
    TN = 0  # Should be negative and is negative
    FN = 0  # Should be positive and is negative

    for i in range(len(pred)):
        if pred[i]:
            if pred[i] == true[i]:
                TP += 1
            else:
                FN += 1
        elif not pred[i]:
            if pred[i] == true[i]:
                TN += 1
            else:
                FP += 1

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = (2 * TP) / (2 * TP + FP + FN)

    print(f'Accuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}\nF-score: {f1}')


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


    def predict(nested_lst, k=1):
        predicted = []
        for lst in nested_lst:
            dists = calc_dists(lst)
            result = k_closest_labels(dists, k)
            if result.count(0) > result.count(1):
                predicted.append(0)
            else:
                predicted.append(1)
        return predicted


    def k_closest_labels(dists, k=1):
        dists_and_labels = {d: y_train[i] for i, d in enumerate(dists)}
        labels = [label for dist, label in sorted(dists_and_labels.items())[:k]]
        return labels


    test_vector_2 = [210, 39, 3.19, 'cycling 3h']
    test_vector_2[0] = min_max_scaling(test_vector_2[0], sum_kilometers)
    test_vector_2[1] = min_max_scaling(test_vector_2[1], age)
    test_vector_2.extend(dictionary_vectors[test_vector_2[3]])
    test_vector_2.pop(3)

    test_vector_3 = [518, 33, 3.12, 'nothing']
    test_vector_3[0] = min_max_scaling(test_vector_3[0], sum_kilometers)
    test_vector_3[1] = min_max_scaling(test_vector_3[1], age)
    test_vector_3.extend(dictionary_vectors[test_vector_3[3]])
    test_vector_3.pop(3)

    test_result_1 = predict([test_vector, test_vector_2, test_vector_3], k=1)
    test_result_3 = predict([test_vector, test_vector_2, test_vector_3], k=3)
    test_result_5 = predict([test_vector, test_vector_2, test_vector_3], k=5)


    print('Metric values when k = 1:')
    binary_classification_metrics(test_result_1, [1, 0, 0])
    print('Metric values when k = 3:')
    binary_classification_metrics(test_result_3, [1, 0, 0])

