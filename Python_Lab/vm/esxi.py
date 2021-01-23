from pyVmomi import *
from pyvim import *

host='192.168.88.13'
user='Administrator@vsphere.local'
password='Binqsoft01'
port=443#端口
context = None
if hasattr(ssl, '_create_unverified_context'):
    context = ssl._create_unverified_context()
si = SmartConnect(host=host,user=user,pwd=password,port=port,sslContext=context)
if not si:
    print("帐号密码有问题")
atexit.register(Disconnect, si)
 
 
###################################################################################################
def WaitForTasks(tasks, si):#任务
    pc = si.content.propertyCollector
    taskList = [str(task) for task in tasks]
    objSpecs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task) for task in tasks]
    propSpec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,pathSet=[], all=True)
    filterSpec = vmodl.query.PropertyCollector.FilterSpec()
    filterSpec.objectSet = objSpecs
    filterSpec.propSet = [propSpec]
    filter = pc.CreateFilter(filterSpec, True)
    try:
        version, state = None, None
        while len(taskList):
            update = pc.WaitForUpdates(version)
            for filterSet in update.filterSet:
                for objSet in filterSet.objectSet:
                    task = objSet.obj
                    for change in objSet.changeSet:
                        if change.name == 'info':
                            state = change.val.state
                        elif change.name == 'info.state':
                            state = change.val
                        else:
                            continue
                        if not str(task) in taskList:
                            continue
                        if state == vim.TaskInfo.State.success:
                            taskList.remove(str(task))
                        elif state == vim.TaskInfo.State.error:
                            raise task.info.error
            version = update.version
    finally:
        if filter:
            filter.Destroy()
def getvmname():#打印所有虚拟机名
    content = si.RetrieveContent()
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            datacenter = child
            vmFolder = datacenter.vmFolder
            vmList = vmFolder.childEntity
            for vm in vmList:
                print(vm.summary.config.name)
                print(vm.name)
def getvmstatus(vm_name):#获取虚拟机状态
    content = si.RetrieveContent()
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            datacenter = child
            vmFolder = datacenter.vmFolder
            vmList = vmFolder.childEntity
            for vm in vmList:
                if vm.summary.config.name == vm_name :
                    print(vm.summary.runtime.powerState)
 
