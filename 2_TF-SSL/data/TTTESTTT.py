f_ = open('C:/Users/Dester/Desktop/新建文件夹/111.txt', 'r',encoding='utf8')
n = 0
list1 = []
for i in f_.readlines():
    n += 1
    s = i.strip()
    list1.append(s)
f_.close()

ff_ = open('C:/Users/Dester/Desktop/新建文件夹/222.txt', 'r',encoding='utf8')
m = 0
list2 = []
for i in ff_.readlines():
    m += 1
    s = i.strip()
    list2.append(s)
ff_.close()

fff_ = open('C:/Users/Dester/Desktop/新建文件夹/333.txt', 'w',encoding='utf8')
for i in range(n):
    if len(list1[i]) > 100 or len(list2[i]) > 200:
        continue
    s = list1[i] + '\t' + list2[i]
    fff_.write(s + '\n')

fff_.close() 