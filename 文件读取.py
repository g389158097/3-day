#先从文件读取开始
f=open(file="D:/python learning.txt",mode='r',encoding='UTF-8')
#r 只读模式
data=f.read()
print(data)

#以什么方式存的编码，就要以什么方式读
#不知道编码 mode选择rb 二进制读取 encoding就不带 用于网络传输，或者打开图片
#循环读取
for line in data:#按行读取
    print(line)
f.close()
