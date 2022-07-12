#Destroy the Kilge
#(these first lines were written at) 10/3/15 6:09 p.m.
#version alpha completed: 11/14/15 10:30 p.m.
#version beta completed: 1/20/16 10:25 p.m.
#version 1.0 alpha completed: 2/25/16 5.23 p.m.
#a big bug fixed on 3/15/2019 9:00 p.m.
#lol another bug fixed on 3/18/2019 9:43 p.m.
#My first attempt to make a text adventure I actually am pretty confident I will be able to finish
#Johnathan Huff

#Steve functions
def menu_call():
	global health
	global user_damage
	global water
	global weapon
	global battlevar
	global random
	global cactus_juice
	global weaponlist
	print " "
	print "This is the pause menu."
	print "his name is steve."
	time.sleep(.2)
	while True:
		print " "
		print "status report:"
		status_report()
		menu_go = raw_input( "press help for a list of commands. " )
		if menu_go == 'help':
			menu_help()
		elif menu_go == 'inventory':
			menu_inventory()
		elif menu_go == "weaponC":
			menu_weaponC()
		elif menu_go == "status":
			menu_status()
		elif menu_go == "quit":
			print "your password is:"
			print change, ":", weaponlist
			print water, cactus_juice, water_main, health, battlevar, weapon, key, Gate, Note
			print user_damage, cactus_stone, rifleget, message, opinion, ruby, doll, r2door, ":", checkpoint
			quit()
		elif menu_go == "done":
			break
		else:
			print """"
user error. unknown input.
"""

def menu_help():
	print """
some sample commands:
inventory: list your inventory
weaponC: lists the weapons catalog
status: change your status (e.g. drink water)
quit: closes the program
done: return to game
"""
	time.sleep(.5)

def status_report():
	print "water =", water
	print "health points =", health
	print "weapon =", weapon

def menu_inventory():
	global ruby
	global doll
	global key
	global weapon
	global weaponlist
	global water
	global cactus_juice
	global health
	global opinion
	global message
	global cactus_stone
	print ' '
	print "health =", health
	print "weapon =", weapon
	print "you have weapons", weaponlist
	print "water =", water
	print "cactus juice =", cactus_juice
	if ruby > 0:
		print "you have a ruby."
	else:
		pass
	if key > 0:
		print "you have", key, "keys."
	else:
		pass
	if doll > 0:
		print "you have a doll."
	else:
		pass
	if opinion > 0:
		opinionye()
	else:
		pass
	if message == 1:
		print "you found a message on a stone tablet:"
		print "THE TOP DIRECTS"
		print "THE BOTTOM SUPPLIES"
		print "REMEMBER THIS AT THE GATE"
	else:
		pass
	if cactus_stone > 0:
		print "you have a cactus stone."
	else:
		pass

def opinionye():
	global opinion
	if opinion == 1:
		print "This place is desolate and demolished."
		print "The Kilge probably did all of this."
		print "makes sense."
	elif opinion == 2:
		print "The Kilge definitely did this."
		print "I'm curious to find them."
	elif opinion == 3:
		print "Terrorist who nuke towns"
		print "and destroy things, thats"
		print "who the Kilge are. How do I"
		print "destroy them if they did all this?"
	elif opinion == 4:
		print "The Kilge have taken so many lives."
		print "They will pay, if its the last thing"
		print "I do."
	elif opinion == 5:
		print "I question everything I ever thought"
		print "and everything I was told. Do the"
		print "Kilge even exist? If they actually do,"
		print "did they cause the destruction, or were"
		print "they the ones destroyed? I don't know anymore."
	else:
		pass

def menu_weaponC():
	print ' '
	print "a catalog of weapons."
	print ' '
	print """
fists: 1
	starter weapon. very low damage.

bone spear: 2
	a basic weapon able to be found as the very first
	thing you can do in the game. gives you a fighting
	chance.

rustic sword: 2.5
	man! this thing is KEWL, but not super awesome.
	Still a little better than bone spear.

old bow: 3
	attack from farther. take less damage. slight
	risk of missing.

pistol: 5
	attack from farther. take less damage. do lots of damage.
	slight risk of missing.

rifle: 8
	attack from REALLY far away. Take very little damage. do lots
	of damage, with a reasonable risk of missing...

shotgun: 10
	attack from up close like swords. Do MEGA damage. random
	one in three chance your opponent gets to attack twice,
	whilst you reload. damage is random and not consistent.

bazooka: 20
	do devastating damage. opponent attacks you 3 times
	each turn whilst you reload. risk of missing.

there are a few other weapons, but you can discover those
yourself.
"""

def menu_status():
	global cactus_juice
	global health
	global water
	global weapon
	global weaponlist
	print ' '
	while cactus_juice > 0:
		jchoice = raw_input( "would you like to drink cactus juice? " )
		if jchoice == 'yes':
			print "it's the quenchiest!"
			cactus_juice = cactus_juice - 1
			health = health + 80
		elif jchoice == 'no':
			print "ok"
			break
		else:
			print "user error. unrecognized input."

	while water > 0:
		wchoice = raw_input( 'would you like to drink water? ' )
		if wchoice == 'yes':
			print "you drank a water and gained 30 health points."
			water = water - 1
			health = health + 30
		elif wchoice == 'no':
			print "ok"
			break
		else:
			print "user error. unrecognized input."

	while True:
		swchoice = raw_input( "would you like to switch weapons? " )
		if swchoice == "yes":
			print "you have weapons", weaponlist
			weapon_change = raw_input( 'enter the number to change to that weapon. ' )
			try:
				if float(weapon_change) in weaponlist:
					weapon = float(weapon_change)
				else:
					print "you don't have that weapon"	
			except ValueError:
				print "big oof"		
				break

	#		if weapon_change in weaponlist:
	#			weapon = weapon_change
	#		else:
	#			print "you don't have that weapon."
		elif swchoice == 'no':
			print "ok"
			break

#Location functions
def start_point():
	print "this is the drop zone."
	while True:
		SP_input = raw_input( "You can go to the small cave, or the oasis. " )
		if SP_input == 's':
			break
		elif SP_input == 'o':
			break
		elif SP_input == 'menu':
			menu_call()
		else:
			print 'user error. unrecognized input.'

	if SP_input == 's':
		small_cave()

	if SP_input == 'o':
		oasis1()

