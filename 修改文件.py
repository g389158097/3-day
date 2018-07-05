import os
#seek完后直接write会覆盖文件原来的内容
#那修改呢？
#文件在硬盘上创建了，长度就是固定的，不能顺延
#word等可以修改的原理是先加载到内存上，完事再覆盖过去
#所以可以一行一行的读，一边读一边写
#修改占硬盘
#修改占内存
f_name='py'
f_new_name='py.new'
old_str='崔'
new_str='秉'
f=open(f_name,'r',encoding='utf-8')
f_new=open(f_new_name,'w',encoding='utf-8')
for line in f:
    if old_str in line:
        line=line.replace(old_str,new_str)
    f_new.write(line)
f.close()
f_new.close()
#import os调用系统命令
os.rename(f_new_name,f_name)
