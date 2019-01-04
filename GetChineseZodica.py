#记录生肖
chineseZodica = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
#input 为控制台输入语句
year = int(input('请输入出生年份\n'))
zodicaNum = year%12
print( chineseZodica[zodicaNum-4] )

print( "兔" in chineseZodica)