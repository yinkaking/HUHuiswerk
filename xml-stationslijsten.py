import xml.etree.ElementTree as ET
tree = ET.parse('files/stations.xml')
root = tree.getroot()

dictionary = dict()

print("Dit zijn de codes en types van de 4 stations:")
for station in root:
	dictionary[station[0].text] = station
	print(station[0].text + " - " + station[1].text)

print("\nDit zijn alle station met een of meer synoniemen:")
for key, station in dictionary.items():
	for synoniem in station[4]:
		print(key+" - "+synoniem.text)

print("\nDit is de lange naam van elk station")
for key, station in dictionary.items():
	print(key+" - "+station[2][2].text)