import os
import requests

if __name__ == '__main__':
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if 'data_about_marathon_runners.txt' not in os.listdir('../Data'):
        print('data_about_marathon_runners loading.')
        url = "https://www.dropbox.com/s/xmsobyv41wz8vb4/data_about_marathon_runners.txt?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/data_about_marathon_runners.txt', 'wb').write(r.content)
        print('Loaded.')

    runners: list[list[str and int]] = []

    with open('../Data/data_about_marathon_runners.txt') as file:
        for line in file:
            runners.append(line.strip().split(','))

    print(runners)
