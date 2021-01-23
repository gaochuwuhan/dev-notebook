import psycopg2
#创建一个connection类
conn = psycopg2.connect(dbname="apiapp", user="apiapp",
        password="Password01!", host="192.168.88.163", port="5432")
cur = conn.cursor()  #创建一个cursor类，用来在Session执行psql命令     
fields = ("task_id", "state", "data")

sql_str = (
            f"select task_id from api_childscantask where id in "
            "(select childscantask_id from api_discovertask_child_tasks "
            f"where discovertask_id = 244)"
        )

cur.execute(sql_str) 
res =  cur.fetchall()
task_id=str(list(map(lambda x: x[0], res)))
# print('task id is',task_id)
sqls = (
    f"select {','.join(fields)} from api_childscantask "  #查询fields对应的字段
    f"where task_id= 'e375eb03-2e48-4d47-ab18-a0ce6c7713c8'")
# print(sqls)
cur.execute(sqls)
res2=cur.fetchall()
# print(res2)
conn.close()
# def res(res):
task = dict(zip(fields,res2[0]))
class Task:
    # def __init__(self,task):
        
    def get_task_state(self):
        state=task['state']
        return state

    def is_task_finished(self):
        state = self.get_task_state()
        return state in ("done", "failed")

    def is_task_successed(self):
        state = self.get_task_state()
        print(f"任务状态是{state}")
        return state == "success"
print(Task().get_task_state())
print(Task().is_task_finished())


