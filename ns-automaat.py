stations = [
	"Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk",
	"Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven",
	"Weert", "Roermond", "Sittard", "Maastricht"
]

def inlezen_beginstation(stations):
	stationsNaam = input("Uw Beginstation: ")
	if stationsNaam in stations:
		if stationsNaam == "Maastricht":
			print("Dit is het eindstation, je kan hier niet beginnen.")
			stationsNaam = inlezen_beginstation(stations)
	else:
		print("Dit station bestaat niet, Probeer het opnieuw")
		stationsNaam = inlezen_beginstation(stations)
	return stationsNaam

def inlezen_eindstation(stations, beginstation):
	stationsNaam = input("Uw Eindstation: ")
	if stationsNaam not in stations or stations.index(beginstation) >= stations.index(stationsNaam):
		print("Probeer het opnieuw, dit station bestaat niet of is niet bereikbaar vanaf uw beginstation")
		stationsNaam = inlezen_eindstation(stations, beginstation)
	else:
		return stationsNaam

def omroepen_reis(stations, beginstation, eindstation):
	stationBeginNummer = stations.index(beginstation) + 1
	stationEindNummer = stations.index(eindstation) + 1
	afstandStations = stations.index(eindstation) - stations.index(beginstation)

	print("Het beginstation " + beginstation + " is het "+ str(stationBeginNummer) + "e station in het traject.")
	print("Het eindstation " + eindstation + " is het "+ str(stationEindNummer) + "e station in het traject.")
	if stationBeginNummer + 1 is not stationEindNummer:
		print("De afstand bedraagt "+ str(afstandStations) +" station(s).")
	print("De prijs van het kaartje is "+ str(afstandStations * 5) +" euro.")
	print("Jij stapt in de trein in: " + beginstation)
	for idx, station in enumerate(stations):
		if idx + 1 > stationBeginNummer and idx + 1 < stationEindNummer:
			print(" 	- " + station)
	print("Jij stapt uit de trein in: " + eindstation)
	
beginStation = inlezen_beginstation(stations)
eindStation = inlezen_eindstation(stations, beginStation)
omroepen_reis(stations, beginStation, eindStation)