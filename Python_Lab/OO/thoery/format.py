print("hi {0},{0} is a human".format("xiaobai")) #一个位置参数复用多次
print("hi {},this is {}".format("lx","bai")) #通过位置自动填充
print("hi {0},this is {1}".format("lx","bai"))  #按位置序号填充，一定要连续
print("hi {1},this is {0}".format("lx","bai")) #lx代表0，bai代表1
print("hi {0},this is {2}".format("lx","bai")) #错误类型，0下一个参数不能直接是2