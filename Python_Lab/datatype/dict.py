lists = []
data={"value":1,"name":"network"}
item=[{"value":11,"name":"plc","is_leaf":True},{"value":21,"name":"hmi","is_leaf":True}]
re = data.update({"children": item})
lists.append(data)
print (lists)