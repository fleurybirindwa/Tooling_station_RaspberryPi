import bluetooth
import time

print("Searching devices")

def bth_search():
    nearby_devices = bluetooth.discover_devices(duration =3, flush_cache=True)
    print("found %d devices" % len(nearby_devices))

    for addr in nearby_devices:
        try:
            print("%s" %(addr))
        except UnicodeEncodeError:
            print("%s" % (addr.encode('uft-8', 'replace')))

while True:
    bth_search()
    time.sleep(2)
