li = list()
months = ["Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober", "November", "December"];
has31Days = True

class Month(object):
	def __init__(self, arg, arg2):
		self.name = arg
		self.numberOfDays = arg2
	def __str__(self):
		return self.name + " : dagen : " + str(self.numberOfDays)

for x in range(0,12):
	if has31Days:
		has31Days = False
		li.append(Month(months[x], 31))
	elif months[x] == months[1]:
		li.append(Month(months[x], 28))
		has31Days = True
	elif months[x] == months[7]:
		li.append(Month(months[x], 31))
	else:
		li.append(Month(months[x], 30))
		has31Days = True

for x in li:
	print(x)