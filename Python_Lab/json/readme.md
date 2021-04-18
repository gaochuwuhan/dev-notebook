- json在python中是一个str类型
json.loads() 可以将一个json字符串转换为字典
json.dumps() 可以将一个字典转换为json字符串

JSONParser().parse(request)  将request的body转换成字典
JSONRenderer().render(ArticleSerilizers(instance=queryset,many=True)) 将序列化后的drf类型转换为byte类型