def small_cave():
	global health
	global user_damage
	global water
	global weapon
	global battlevar
	global random
	global weaponlist
	while weapon == 1:
		SC_weapon = raw_input( """
there is a crude spear on the ground.
Looks handmade. Still probably better
than fists. Pick it up? (y/n) """ )
		if SC_weapon == "y":
			weapon = 2.0
			weaponlist.append(2.0)
		elif SC_weapon == "n":
			break
		else:
			print "user error. unrecognized input."

	print "this is the small cave."
	while True:
		SC_input = raw_input( "You can go to the drop zone, or the oasis. " )
		if SC_input == 'd':
			break
		elif SC_input == "o":
			break
		elif SC_input == 'menu':
			menu_call()
		else:
			print "user error. Unrecognized input."

	if SC_input == 'd':
		start_point()

	if SC_input == 'o':
		oasis1()

def oasis1():
	global health
	global user_damage
	global water
	global weapon
	global battlevar
	global random
	global change
	print "this is the oasis."
	while battlevar == 1:
		game = 1
		enemy = 100
		while game == 1:
			print "There is a large spider."
			print "it wants to battle."
			print " "

			number = random.randint(1,13)
			damage = random.randint(3,7) * change
			print 'health =', health
			print 'enemy health =', enemy
			print 'you have', water, 'water.'
			action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)

			if action == "1":
				enemy = enemy - user_damage * weapon
			elif action == "2":
				enemy = enemy - number * weapon
			elif action == "3":
				if water >= 1:
					print 'you drank water and gained 30 health points.'
					health = health + 30
					water = water - 1
				if water == 0:
					print "you have no water to drink"
					pass
			else:
				pass
			if enemy <= 0:
				print 'you defeated the spider.'
				battlevar = 2
				break
			health = health - damage
			if health <= 0:
				quit( "you died. " )
			print 'the spider hit you for', damage, 'damage.'

	while True:
		O1_input = raw_input( "you can go to the wasteland edge, the city gate, the small cave, or the drop zone. " )
		if O1_input == "w":
			break
		elif O1_input == "c":
			break
		elif O1_input == 's':
			break
		elif O1_input == 'd':
			break
		elif O1_input == "menu":
			menu_call()
		else:
			print "user error. unrecognized input."

	if O1_input == "w":
		wasteland_edge()

	if O1_input == 'c':
		city_wall()

	if O1_input == 's':
		small_cave()

	if O1_input == 'd':
		start_point()

def wasteland_edge():
	global weaponlist
	global water
	print "this is the wasteland edge."

	sandstorm()
	cactus_battle()
	lion_battle()
	resident()
	waterget()

	global weapon
	while weapon < 2.5:
		rswordhope = random.randint(1,3)
		if rswordhope == 1:
			pass
		elif rswordhope == 2:
			weapon = 2.5
			weaponlist.append(2.5)
			print "you found a sword buried in the sand."
			print "wow it looks SUPER cool!"
		else:
			weapon = 2.5
			print "you found a sword buried in the sand."
			print "wow it looks SUPER cool!"
			weaponlist.append(2.5)

	print "a fine line is visible where the desert turns into wasteland nothingness"
	while True:
		WE_input = raw_input( "you can go to the oasis, the wasteland corner, or the heart of the wasteland. " )
		if WE_input == 'menu':
			menu_call()
		elif WE_input == 'o':
			break
		elif WE_input == 'h':
			break
		elif WE_input == 'w':
			break
		else:
			print "user error. unrecognized input."

	if WE_input == 'o':
		oasis1()

	if WE_input == 'w':
		wasteland_corner()

	if WE_input == 'h':
		heart_wasteland()

def heart_wasteland():
	cactus_battle()
	lion_battle()
	sandstorm()
	waterget()
	waterget()
	#there are supposed to be two water function calls here. Not a bug.
	print "this is the wasteland heart, the climax of emptiness."
	while True:
		WH_input = raw_input( "you can go to the wasteland edge, the object over the horizon, the forest outskirts, or the sandy dunes. " )
		if WH_input == 'menu':
			menu_call()
		elif WH_input == "w":
			break
		elif WH_input  == 'o':
			break
		elif WH_input == 's':
			break
		elif WH_input == 'f':
			break
		else:
			print "user error. unrecognized input."
	if WH_input == 'w':
		wasteland_edge()

	if WH_input == 'o':
		horizon()

	if WH_input == 's':
		sandy_dunes()

	if WH_input == 'f':
		forest_outskirts()

def sandy_dunes():
	sand_maybe()
	waterget()
	cactus_battle()
	print "you are coming out of the wasteland."
	while True:
		SD_choice = raw_input( "you can go to the road2 or the heart of the wasteland. " )
		if SD_choice == 'menu':
			menu_call()
		elif SD_choice == '2':
			break
		elif SD_choice == 'h':
			break
		else:
			print "user error. unrecognized input."
	if SD_choice == '2':
		road2()
	if SD_choice == 'h':
		heart_wasteland()

def horizon():
	global message
	global doll
	waterget()
	print " "
	print "the object is a stone tablet."
	print "it reads, "
	print "THE TOP DIRECTS"
	print "THE BOTTOM SUPPLIES"
	print "REMEMBER THIS AT THE GATE"
	print "what in the world could that mean?"
	print " "
	if message == 0:
		message = 1
	else:
		pass
	print " "
	time.sleep(2)
	if doll == 0:
		print "you found a doll half buried in the sand."
		print "how did it get here?"
		doll = 1
	else:
		 pass
	print "this is the horizon, the west edge of the desert."
	while True:
		H_input = raw_input( "you can go back to the heart of the wasteland. " )
		if H_input == 'menu':
			menu_call()
		elif H_input == 'h':
			break
		else:
			print "user error. unrecognized input."
	if H_input == 'h':
		heart_wasteland()

def wasteland_corner():
	cactus_battle()
	lion_battle()
	sandstorm()
	resident()
	waterget()

	print "sheer nothingness. was there ever anything?"

	while True:
		WC_input = raw_input( "you can go to the wasteland edge or the old road 3. " )
		if WC_input == 'w':
			break
		elif WC_input == '3':
			break
		elif WC_input == 'menu':
			menu_call()
		else:
			print "user error. unrecognized input."

	if WC_input == 'w':
		wasteland_edge()

	if WC_input == '3':
		road3()

