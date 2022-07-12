
def attack_number():
	global random
	global weapon
	reloading = random.randint(1,20)
	if weapon == 10:
		if reloading < 4:
			return 2
		else:
			return 1
	elif weapon == 20:
		return 2
	elif weapon == 3:
		return .8
	else:
		return 1					

def hit_miss():
	global weapon
	global random
	risk = random.randint(1,101)
	if weapon == 3:
		if risk < 15:
			return 0
		else:
			return 1
	elif weapon == 5:
		if risk < 10:
			return 0
		else:
			return 1
	elif weapon == 8:
		if risk < 20:
			return 0
		else:
			return 1
	elif weapon == 10:
		if risk < 10:
			return 0
		elif risk in range(10,30):
			return .5
		elif risk in range(30,60):
			return .7
		elif risk in range(61,84):
			return .9
		elif risk in range(85,100):
			return 1
		else:
			return 1
	elif weapon == 20:
		if risk < 30:
			return 0
		else:
			return 1
	else:
		return 1																			

def distad():
	global weapon
	if weapon == 3:
		return .8
	elif weapon == 5:
		return .7
	elif weapon == 8:
		return .3
	elif weapon == 20:
		return .7
	else:
		return 1



weapon = 3
import random


hit_miss()
attack_number
print hit_miss()
print attack_number()