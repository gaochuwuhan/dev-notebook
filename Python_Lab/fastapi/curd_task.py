from collections import defaultdict
from typing import Dict, List, Type
from app.crud.http.crud_probe_base import HttpProbeBase
from uuid import uuid4
from app.schemas.diting.schema_probe import ErrorscanTasktype
from probe.schemas.probe_task_schema import ProbeTask
import logging as logger
import json


class CRUDTask(HttpProbeBase[ProbeTask]):
    def __init__(self, path: str, model: Type[ProbeTask], group_by_fields: List[str]):  #将 ProbeTask中的属性（msg_id和client传到model参数），多个subnet作为list传到group_by_fields
        self.group_by_fields = group_by_fields
        super().__init__(path, model)

    def send_tasks(self, params: List[Dict[str, str]], tasktype):
        ip_range_by_probe = defaultdict(list)  #defaultdict(list),会构建一个默认value为list的字典，目前是空
        for param in params:
            key = json.dumps({field: param[field] for field in self.group_by_fields}) 
            ip_range_by_probe[key].append(param["subnet"]) #返回一个以subnet为key的字典放进ip_range_by_probe
        res = []
        for key, ip_range in ip_range_by_probe.items():
            group_by_key_value = json.loads(key)
            probe_ip = group_by_key_value.get("probe_ip")

            body = dict(
                **group_by_key_value,
                ip_range=ip_range,
                tasktype=tasktype,
                client=self.client,
                msg_id=uuid4(),
            )
            if not probe_ip:
                logger.error(f"下发任务失败{body=}, probe ip 找不到")
                continue
            self.base_url = self.get_url(probe_ip, 4000, self.path)
            probe_res = super().create(body)
            if probe_res and isinstance(probe_res, dict) and probe_res.get("ok"):
                res.append(body)
            else:
                logger.error(f"下发任务失败{body=}, {probe_res=}")
        return res

    def send_error_tasks(self, params: List[Dict]):
        params_by_probe = defaultdict(list)
        for param in params:
            params_by_probe[param.get("probe_ip")].append(param)

        res = []
        for probe_ip, task_params in params_by_probe.items():
            self.base_url = self.get_url(probe_ip, 4000, self.path)

            body = dict(
                params=task_params,
                client=self.client,
                msg_id=uuid4(),
                tasktype=ErrorscanTasktype.errorscan,
            )
            probe_res = super().create(body)
            if probe_res.get("ok"):
                res.append(body)
            else:
                logger.error(f"下发任务失败{body=}, {probe_res=}")
        return res
