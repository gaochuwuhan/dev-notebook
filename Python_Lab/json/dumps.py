import json
from typing import Dict, List, Type
from collections import defaultdict

# class CRUDTask:
#     def __init__(self, path: str, model: Type[ProbeTask], group_by_fields: List[str]):  #将 ProbeTask中的属性（msg_id和client传到model参数），多个subnet作为list传到group_by_fields
#         self.group_by_fields = group_by_fields
#         super().__init__(path, model)

def send_tasks(params: List[Dict[str, str]],group_by_fields:List[str]):
    ip_range_by_probe = defaultdict(list)  #defaultdict(list),会构建一个默认value为list的字典，目前是空
    for param in params:
        print(param,group_by_fields,ip_range_by_probe)
        # temp_dict = {field: param[field] for field in group_by_fields}
        # print(temp_dict, 1111)
        key = json.dumps({field: param[field] for field in group_by_fields}) 
        ip_range_by_probe[key].append(param["subnet"])
    print(ip_range_by_probe)

send_tasks([{"scan_type":"深度发现"}],['192.168.10.7','192.168.10.19'])
