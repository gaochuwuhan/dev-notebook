## list
1. 交集

- nest_ips = [ [], [], [] ]形式里面所有的list取交集放到一个新list中：
   list(set.intersection(*map(set,nest_ips)))

2. 去重

- list1 = [1,2,3,3]
list1=list(set(list1))