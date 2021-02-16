import json

s1 = '{ "name":"bai","area":"SH" }' #定义一个json，外边必须是单引号，里面必须双引号
d1=json.loads(s1)  #将json转换为dict

print(s1,":",type(s1),"\n",d1,":",type(d1)) #看看最后在python中二者是什么类型
#可以看到json是str类型，字典是dict类型