def road1():
	global rifleget
	demon_lama()
	resident()
	if rifleget == 1:
		global weapon
		global weaponlist
		print " "
		print "there is a chest sitting in the middle of the road."
		print "there is a note attached to it. It reads:"
		print '"take this as a donation. please help us."'
		print "a rifle is inside! It's in great shape!"
		weaponlist.append(8.0)
		weapon = 8.0
		print "who else is out here?"
		print " "
		rifleget = 2
	else:
		pass
		print "this is the road1"
	while True:
		R1_input = raw_input( "you can go to the road2 " )
		if R1_input == 'menu':
			menu_call()
		elif R1_input == '2':
			break
		else:
			print "user error. unrecognized input."
	if R1_input	== '2':
		road2()

def road2():
	demon_lama()
	resident()
	print "this is the road2"
	while True:
		R2_input = raw_input( "you can go to the road1, road3, or the sandy dunes. " )
		if R2_input == 'menu':
			menu_call()
		elif R2_input == '1':
			break
		elif R2_input == '3':
			break
		elif R2_input == 's':
			break
		else:
			print "user error. unrecognized. input."
	if R2_input == '1':
		road1()
	if R2_input == '3':
		road3()
	if R2_input == 's':
		sandy_dunes()

def road3():
	demon_lama()
	resident()
	global weapon
	global weaponlist
	if 5.0 not in weaponlist:
		weaponlist.append(5.0)
		weapon = 5.0
		print " "
		print "you found a battered pistol half buried in the sand."
		print "still fires true."
		print " "
	else:
		pass
	waterget()

	print "this is the road3."
	while True:
		R3_input = raw_input( "you can go to the wasteland corner, road2, or road4. " )
		if R3_input == '2':
			break
		elif R3_input == '4':
			break
		elif R3_input == 'w':
			break
		elif R3_input == 'menu':
			menu_call()
		else:
			print "user error. unrecognized input."

	if R3_input == 'w':
		wasteland_corner()
	if R3_input == '2':
		road2()
	if R3_input == '4':
		road4()

def road4():
	demon_lama()
	resident()
	print "this is the road4"
	while True:
		R4_input = raw_input( "you can go to the road3, the road5, or the damp cave. " )
		if R4_input == 'menu':
			menu_call()
		elif R4_input == '3':
			break
		elif R4_input == '5':
			break
		elif R4_input == 'd':
			break
	if R4_input == '3':
		road3()
	if R4_input == '5':
		road5()
	if R4_input == 'd':
		damp_cave()

def road5():
	global weapon
	global weaponlist
	global key
	global doll
	global ruby
	global time
	global cactus_juice
	global opinion
	if 10.0 not in weaponlist:
		time.sleep(1)
		print "a hut stands at the end of the road."
		time.sleep(2)
		print "you walk inside."
		time.sleep(2)
		print " "
		print "a man offers you a large package for trade."
		print "says its invaluable."
		print " "
		time.sleep(2)
		if ruby > 0:
			print "you offer him a ruby."
			print "he says it's not enough."
			time.sleep(2)
			if doll > 0:
				print "you show him the doll."
				time.sleep(2)
				print "he weeps."
				time.sleep(3)
				print "he says it belonged to his daughter, before they came."
				time.sleep(2)
				print 'he wouldnt say who "they" were, but it must be the Kilge.'
				print "the man takes the trade."
				time.sleep(3)
				print " "
				print "you open the chest."
				print " "
				print "there is a shotgun, 3 cactus juices, and a key inside!"
				weaponlist.append(10.0)
				weapon = 10.0
				cactus_juice = cactus_juice + 3
				key = key + 1
				opinion = 3
			else:
				print "you don't have anything else to give."
				print "you walk away."
		else:
			print "you have nothing to offer."
	else:
		pass

	print "this is road5, the end of the road."
	while True:
		R5_input = raw_input( "you can go to the road4. " )
		if R5_input == 'menu':
			menu_call()
		elif R5_input == '4':
			break
		else:
			print "user error. unrecognized input."

	if R5_input == '4':
		road4()

def damp_cave():
	global time
	global cactus_stone
	global weapon
	global weaponlist
	print "there is an eerie ringing coming from the walls."
	print " "
	time.sleep(3)
	if 40.0 not in weaponlist:
		print "there is a hole in the wall."
		if cactus_stone > 0:
			print "you stick the cactus stone in the hole."
			time.sleep(2)
			print "the wall opens up and you walk inside."
			mechsuit()
		else:
			print "this place is very mysterious."
	else:
		pass
	while True:
		DC_input = raw_input( "you can go to the road4. " )
		if DC_input == 'menu':
			menu_call()
		elif DC_input == '4':
			break
		else:
			print "user error. unrecognized input."
	if DC_input == '4':
		road4()

def city_wall():
	lion_battle()
	resident()
	sandstorm()
	waterget()

	global weapon
	global weaponlist
	while weapon < 2.5:
		rswordhope = random.randint(1,3)
		if rswordhope == 1:
			pass
		elif rswordhope == 2:
			weapon = 2.5
			weaponlist.append(2.5)
			print "you found a sword buried in the sand."
			print "wow it looks SUPER cool!"
		else:
			weapon = 2.5
			weaponlist.append(2.5)
			print "you found a sword buried in the sand."
			print "wow it looks SUPER cool!"

	while True:
		print "a fallen city lies just ahead..."
		CW_input = raw_input( "you can go to the oasis, or to main street. " )
		if CW_input == "o":
			break
		elif CW_input == 'm':
			break
		elif CW_input == 'menu':
			menu_call()
		else:
			print "user error. unrecognized input."

	if CW_input == 'o':
		oasis1()

	if CW_input == 'm':
		main_street()

def main_street():
	global water
	global health
	global water_main
	global opinion
	while water_main == 1:
		water = water + 3
		print " "
		print "you found 3 waters in an abandoned house."
		print """
by the looks of the city, it used to be grand. Somehow, it
was destroyed. The Kilge must be responsible! (notices
noises can be heard) """
		if opinion < 1:
			opinion = 1
		else:
			pass
		water_main = 2
		time.sleep(2)

	while True:
		MS_input = raw_input( "you can go to the city wall, or the market. " )
		if MS_input == 'c':
			break
		elif MS_input == 'm':
			break
		elif MS_input == 'menu':
			menu_call()
		else:
			print "user error. unrecognized input."

	if MS_input == 'c':
		city_wall()

	if MS_input == 'm':
		market()

