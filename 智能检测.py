import chardet
#检测rb转换的编码是什么
f=open(file="D:/python learning.txt",mode='rb')
data=f.read()
print(data)
c=chardet.detect(data)
print(c)
f.close()
#confidence 置信程度
