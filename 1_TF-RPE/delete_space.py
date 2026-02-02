fr = open('D:\PythonProject\Transformer-master+FGM\data/dev_del.txt','r',encoding='utf-8')
fw = open('D:\PythonProject\Transformer-master+FGM\data/dev.txt','w',encoding='utf-8')
lines = fr.readlines()
for i in range(len(lines)):

    fw.write(lines[i][0:lines[i].index('\t')+1])
    fw.write(lines[i][lines[i].index('\t') + 1:-1].replace(' ',''))
    fw.write('\n')

fr.close()
fw.close()