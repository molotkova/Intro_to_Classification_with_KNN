import os
import requests
import sys

if __name__ == '__main__':
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if 'data_about_marathon_runners.txt' not in os.listdir('../Data'):
        sys.stderr.write("[INFO] Dataset is loading.\n")
        url = "https://www.dropbox.com/s/xmsobyv41wz8vb4/data_about_marathon_runners.txt?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/data_about_marathon_runners.txt', 'wb').write(r.content)
        sys.stderr.write("[INFO] Loaded.\n")

    runners: list[list[str and int]] = []

    with open('../Data/data_about_marathon_runners.txt') as file:
        for line in file:
            runners.append(line.strip().split(','))

    print(runners)
#    print("""[['Yes', '330.8', '35', '1.33', 'nothing'], ['Yes', '214', '45', '1.44', 'cycling 4h'], ['Yes', '338.4', '30', '1.37', 'nothing'], ['Yes', '531.2', '25', '1.18', 'nothing'], ['Yes', '274.4', '28', '0.86', 'nothing'], ['No', '194', '32', '1.82', 'cycling 3h'], ['No', '110.8', '41', '1.66', 'cycling 3h'], ['No', '161.2', '29', '1.9', 'cycling 5h'], ['No', '200', '55', '1.96', 'nothing'], ['No', '82.8', '38', '1.78', 'cycling 5h']]
# """)
