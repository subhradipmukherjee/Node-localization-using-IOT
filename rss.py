import rssi

def radius():
	interface = 'wlan0'
	rssi_scanner = rssi.RSSI_Scan(interface)
	ssids = ['Aj*','linksys']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.
	ap_info = rssi_scanner.getAPinfo(networks=ssids,sudo=True)
#dist = rssi_scanner.getDistanceFromAP(sudo=True)

	#print(ap_info[0]['signal'])
	
	#calculating the distance using the formula
	rss=ap_info[0]['signal']
	Ptx=-63
	n = 1.8
	distance =  10**((Ptx-rss)/(10*n))
	return (distance)