def market():
	global weapon
	global weaponlist
	global ruby
	global water
	global opinion
	while weapon < 3.0:
		print " "
		print "there is an old bow on the ground."
		print 'looks handy.'
		weaponlist.append(3.0)
		weapon = 3.0
	print"""
remains of a marketplace...
the Kilge will pay.
"""
	if ruby == 0:
		print "you found a smooth ruby on the ground."
		print "such beauty in utter destruction."
		ruby = 1
		if opinion < 2:
			opinion = 2
		else:
			pass
	else:
		pass

	while True:
		M_input = raw_input( "you can go to main street, or town square. " )
		if M_input == 'm':
			break
		elif M_input == 't':
			break
		elif M_input == 'menu':
			menu_call()
		else:
			print "user error. unrecognized input."

	if M_input == 'm':
		main_street()
	else:
		pass

	if M_input == 't':
		town_square()
	else:
		pass

def town_square():
	global battlevar
	global water
	global health
	global weapon
	global user_damage
	global change
	global random
	global cactus_juice
	global key
	global cactus_stone

	while battlevar == 2:
                print " "
		print "there is a deadly presence here."
		print "you should probably come back later."
                print " "
		dchoice = raw_input( "would you like to turn back? " )
		if dchoice == 'yes':
			break
		elif dchoice == 'no':
                        print " "
			print "A massive cactus tumbles upright."
			print "It's at least 15 feet tall."
                        print " "
			break
		else:
			print "user error. unrecognized input."
	else:
		pass

	if dchoice == 'yes':
		market()
	else:
		pass

	if battlevar == 2:
		bigboy = 500
		while True:
			number = random.randint(1,13)
			big_damage = random.randint(30,100) * change
			print "health =", health
			print "enemy health =", bigboy
			print "you have", water, "water."

			action = int( raw_input( """
1. basic attack
2. special attack
3. drink water
"""	) )
			if action == 1:
				bigboy = bigboy - user_damage * weapon * hit_miss()
			elif action == 2:
				bigboy = bigboy - number * weapon * hit_miss()
			elif action == 3:
				if water >= 1:
					print 'you drank water and gained 30 health points.'
					health = health + 30
					water = water - 1
				if water == 0:
					pass
			else:
				print "user error. unrecognized input."
				pass
			if bigboy <= 0:
				print " "
				print 'you defeated the giant cactus.'
				cactus_juice = cactus_juice + 10
				key = key + 1
				cactus_stone = cactus_stone + 1
				print "you got 10 cactus juices, a key, and a cactus stone."
				print " "
				break
			health = health - big_damage * attack_number()
			if health <= 0:
				quit( "you died. " )
			print 'the cactus hit you', attack_number(), 'times for', big_damage, 'damage.'
		else:
			pass

	while True:
		TS_input = raw_input( "you can go to the market place. " )
		if TS_input == 'm':
			break
		elif TS_input == 'menu':
			menu_call()
		else:
			print "user error. unrecognized input."

	if TS_input == "m":
		market()

def forest_outskirts():
	bionic_tree()
	bionic_tree()
	lion_battle()
	waterget()

	print "this is the forest outskirts."
	while True:
		FO_input = raw_input( """you can go to the heart of the wasteland,
the forest plains, or thick woods.
""" )
		if FO_input == 'menu':
			menu_call()
		elif FO_input == 'h':
			break
		elif FO_input == 'f':
			break
		elif FO_input == 't':
			break
		else:
			print "user error. unrecognized input."
	if FO_input == 'h':
		heart_wasteland()
	if FO_input == 'f':
		forest_plains()
	if FO_input == 't':
		thick_woods()

def thick_woods():
	bionic_tree()
	bionic_tree()
	lion_battle()
	waterget()

	print "this is the thick woods."
	while True:
		TW_input = raw_input( "you can go to the trodden trail, the boothill bunker, the camp ground, or the forest outskirts. " )
		if TW_input == 'menu':
			menu_call()
		elif TW_input == 't':
			break
		elif TW_input == 'b':
			break
		elif TW_input == 'c':
			break
		elif TW_input == 'f':
			break
		else:
			print "user error. unrecognized input."

	if TW_input == 't':
		trodden_trail()

	if TW_input == 'b':
		boothill_bunker()

	if TW_input == 'c':
		camp_ground()

	if TW_input == 'f':
		forest_outskirts()

def forest_plains():
	bionic_tree()
	bionic_tree()
	lion_battle()
	waterget()

	print "this is the forest plains."
	while True:
		FP_input = raw_input( "you can go to the forest outskirts, or the trodden trail. " )
		if FP_input == 'menu':
			menu_call()
		elif FP_input == 'f':
			break
		elif FP_input == 't':
			break
		else:
			print "user error. unrecognized input."

	if FP_input == 'f':
		forest_outskirts()

	if FP_input == 't':
		trodden_trail()

def boothill_bunker():
	global weaponlist
	global time
	bionic_tree()
	bionic_tree()
	resident()
	resident()
	waterget()
	waterget()

	print "a bunker stands on a hill."
	time.sleep(1.5)
	print "you go inside."
	time.sleep(1.5)
	print " "
	if 20.0 not in weaponlist:
		bazookaget()
	else:
		pass

	print "this is the boothill bunker."
	while True:
		BB_input = raw_input( "you can go to the thick woods. " )
		if BB_input == 'menu':
			menu_call()
		elif BB_input == 't':
			break
		else:
			print "user error. unrecognized input."

	if BB_input == 't':
		thick_woods()

def camp_ground():
	print "its a camp full of trees!"
	bionic_tree()
	bionic_tree()
	bionic_tree()
	bionic_tree()
	bionic_tree()
	bionic_tree()
	bionic_tree()
	bionic_tree()
	waterget()
	waterget()

	print "this is the camp ground."
	while True:
		CG_input = raw_input( "you can go to the thick woods." )
		if CG_input == 'menu':
			menu_call()
		elif CG_input == 't':
			break
		else:
			print "user error. unrecognized input."

	if CG_input == 't':
		thick_woods()

