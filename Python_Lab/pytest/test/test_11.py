import pytest
import requests

class Baidu():
    url="http://www.google.com"
    def get_baidu(self):
        res=requests.get(self.url)
        return res.status_code
        # assert res.status_code == 200
    
def test_res():
    Baidu().get_baidu()
# print(Baidu().get_baidu())
