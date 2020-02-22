import bluetooth

def list_detected():
    mac_addr_list=[]
    nearby_devices = bluetooth.discover_devices()


    for addr in nearby_devices:
       mac_addr_list.append(addr)

       print(mac_addr_list)



