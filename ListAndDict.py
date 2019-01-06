#列表和字典推导式联系
#实例  1~10中的偶数放入列表

aList=[];
for i in range(1,11):
    if(i % 2 == 0):
        aList.append(i*i)
print(aList)


aList1=[ i*i for i in range(1,11) if( i % 2 == 0) ]
print(aList1)


chineseZodica = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
bDict={}
for i in chineseZodica:
    bDict[i]=0
print(bDict)


bDict1={i:0 for i in chineseZodica}
print(bDict1)
