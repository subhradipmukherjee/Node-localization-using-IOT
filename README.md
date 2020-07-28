# Node-localization-using-IOT
Fetching the location of indoor object connected in  IOT network using trilateration and rssi method without direct use of gps modules
gps.py - this code is uploaded in raspberry pi to which a gps node is attached which fetches the co-ordinates of this anchor nodes.
rssi.py - this code calculates approx distance btw 2 nodes based on strength of signal transmitted
tri.py - this code is used for implementing trilateration method which helps in finding the cordinates of non-anchor nodes to which gps module is not connected.
