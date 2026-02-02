fr = open("./data/train1.txt", 'r',encoding='utf-8')
fw = open("./data/train.txt", 'w',encoding='utf-8')
lines = fr.readlines()

for i in range(len(lines)):
    if len(lines[i]) <= 180:
        fw.write(lines[i])

fr.close()
fw.close()