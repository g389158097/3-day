#读写混合模式 r+
f=open(file="D:/python learning.txt",mode='w+',encoding='UTF-8')
data=f.read()
print(data)
f.write('123')
print(data)
f.close()
#read是不会往前读取的
#w+写读模式 先写入，读取的是空白
#新写的是可以读的