def trodden_trail():
	cactus_battle()
	resident()
	demon_lama()
	bionic_tree()
	waterget()

	print "this is the trodden trail."

	while True:
		TT_input = raw_input( "you can go to the thick woods, of the barren trail. " )
		if TT_input == 'menu':
			menu_call()
		elif TT_input == 't':
			break
		elif TT_input == 'b':
			break
		else:
			print "user error. unrecognized input."

	if TT_input == 't':
		thick_woods()

	if TT_input == 'b':
		barren_trail()

def barren_trail():
	cactus_battle()
	resident()
	demon_lama()
	bionic_tree()
	waterget()

	print "this is the barren trail."
	while True:
		BT_input = raw_input( "you can go to the trodden trail, or the lost path. " )
		if BT_input == 't':
			break
		elif BT_input == 'menu':
			menu_call()
		elif BT_input == 'l':
			break
		else:
			print "user error. unrecognized input."

	if BT_input == 't':
		trodden_trail()

	if BT_input == 'l':
		lost_path()

def lost_path():
	cactus_battle()
	resident()
	demon_lama()
	bionic_tree()
	waterget()

	print "this is the lost path."

	while True:
		LP_input = raw_input( "you can go to the barren trail, or the iron gate. " )
		if LP_input == 'menu':
			menu_call()
		elif LP_input == 'b':
			break
		elif LP_input == 'i':
			break
		else:
			print "user error. unrecognized input."

	if LP_input == 'b':
		barren_trail()

	if LP_input == 'i':
		iron_gate()

def iron_gate():
	global time
	global key
	global rdefeat
	if rdefeat == 0:
		time.sleep(2)
		print "there are three holes in the gate."
		if key >= 3:
			time.sleep(1)
			print "you put your keys in the holes."
			time.sleep(2)
			print "a message appears."
			time.sleep(2)
			print "it reads:"
			code_guess = raw_input( """
enter the password:
398652063
qljngcbif
"""	)
			if code_guess == 'turtleboi':
				time.sleep(2)
				print " "
				final_battle()
			else:
				print "you got it wrong."
				print " "
				print "returning to the previous area."
				lost_path()
		else:
			print " "
			print "you cant do anything."
			print "returning to the previous area."
			print " "
			lost_path()
	else:
		print " "
		print "this is the iron gate."
		while True:
			ig_input = raw_input("You can go to the lost path, or first room. ")
			if ig_input == "f":
				go.first_room()
			elif ig_input == "menu":
				menu_call()
			elif ig_input == "l":
				lost_path()
			else:
				print "user error. unrecognized input."

#battle functions
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
		if reloading < 5:
			return 2
		else:
			return 1
	else:
		return 1

def hit_miss():
	global weapon
	global random
	risk = random.randint(1,101)
	if weapon == 3:
		if risk < 12:
			return 0
		else:
			return 1
	elif weapon == 5:
		if risk < 8:
			return 0
		else:
			return 1
	elif weapon == 8:
		if risk < 30:
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
		if risk < 10:
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
		return .6
	else:
		return 1

def cactus_battle():
	boop = random.randint(1,7)
	if boop == 4:
		global health
		global user_damage
		global water
		global weapon
		global battlevar
		global change
		global cactus_juice
		global time
		print "a cactus moves in the distance?"
		time.sleep(1)
		print "it sprints toward you to attack!"
		time.sleep(1)

		cactus = 200

		low = random.randint(1,12)
		high = random.randint(15,37)

		while True:
			number = random.randint(1,13) * hit_miss()
			cactus_damage = random.randint(low,high) * change * attack_number() * distad()
			print "health =", health
			print "enemy health =", cactus
			print "you have", water, "water."

			action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)
			if action == "1":
				cactus = cactus - user_damage * weapon * hit_miss()
			elif action == "2":
				cactus = cactus - number * weapon
			elif action == "3":
				if water >= 1:
					print 'you drank water and gained 30 health points.'
					health = health + 30
					water = water - 1
				if water == 0:
					pass
			else:
				print "user error. unrecognized input."
				pass
			if cactus <= 0:
				print 'you defeated the cactus.'
				cactus_juice = cactus_juice + 1
				break
			health = health - cactus_damage
			if health <= 0:
				quit( "you died. " )
			print 'the cactus hit you for', cactus_damage, 'damage.'
		else:
			pass

def sandstorm():
	global water
	global health
	boop2 = random.randint(1,14)
	if boop2 == 7:
		print " "
		print "A sandstorm whipped up."
		print "gotta find shelter."
		time.sleep(2)
		if water >= 5:
			water = water - 5
		else:
			water = 0
		if health >= 50:
			health = health - 50
		else:
			health = 0
		if health <= 0:
			quit( "you died.")
		else:
			print "you lived, but lost some life and water."
	else:
		pass

def lion_battle():
	print " "
	boop3 = random.randint(1,6)
	if boop3 == 5:
		global health
		global user_damage
		global water
		global weapon
		global battlevar
		global change
		print "a lion pounces from behind a rock."

		lion = 150

		while True:
			number = random.randint(1,13) * hit_miss()
			enemy_damage = 8 * change * distad()
			print "health =", health
			print "enemy health =", lion
			print "you have", water, "water."

			action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)
			if action == "1":
				lion = lion - user_damage * weapon * hit_miss()
			elif action == "2":
				lion = lion - number * weapon
			elif action == "3":
				if water >= 1:
					print 'you drank water and gained 30 health points.'
					health = health + 30
					water = water - 1
				if water == 0:
					pass
			else:
				print "user error. unrecognized input."
				pass
			if lion <= 0:
				print 'you defeated the lion.'
				break
			health = health - enemy_damage * attack_number()
			if health <= 0:
				quit( "you died. " )
			print 'the lion hit you for', enemy_damage, 'damage.'
		else:
			pass

def resident():
	boop4 = random.randint(1,10)
	if boop4 == 4:
		mood = random.randint(1,10)
		print "A resident comes out to meet you."
		time.sleep(1)
		if mood <= 5:
			print "he has kind eyes."
			time.sleep(1)
			good_mood()
		else:
			print "he has dangerous eyes."
			time.sleep(1)
			bad_mood()
	else:
		pass

