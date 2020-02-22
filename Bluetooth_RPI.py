import bluetooth


def list_detected_BT
	temp_MAC_list=[]
	MAC_addr_list=[]
	nearby_devices = bluetooth.discover_devices()
	
	for addr in nearby_devices:
		temp_MAC_list.append(addr)
		#print " %s" % (addr)
	differences_between_lists = temp_MAC_list.difference(MAC_addr_list)
	MAC_addr_list.append(diffrences_between_lists)
	#Send "diffrences_between_lists" to firebase
	
	