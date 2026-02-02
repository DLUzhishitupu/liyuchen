new_data = []
with open("./data/train-Together.txt", encoding='utf-8') as f:
    for line in f.readlines():
        
        if "\t" not in line:
            continue
        new_data.append(line)

with open('./data/train.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_data)