def good_mood():
	while True:
		global user_damage
		global water
		global weapon
		global weaponlist
		global cactus_juice
		mood_weapon = (3,4,5)
		randy = random.randint(3,6)
		print """
"It's a dangerous world out here," he says.
"let me help you out. What do you need?"
He offers some waters, some cactus juice,
a weapon, or a power boost."""
		get = raw_input( "what would you like to get? " )
		if get == "weapon":
			if randy not in weaponlist:
				weaponlist.append(randy)
				print "he smiles and walks away."
				break
			elif randy in weaponlist:
				print "you already have the weapon he has."
			else:
				pass
				print "some unknown error occurred."
		elif get == "waters":
			water = water + 5
			print "he gave you 5 waters."
			print "he smiles and walks away."
			break
		elif get == "cactus juice":
			cactus_juice = cactus_juice + 3
			print "he gave you 3 cactus juices."
			print "he smiles and walks away."
			break
		elif get == "power boost":
			user_damage = user_damage + 1
			print "he smiles and walks away."
			break
		else:
			print "user error. unrecognized input."

def bad_mood():
	global health
	global user_damage
	global water
	global weapon
	global random
	global change
	global time

	man = 150

	print "he pulls out a weapon of the likes you've never seen."
	print " "
	while True:
		number = random.randint(1,13) * hit_miss()
		print "health =", health
		print "enemy health =", man
		print "you have", water, "water."

		action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)
		if action == "1":
			man = man - user_damage * weapon * hit_miss()
			man_damage = user_damage * weapon * hit_miss()
		elif action == "2":
			man = man - number * weapon
			man_damage = user_damage * weapon
		elif action == "3":
			man_damage = 0
			if water >= 1:
				print 'you drank water and gained 30 health points.'
				health = health + 30
				water = water - 1
			if water == 0:
				pass
		else:
			print "user error. unrecognized input."
			man_damage = 0
			pass
		if man <= 0:
			print 'you defeated the man...'
			time.sleep(1)
			print"its like looking in a mirror."
			time.sleep(2)
			break
		health = health - man_damage
		if health <= 0:
			quit( "you died. " )
		print 'the enemy hit you for', man_damage, 'damage.'
	else:
		pass

def demon_lama():
	global random
	boopgo = random.randint(1,7)
	enemy = 500
	enemy_damage = 1
	if boopgo == 6:
		global health
		global user_damage
		global water
		global weapon
		global battlevar
		global change
		print "a demon lama spawns from the dunes."
		time.sleep(1)
		while True:
			number = random.randint(1,13) * hit_miss()
			print "health =", health
			print "enemy health =", enemy
			print "you have", water, "water."

			action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)
			if action == "1":
				enemy = enemy - user_damage * weapon * hit_miss()
			elif action == "2":
				enemy = enemy - number * weapon
			elif action == "3":
				if water >= 1:
					print 'you drank water and gained 30 health points.'
					health = health + 30
					water = water - 1
				if water == 0:
					pass
			else:
				print "user error. unrecognized input."
				pass
			if enemy <= 0:
				print 'you defeated the demon lama.'
				break
			health = health - enemy_damage * attack_number()
			if health <= 0:
				quit( "you died. " )
			print 'the demon lama hit you', attack_number(), 'times for', enemy_damage, 'damage.'
			enemy_damage = enemy_damage + 1
		else:
			pass

def sand_maybe():
    print "a sand dune is acting weird..."
    wanna = raw_input( "investigate? ")
    if wanna == 'no':
        pass
    elif wanna == 'yes':
        sand_game()
    else:
        pass

def sand_game():
	global random
	global rifleget
	global time
	global cactus_juice
	turn = 1
	time.sleep(2)
	print "the sand dune begins to speak."
	time.sleep(2)
	print '''
"I am Zugura, master of logical guesses.
Play a game with me. See if you are a
master of thinking."
'''
	time.sleep(2)
	print '"I will think of a number in a range of numbers."'
	print '"you have 6 guesses to get it right, or suffer'
	print 'the consequences!"'
	time.sleep(2)
	low = random.randint(0,50)
	high = random.randint(65,200)
	number = random.randint(low,high)
	while turn <= 6:
		print '"I am thinking of a number between'
		print low, "and", high
		print "you have", 7 - turn, "guesses left."
		guess = int( raw_input( 'what is it?" ' ) )
		if guess == number:
			break
		else:
			pass
		if guess > number:
			print " "
			print '"wrong. guess lower."'
			print " "
		else:
			pass
		if guess < number:
			print " "
			print '"wrong. guess higher."'
			print " "
		else:
			pass
		turn = turn + 1
		if turn > 6:
			break
	if turn > 6:
		sand_battle()
	else:
		print "you got the number right."
		print "it was", number
		print '"good job. as reward, i give you this."'
		print " "
		time.sleep(1)
		print "you gained a cactus juice!"
		cactus_juice = cactus_juice + 1
		rifleget = 1

def sand_battle():
	print " "
	print "Zugura tries to battle you, but he really"
	print "cant, because he is a sand dune, so you just"
	print "walk away."
	print " "

def bionic_tree():
	global health
	global user_damage
	global water
	global weapon
	global battlevar
	global random
	global change

	tree_boop = random.randint(1,5)
	tree = 75

	if tree_boop == 7:
		print " "
		print "a bionic tree approaches from the forest."
		print " "
		time.sleep(2)
		while True:
			number = random.randint(1,13) * hit_miss()
			tree_damage = random.randint(35,95) * change * attack_number() * distad()
			print "health =", health
			print "enemy health =", tree
			print "you have", water, "water."

			action = int( raw_input( """
1. basic attack
2. special attack
3. drink water
"""	) )
			if action == 1:
				tree = tree - user_damage * weapon * hit_miss()
			elif action == 2:
				tree = tree - number * weapon
			elif action == 3:
				if water >= 1:
					print 'you drank water and gained 30 health points.'
					health = health + 30
					water = water - 1
				if water == 0:
					pass
			else:
				print "user error. unrecognized input."
				pass
			if tree <= 0:
				print 'you defeated the bionic tree.'
				break
			health = health - tree_damage
			if health <= 0:
				quit( "you died. " )
			print 'the bionic hit you', attack_number(), 'times for', tree_damage, 'damage.'
		else:
			pass
	else:
		pass

