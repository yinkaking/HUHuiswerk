maxKluizen = 12
listOfFileLines = list()
kluisNummerList = list()

def readFile():
	del listOfFileLines[:]
	with open("files/kluizen.txt") as f:
		for line in f:
			listOfFileLines.append(line)
		f.close()

def toon_aantal_kluizen_vrij():
	readFile()
	return maxKluizen - len(listOfFileLines)

def nieuwe_kluis():
	if toon_aantal_kluizen_vrij() == 0:
		print("Alle kluizen zitten vol!")
		return False
	else:
		code = input("Uw wachtwoord/code voor de kluis? (Minimaal 4 tekens!) ")
		if len(code) < 4:
			nieuwe_kluis()
		for line in listOfFileLines:
			kluisLi = line.split(";")
			kluisNummerList.append(int(kluisLi[0]))
		print(kluisNummerList)
		kluisNummer = newKluisNumber(1, kluisNummerList);
			
		file = open("files/kluizen.txt", "w")
		for line in listOfFileLines:
			file.write(line)
		file.write("\n" +str(kluisNummer) + ";" + code)
		file.close()
		print("Uw heeft nu een kluis, het nummer is "+ str(kluisNummer))
		readFile()

def kluis_openen():
	readFile()
	code = input("Uw wachtwoord/code voor de kluis? ")
	number = int(input("Uw Kluisnummer?"))
	if (str(number) + ";" + code) in listOfFileLines:
		print("Uw kluis is nu open!")
	else:
		print("Het wachtwoord of het nummer kloppen niet, probeer nogmaals")
		kluis_openen()

def kluis_teruggeven():
	readFile()
	code = input("Uw wachtwoord/code voor de kluis? ")
	number = int(input("Uw Kluisnummer?"))
	if (str(number) + ";" + code) not in listOfFileLines:
		print("Don't even try")
	elif (str(number) + ";" + code) in listOfFileLines:
		file = open("files/kluizen.txt", "w")
		for line in li:
			if line == (str(number) + ";" + code):
				continue
			file.write(line)
		file.close()
		print("Kluis is weer beschikbaar")

def newKluisNumber(number, kluisListArg):
	if number in kluisListArg:
		number = number + 1
		return newKluisNumber(number, kluisListArg)
	else:
		return number

print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
print("4: Ik geef mijn kluis terug")
menuChoice = int(input("Wat wilt u doen? "))

if not isinstance(menuChoice, int):
	print("Error Terminating Program")
	exit()

if menuChoice == 1:
	print(toon_aantal_kluizen_vrij())
elif menuChoice == 2:
	nieuwe_kluis()
elif menuChoice == 3:
	kluis_openen()
elif menuChoice == 4:
	kluis_teruggeven()