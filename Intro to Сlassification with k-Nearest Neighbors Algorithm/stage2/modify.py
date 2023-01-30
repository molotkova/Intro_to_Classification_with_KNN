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

    print(y_train)
    print(runners)
