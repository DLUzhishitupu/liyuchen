def process_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if len(line) > 150:
                print(line)

if __name__ == '__main__':
    path = './train.txt'
    process_data(path)