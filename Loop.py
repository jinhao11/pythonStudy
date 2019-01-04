chineseZodica = '鼠牛虎兔龍蛇馬羊猴雞狗豬'

for cz in chineseZodica:
    print(cz)

for i in range(1,13):
    print(i)

for year in range(2000,2019):
    print("%s 年的生肖时 %s"  %(year,chineseZodica[year%12-4]))

