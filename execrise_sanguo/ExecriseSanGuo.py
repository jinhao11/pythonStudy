import re

#从文本中统计人物、武器的出现次数

#从给定名称的文件中，返回str出现的次数
def findStrTime(str,fileName):
    with open(fileName,encoding='UTF-8') as file:
        data = file.read().replace('\n','')
        num = re.findall(str,data)
        print(' %s  出现 %s  次' % (str, len(num)))
    return len(num)


#1.从name.txt读取人名

name_dict =  {}
with open('name.txt',encoding='UTF-8') as f:
    for line in f:
        names = line.replace("\n","").split("|")
        for n in names:
            name_dict[n] = findStrTime(n,"sanguo_utf8.txt")
print(name_dict)
