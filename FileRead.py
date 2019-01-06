#当行读取
file5 = open("file.txt","w")
file5.write("1关羽")
file5.write("2张飞")
file5.write("3刘备")
file5.close()

file6 = open("file.txt")
print(file6.tell())

print(file6.read(0))
print(file6.read(1))
print(file6.read(2))