def final_battle():
	global health
	global user_damage
	global water
	global weapon
	global battlevar
	global random
	global change
	global time
	global rdefeat
	print " "
	print "the gate opens."
	print " "
	time.sleep(2)
	print "a giant robot stands in sight, just behind where the gate was."
	time.sleep(4)
	print '"KILGE" is printed across its chest.'
	time.sleep(3)

	robot = 1000

	while True:
		number = random.randint(1,13) * hit_miss()
		enemy_damage = random.randint(170,350) * change * attack_number() * distad()
		print "health =", health
		print "enemy health =", robot
		print "you have", water, "water."

		action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)
		if action == "1":
			robot = robot - user_damage * weapon * hit_miss()
		elif action == "2":
			robot = robot - number * weapon
		elif action == "3":
			if water >= 1:
				print 'you drank water and gained 30 health points.'
				health = health + 30
				water = water - 1
			if water == 0:
				pass
		else:
			print "user error. unrecognized input."
			pass
		if robot <= 0:
			print " "
			print " "
			print " "
			print 'you defeated the robot.'
			print " "
			print " "
			print " "
			break
		health = health - enemy_damage
		if health <= 0:
			quit( "you died. " )
		print 'the robot hit you', attack_number(), 'times for', enemy_damage, 'damage.'
	else:
		pass

	if robot <= 0:
		checkpoint = 1
		rdefeat = 1
		go.start_point()

#other
def waterget():
	global water
	watervar = random.randint(1,20)
	if watervar == 2:
		water = water + 1
		print "you found a water!"
	elif watervar == 7:
		water = water + 3
		print "you found 3 waters!"
	elif watervar == 13:
		print "you found 5 waters! wow!"
		water = water + 5
	elif watervar == 17:
		print "you found 10 waters! jackpot!"
		water = water + 10
	else:
		pass

def bazookaget():
	global weapon
	global weaponlist
	global key
	weaponlist.append(20.0)
	weapon = 20.0
	key = key + 1
	print " "
	print "You found a bazooka!"
	print 'you found a key!'
	print " "

def mechsuit():
	global weaponlist
	global weapon
	print " "
	print " "
	print "YOU FOUND A MECH SUIT"
	print "HOW DID IT GET HERE"
	print " "
	print " "
	weaponlist.append(40.0)
	weapon = 40.0

def error():
	print ";;;"
	print ";;;"
	print "beginning game with default values for the ones not entered"
	print ";;;"
	print ";;;"
	start_point()

def password_system():
	global change
	global top
	global water
	global cactus_juice
	global water_main
	global health
	global battlevar
	global weapon
	global key
	global user_damage
	global cactus_stone
	global rifleget
	global message
	global opinion
	global ruby
	global doll
	global weaponlist
	global Gate
	global Note
	global r2door

	print " "
	print "welcome to the password system."
	print "follow my instructions to enter the password."
	user_input1 = float(raw_input("enter the number in the top left corner: ") )
	if user_input1 in [.8,1,1.2,1.4]:
		change = user_input1
	else:
		print "that is not possible."
		error()
	user_input2 = int(raw_input("how many numbers are inside the brackets? "))
	if user_input2 <= 0:
		if user_input2 > 9:
			print "that is not possible."
			error()
	elif user_input2 > 9:
		if user_input2 <= 0:
			print "that is not possible."
			error()
	else:
		top = user_input2
	weaponlist = []
	for i in range(0,top):
		print "what is number", i + 1, "in the brackets?"
		user_inputa = float(raw_input(">>> "))
		if user_inputa in [1,2,2.5,3,5,8,10,20,40,60,100]:
			if user_inputa not in weaponlist:
				weaponlist.append(user_inputa)
			else:
				print "that is not possible."
				error()
		else:
			print "that is not possible."
			error()

	print "now enter the numbers in the second row, from left"
	print "to right. They will be entered one at a time."
	print "once you have done that, do the same for the bottom row."

	user_input3 = int(raw_input("enter a number: "))
	print " "
	if water < 0:
		print "that is not possible."
		error()
	else:
		water = user_input3

	user_input4 = int(raw_input("enter a number: "))
	print " "
	if cactus_juice < 0:
		print "that is not possible."
		error()
	else:
		cactus_juice = user_input4

	user_input5 = int(raw_input("enter a number: "))
	print " "
	if user_input5 > 2:
		print "that is not possible."
		error()
	elif user_input5 < 0:
		print "that is not possible."
		error()
	else:
		water_main = user_input5

	user_input6 = float(raw_input("enter a number: "))
	print " "
	if user_input6 <= 0:
		print "that is not possible."
		error()
	health = user_input6

	user_input7 = int(raw_input("enter a number: "))
	print " "
	if user_input7 not in [1,2]:
		print "that is not possible."
		error()
	battlevar = user_input7

	user_input8 = int(raw_input("enter a number: "))
	print " "
	if user_input8 not in [1,2,2.5,3,5,8,10,20,40]:
		print "that is not possible."
		error()
	else:
		weapon = user_input8

	user_input9 = int(raw_input("enter a number: "))
	print " "
	if key not in [0,1,2,3]:
		print "that is not possible."
		error()
	key = user_input9

	user_input18 = int(raw_input("enter a number: "))
	print " "
	if user_input18 not in [0,1]:
		print "that is not possible."
		error()
	Gate = user_input18

	user_input19 = int(raw_input("enter a number: "))
	print " "
	if user_input19 not in [0,1]:
		print "that is not possible."
		error()
	else:
		Note = user_input19

	user_input10 = int(raw_input("enter a number: "))
	print " "
	if user_input10 < 5:
		print "that is not possible."
		error()
	user_damage = user_input10

	user_input11 = int(raw_input("enter a number: "))
	print " "
	if user_input11 not in [0,1]:
		print "that is not possible."
		error()
	else:
		cactus_stone = user_input11

	user_input12 = int(raw_input("enter a number: "))
	print " "
	if user_input12 not in [0,1]:
		print "that is not possible."
		error()
	else:
		rifleget = user_input12

	user_input13 = int(raw_input("enter a number: "))
	print " "
	if user_input13 not in [0,1]:
		print "that is not possible."
		error()
	message = user_input13

	user_input14 = int(raw_input("enter a number: "))
	print " "
	if user_input14 not in [0,1,2,3,4,5]:
		print "that is not possible."
		error()
	opinion = user_input14

	user_input15 = int(raw_input("enter a number: "))
	print " "
	if user_input15 not in [0,1]:
		print "that is not possible."
		error()
	ruby = user_input15

	user_input16 = int(raw_input("enter a number: "))
	print " "
	if user_input16 not in [0,1]:
		print "that is not possible."
		error()
	doll = user_input16

	user_input20 = int(raw_input("enter a number: "))
	print " "
	if user_input20 not in [0,1]:
		print "that is not possible."
		error()
	else:
		r2door = user_input20

	print "now enter the number in the very bottom"
	print "right corner, that is separated by a colon."
	user_input17 = int(raw_input( ">>> "))
	if user_input17 not in [0,1]:
		print "that is not possible."
		error()
	elif user_input17 == 0:
		checkpoint = 0
		print " "
		print "starting game..."
		time.sleep(1.5)
		print " "
		start_point()
	elif user_input17 == 1:
		checkpoint = 1
		print " "
		print "starting game..."
		time.sleep(1.5)
		print " "
		go.start_point()
	else:
		print "that is not possible."
		error()

