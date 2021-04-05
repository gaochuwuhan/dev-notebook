from requests.api import get #request.get()的源路径，可以查看源码看看他的源参数有url,parms=None;post(url, data=None, json=None, **kwargs);patch(url, data=None, **kwargs);delete(url, **kwargs);put(url, data=None, **kwargs)


'''自定义请求头headers,如果为http添加头部，要传一个dict给headers参数。
    headers可以是api key
'''

key_headers = {"AUTHORIZATION":"Api-Key edsi12eosnfgh"}
res = request.get(headers=key_headers,url=http://ds.wudun.net:8001/tasks)
