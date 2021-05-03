from api_probe import All_probe
from api_device import All_device

def read_probes():
    list_,total=All_probe().get_multi()
    id = []
    for probe in list_:
        id.append(probe.pop("device_id"))
        print(probe,id)
    probes = [
        dict(**probe,device=All_device.get_id(id=id))
        # for probe in list_
    ]

    return dict(list=probes,total=total)
    # return id

print(read_probes())