#pregame functions.
def game_mode():
	global change
	change = 1.01
	percent_change = 100

	while change == 1.01:
		change_set = int( raw_input( """
Welcome, adventurer.
This game has several game modes.

1. Nerd
2. Normal
3. Challenging
4. Woo Mama

press the corresponding number
to choose. Normal is the standard
mode.
""" ) )
		if change_set == 1:
			print "You chose Nerd mode...oh boy"
			percent_change = 80
			change = .80
		elif change_set == 2:
			print "You chose Normal mode."
			percent_change = 100
			change = 1.00
		elif change_set == 3:
			print "You chose Challenging mode. good luck."
			percent_change = 120
			change = 1.20
		elif change_set == 4:
			print "Woo Mama! Be prepared for many frustrations. good luck, adventurer."
			percent_change = 140
			change = 1.40
		else:
			print "user error. unrecognized input."

	print ' '
	print "Based on the difficulty you have selected,"
	print "damage you take will be", percent_change, "percent of the standard amount of damage."
	print " "

	while True:
		gm_continue = raw_input( 'press go to proceed. press quit to quit. ' )
		if gm_continue == 'go':
			break
		elif gm_continue == 'quit':
			quit( "user prompt. program terminated." )
		else:
			print "user error. unrecognized input."

	game_start()

def game_menu():
	first_percent = random.randint(2,7)
	second_percent = random.randint(18,37)
	third_percent = random.randint(45,67)
	fourth_percent = random.randint(78,89)

	print "Loading game..."
	time.sleep(2)
	print first_percent, "percent"
	time.sleep(1.3)
	print second_percent, "percent"
	time.sleep(1)
	print third_percent, "percent"
	time.sleep(.7)
	print fourth_percent, "percent"
	time.sleep(.5)
	print "100 percent"
	time.sleep(1)
	print "initializing..."
	time.sleep(4)

	print " "
	print "#### ##### ######### ###  ### #   #"
	time.sleep(.1)
	print "#   ##    #      #  #   ##   # # #"
	time.sleep(.1)
	print "#   ##### ####   #  #### #   #  #"
	time.sleep(.1)
	print "#   ##        #  #  #  # #   #  #"
	time.sleep(.1)
	print "#### #########   #  #   # ###   #"
	time.sleep(.1)
	print "==================================="
	time.sleep(.1)
	print "     #### ####|# #####  ## ###"
	time.sleep(.1)
	print "      # ##### |##  # #  # ###"
	time.sleep(.1)
	print "      # # ####|# #############"
	time.sleep(.1)
	print "************^=========^************"
	time.sleep(.1)
	print "************^LEMONZETZ^************"
	time.sleep(.1)
	print "************^=========^************"
	time.sleep(.1)
	print ' '
	time.sleep(.1)
	print "Destroy the Kilge."
	time.sleep(.1)
	print "2015. Created by Lemonzetz Games."
	time.sleep(4)

	hintboy = raw_input('''
HINT:
read the readme.txt file for
instructions on how to use the
game. (it should be in the
same folder as this game)

with that said...

Press start to begin.
Press password to enter a password.
Press quit to quit.
''' )
	if hintboy == "start":
		game_mode()
	elif hintboy == "quit":
		quit( 'user prompt. program terminated.' )
	elif hintboy == "password":
		password_system()
	else:
		quit( "input not recognized. program terminated." )

def game_start():
	print " "
	gs_continue = raw_input( "Would you like to see the pre-game dialogue? " )
	if gs_continue == 'yes':
		opening()
	elif gs_continue == 'no':
		main()
	else:
		print " "
		print "user error. Unrecognized input."
		time.sleep(.5)
		print "Loading failsafe..."
		time.sleep(2)
		print "system override. Running dialogue function."
		time.sleep(3)
		opening()

def opening():
	print '''
jersy girl walks up.
smacks gum loudly.

"Alright. I could spend HOURS
telling you what you should know.
Here's what you need. Your mission
is to scout and or destroy the Kilge.
get to it."

You jump out of a plane and parachute
down to the drop zone in a desert
'''
	while True:
		gogo = raw_input( "call main loop? (start playing) (y/n) " )
		if gogo == 'y':
			break
		elif gogo == 'n':
			quit( 'user prompt. program terminated. ' )
		else:
			print "user error. unrecognized input."

	main()

def main():
	print " "
	print "Destroy the Kilge"
	time.sleep(2)
	print " "
	print "..falling..........."
	time.sleep(4)
	print "CRASH.....the string snapped...oh dear.."
	time.sleep(2)
	print '"Logic. I have Logic."'
	time.sleep(4)
	print '''
(begins to think out loud)
"I have my wits. my reason. my mission.
The rest is blank.." (combines observations
of broken parachute, blood stained rock, and
thumping head) "I hit my head. On my mission?
What do I remember? Scout, and destroy the Kilge.
Target of unknown origins. How? Why?" (observes
note on ground. reads)

	Better get moving before the
	cactus people come. -Kilge

".....????????"
'''
	start_point()

#===================================
#program start commands, variables, and such

#imports
import random
import time
import main2 as go

#variables
water = 1
health = 100
weapon = 1.0 
change = 1.00 
battlevar = 1
user_damage = 5
cactus_juice = 0
water_main = 1
weaponlist = [1.0] 
ruby = 0
doll = 0
key = 0
opinion = 0
message = 0
rifleget = 0
cactus_stone = 0
checkpoint = 0
Gate = 0
rdefeat = 0
controlrwhat = 0
Note = 0
r2door = 0
