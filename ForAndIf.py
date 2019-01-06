zodicaName = (u'摩羯座',u'水瓶座',u'双鱼座')
zodicaDays = ((1,20),(2,19),(3,21))



for num in range(len(zodicaDays)):
    print(zodicaName[num])

intMonth = int(input('请输入月份: '))
intDay = int(input('请输入日期: '))
for num in range(len(zodicaDays)):
    if zodicaDays[num] >= (intMonth, intDay):
        print(zodicaName[num])
        break;