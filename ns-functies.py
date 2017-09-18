euroPerKM = .80
langeRitKM = 50
langeRitExtraEuro = 15.00
langeRitExtraEuroPerKM = .60

maximaleLeeftijdKorting = 12
minimaleLeeftijdKorting = 65

weekdayDiscountRate = .7
weekendDiscountRate = .65
weekendRegularRate = .6

def standaardtarief(afstandKM):
	returnValue = 0
	if afstandKM <= 0:
		returnValue = returnValue
	elif afstandKM > langeRitKM:
		returnValue = (afstandKM * euroPerKM) + langeRitExtraEuro + (langeRitExtraEuroPerKM * afstandKM)
	else:
		returnValue = afstandKM * euroPerKM
	return returnValue

def ritprijs(leeftijd, weekendrit, afstandKM):
	standaard = standaardtarief(afstandKM)
	returnValue = 0
	hasAgeDiscount = ((leeftijd < maximaleLeeftijdKorting) or (leeftijd >= minimaleLeeftijdKorting))
	if not weekendrit and hasAgeDiscount:
		returnValue = standaard * weekdayDiscountRate
	elif weekendrit and hasAgeDiscount:
		returnValue = standaard * weekendDiscountRate
	elif weekendrit:
		returnValue = standaard * weekendRegularRate
	else:
		returnValue = standaard
	return returnValue

tests = [
	[11, True, 50],
	[12, False, 49],
	[64, True, 100],
	[65, False, 20],
	[40, False, 75.98], # float overflow lets go
	[41, False, 120.56],
	[41, False, -126]
]

for test in tests:
	print("test: €" + str( format( ritprijs( test[0], test[1], test[2] ), ".2f") ) + " --- standaard: €"+ str(standaardtarief(test[2])) )