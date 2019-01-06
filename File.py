#文件编写
file1 = open("name.txt","w")
file1.write("刘备")
file1.close()

#文件的读取
file2 = open("name.txt")
print(file2.read())
file2.close()


#文件内容的添加
file3 = open("name.txt","a")
file3.write("\n关羽")
file3.close()
file4 = open("name.txt","r")

print(file4.read())
file4.close()




