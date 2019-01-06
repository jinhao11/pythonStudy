zodicaName = (u'摩羯座',u'水瓶座',u'双鱼座')
zodicaDays = ((1,20),(2,19),(3,21))

intMonth = int(input('请输入月份: '))
intDay = int(input('请输入日期: '))
n=0
while zodicaDays[n] <= (intMonth,intDay):
    if( zodicaDays[n] >= (3,21) ):
        break
    n += 1
    print(n)