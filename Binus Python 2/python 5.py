import math 

lonA = float(input("Enter Longitude Titik A: "))
latA = float(input("Enter Latitude Titik A: "))
lonB = float(input("Enter Longitude Titik B: "))
latB = float(input("Enter Latitude Titik B: "))
R = 6371.0 
phi1 = math.radians(latA)
phi2 = math.radians(latB)
deltaphi = math.radians (latB - latA)
deltalambda = math.radians (lonB - lonA)

a = math.sin (deltaphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(deltalambda/2)**2 
c = 2* math.atan2(math.sqrt(a), math.sqrt(1-a)) 
distance = R * c 

print("Jarak dari titik A sampai titik B " + str(distance) +"km")