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

#    print("""[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#[[330.8, 35, 1.33, 0, 0, 0, 1], [214.0, 45, 1.44, 0, 1, 0, 0], [338.4, 30, 1.37, 0, 0, 0, 1], [531.2, 25, 1.18, 0, 0, 0, 1], [274.4, 28, 0.86, 0, 0, 0, 1], [194.0, 32, 1.82, 1, 0, 0, 0], [110.8, 41, 1.66, 1, 0, 0, 0], [161.2, 29, 1.9, 0, 0, 1, 0], [200.0, 55, 1.96, 0, 0, 0, 1], [82.8, 38, 1.78, 0, 0, 1, 0]]
#""")
