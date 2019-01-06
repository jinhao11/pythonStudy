#使用dict類型進行生肖統計
chineseZodica = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

dict={}
#字典初始化
for i in chineseZodica:
    dict[i] = 0


while True:
    year = int(input("請輸入年份"))

    dict[ chineseZodica[year % 12] ] += 1

    for key in dict.keys():
        print("%s 生肖的數量是 %d" %(key,dict[key]))

