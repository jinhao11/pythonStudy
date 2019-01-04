#元组比较大小
a=(1,3,5,7)
b=4
print( list( filter(lambda x:x<=b,a) ))

zodiacName=(u'摩羯',u'水瓶');
zodiacDays={(1,20),(2,19)}
(month,day) = (1,20)

print(type((month,day)))

zodiacDay = filter(lambda x: x>=(month, day),zodiacDays)
print(zodiacDay)
zodac_len = len(list(zodiacDay)) % 12
print(zodac_len)


