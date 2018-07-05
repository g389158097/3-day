f=open(file="D:/python learning.txt",mode='a',encoding='UTF-8')
f.write('1212')
f.close()
#写入的同时会创建一个新文件
#wb二进制写入
#w永远不是修改模式，是创建模式，所以w应该尽量慎用




#追加模式 w变成a
#总结 读 写 追加
