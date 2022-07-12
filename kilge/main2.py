#program goes here from main.py then from here goes to "program start"
def start_point():
	print "you enter the bunker, wandering what will happen..."
	import main as a
	import time
	time.sleep(1)
	a.checkpoint = 1
	first_room()

#location functions
def first_room():
	import main as a
	print "this is the bunker entrance."
	print "there is no sign of activity, but"
	print "all the systems are running fine."
	while True:
		fr_choice = raw_input("you can go to the long hallway, or the iron gate. ")
		if fr_choice == "menu":
			a.menu_call()
		elif fr_choice == "l":
			long_hallway()
		elif fr_choice == "i":
			a.iron_gate()
		else:
			print "user error. unrecognized input."

def long_hallway():
	import main as a
	print " "
	print "this is the long hallway."
	while True:
		print """
you can go to the main room, the first room,
room1, room2, room3, room4, room5, room6,
room7, or room8."""
		lh_input = raw_input(">>> ")
		if lh_input == "menu":
			a.menu_call()
		elif lh_input == "m":
			main_room()
		elif lh_input == "f":
			first_room()
		elif lh_input == "1":
			room1()
		elif lh_input == "2":
			room2()
		elif lh_input == "3":
			room3()
		elif lh_input == "4":
			room4()
		elif lh_input == "5":
			room5()
		elif lh_input == "6":
			room6()
		elif lh_input == "7":
			room7()
		elif lh_input == "8":
			room8()
		else:
			print "user error. unrecognized input."

def gate():
	import main as a
	import time
	if a.Gate == 0:
		print "enter the password."
		print "password format:"
		print "XX:XX:XX:XX:XX:XX:XX:XX"
		print "(enter the colons as well)"
		password = raw_input(">>> ")
		if password == "09:58:47:99:42:43:81:78":
			print " "
			print "the gate opens..."
			print "it sounds like another door opened as well."
			print " "
			time.sleep(1.5)
			a.Gate = 1
			a.r2door = 1
		else:
			print " "
			print "that is incorrect."
			print "you have to open to the gate to"
			print "progress farther."
			print "returning to long hallway..."
			print " "
			long_hallway()
	else:
		pass
#numbered rooms
def room1():
	import main as a
	small_drone()
	a.waterget()
	print " "
	print "this is room1."
	print '"78" is written on the wall with a large "8" next to it.'
	print " "
	while True:
		r1_input = raw_input("you can go back to the long hallway. ")
		if r1_input == "l":
			long_hallway()
		elif r1_input == "menu":
			a.menu_call()
		else:
			print "user error. unrecognized input."

def room2():
	import main as a
	global r2door
	small_drone()
	small_drone()
	a.waterget()
	print " "
	print "this is room2."
	print '"81" is written on the wall with a large "7" next to it.'
	print " "
	if a.r2door == 0:
		while True:
			r2_input = raw_input("you can go back to the long hallway. ")
			if r2_input == "l":
				long_hallway()
			elif r2_input == "menu":
				a.menu_call()
			else:
				print "user error. unrecognized input."
	elif a.r2door == 1:
		while True:
			r2_input = raw_input("you can go to the secret room or back to the long hallway. ")
			if r2_input == "l":
				long_hallway()
			elif r2_input == "menu":
				a.menu_call()
			elif r2_input == "s":
				secret_room()
			else:
				print "user error. unrecognized input."
	else:
		print "something went wrong with the r2door variable most likely."
		a.error()

def secret_room():
	import main as a
	print " "
	print "this is the secret room"
	print " "
	if 60 not in a.weaponlist:
		if 40 in a.weaponlist:
			a.weaponlist.append(60.0)
			a.weaponlist.remove(40.0)
			a.weapon = 60.0
			print " "
			print "you found an upgrade for your mechsuit."
			print " "
	
	while True:
		sr_input = raw_input("you can go to the room2. ")
		if sr_input == "menu":
			a.menu_call()
		elif sr_input == "2":
			room2()		

def room3():
	import main as a
	small_drone()
	a.waterget()
	print " "
	print "this is room3."
	print '"42" is written on the wall with a large "5" next to it.'
	print " "
	while True:
		r3_input = raw_input("you can go back to the long hallway. ")
		if r3_input == "l":
			long_hallway()
		elif r3_input == "menu":
			a.menu_call()
		else:
			print "user error. unrecognized input."

def room4():
	import main as a
	small_drone()
	a.waterget()
	print " "
	print "this is room4."
	print '"09" is written on the wall with a large "1" next to it.'
	print " "
	while True:
		r4_input = raw_input("you can go back to the long hallway. ")
		if r4_input == "l":
			long_hallway()
		elif r4_input == "menu":
			a.menu_call()
		else:
			print "user error. unrecognized input."

def room5():
	import main as a
	small_drone()
	a.waterget()
	print " "
	print "this is room5."
	print '"43" is written on the wall with a large "6" next to it.'
	print " "
	while True:
		r5_input = raw_input("you can go back to the long hallway. ")
		if r5_input == "l":
			long_hallway()
		elif r5_input == "menu":
			a.menu_call()
		else:
			print "user error. unrecognized input."

def room6():
	import main as a
	small_drone()
	a.waterget()
	print " "
	print "this is room6."
	print '"47" is written on the wall with a large "3" next to it.'
	print " "
	while True:
		r6_input = raw_input("you can go back to the long hallway. ")
		if r6_input == "l":
			long_hallway()
		elif r6_input == "menu":
			a.menu_call()
		else:
			print "user error. unrecognized input."

def room7():
	import main as a
	small_drone()
	a.waterget()
	print " "
	print "this is room7."
	print '"58" is written on the wall with a large "2" next to it.'
	print " "
	while True:
		r7_input = raw_input("you can go back to the long hallway. ")
		if r7_input == "l":
			long_hallway()
		elif r7_input == "menu":
			a.menu_call()
		else:
			print "user error. unrecognized input."

def room8():
	import main as a
	small_drone()
	a.waterget()
	print " "
	print "this is room8."
	print '"99" is written on the wall with a large "4" next to it.'
	print " "
	while True:
		r8_input = raw_input("you can go back to the long hallway. ")
		if r8_input == "l":
			long_hallway()
		elif r8_input == "menu":
			a.menu_call()
		else:
			print "user error. unrecognized input."

def main_room():
	import main as a
	gate()
	small_drone()
	combat_robot()
	a.waterget()

	print " "
	print "this is the main room."
	print " "
	while True:
		mr_input = raw_input("you can go to the long hallway, the much-too-waxed hall, or the inner entrance. ")
		if mr_input == "menu":
			a.menu_call()
		elif mr_input == "l":
			long_hallway()
		elif mr_input == "m":
			waxed_floor()
		elif mr_input == "i":
			inner_entrance()	
		else:
			print "user error. unrecognized input."

def waxed_floor():
	import main as a
	print " "       
	print "this is the much-too-waxed hall"
	print " "
	while True:
		wf_input = raw_input("you can go to the control room, or the main room. ")
		if wf_input == "menu":
			a.menu_call()
		elif wf_input == "m":
			main_room()
		elif wf_input == "c":
			control_room()
		else:
			print "user error. unrecognized input."			

def control_room():
	import main as a
	small_drone()
	combat_robot()
	a.waterget()

	print " "
	print "this is the control room."
	print " "
	if a.controlrwhat == 0:
		print "control panels, switches, and buttons line the room,"
		print "completely filling the entire area. Moniters also stand"
		print "in a row. Wait...Something moved in one of them."
		print "didnt it?"
		print " "
		a.controlrwhat = 1
	else:
		pass	
	while True:
		cr_input = raw_input("you can go to the much-too-waxed hall or the ventilation shaft. ")
		if cr_input == "m":
			waxed_floor()
		elif cr_input == "menu":
			a.menu_call()	
		elif cr_input == "v":
			ventilation_shaft()	
		else:
			print "user error. unrecognized input."	

def ventilation_shaft():
	import main as a
	AC()
	heat()
	print " "
	print "this is the ventilation_shaft."
	print "nothing here but some old mustard..."
	print " "
	while True:
		vs_input = raw_input("you can go to the large vent or the control room. ")
		if vs_input == "menu":
			a.menu_call()
		elif vs_input == "c":
			control_room()
		elif vs_input == "l":
			large_vent()
		else:
			print "user error. unrecognized input."			

def large_vent():
	import main as a
	AC()
	heat()
	print " "			
	print "this is the large vent"
	print " "
	while True:
		mv_input = raw_input("You can go to the ventilation shaft or the air duct. ")
		if mv_input == "menu":
			a.menu_call()
		elif mv_input == "v":
			ventilation_shaft()
		elif mv_input == "a":
			air_duct()
		else:
			print "user error. unrecognized input."			

def air_duct():
	import main as a
	AC()
	heat()
	if a.Note == 0:
		print " "
		print "there is a letter on the ground."
		print "It reads:"
		print " "
		print "My name is Josh Rhames. I survived the bombs."
		print "The bombs hit hard. I am the only survivor from"
		print "my city. It has been 8 months since the bombing now"
		print "and I have built a stronghold. Rumors have begun to"
		print "spread about a second attack."
		print " "
		print "It will start with a scout who will come to find us."
		print "That scout will report back to the headquarters to direct"
		print "a more accurate bombing. I dont know if anyone out there"
		print "survived, but if anyone can hear this, come to my stronghold."
		print "I am the Kilge. I will protect you."
		print " "
		a.opinion = 5
		print "what is this?"
		print " "
		print "this is the air duct."
		print " "
		a.Note = 1
	else:
		pass	
	while True:
		ad_input = raw_input("you can go to the large vent or the main room. ")
		if ad_input == "menu":
			a.menu_call()
		elif ad_input == "l":
			large_vent()
		elif ad_input == "m":
			print " "		
			print "you fell down into the main room."
			print " "
			main_room()
		else:
			print "user error. unrecognized input."	

def inner_entrance():
	import main as a
	small_drone()
	combat_robot()
	a.waterget()
	print " "
	print "this is the inner entrance."
	print "there is a ward that looks like a squid."
	print " "
	while True:
		ie_input = raw_input("you can go to the main room, the ward, or the corner room. ")
		if ie_input == "menu":
			a.menu_call()
		elif ie_input == "m":
			main_room()	
		elif ie_input == "w":
			ward()
		elif ie_input == "c":
			corner_room()	
		else:
			print "user error. unrecognized input."	

def ward():
	import main as a
	a.waterget()
	a.waterget()
	a.waterget()
	print " "
	print "this is the ward, a safe place from enemies."
	print " "
	while True:
		w_input = raw_input("you can go to the inner entrance, or the suspiciously opened vault. ")
		if w_input == "menu":
			a.menu_call()
		elif w_input == "i":
			inner_entrance()
		elif w_input == "s":
			opened_vault()
		else:
			print "user error. unrecognized input."			

def corner_room():
	import main as a
	small_drone()
	small_drone()
	small_drone()
	combat_robot()
	combat_robot()
	a.waterget()
	print " "
	print "this is the corner room. Lots of enemies hang out here."
	print " "
	while True:
		cr_input = raw_input("you can go to the inner entrance or the suspiciously opened vault. ")
		if cr_input == "menu":
			a.menu_call()
		elif cr_input == "i":
			inner_entrance()
		elif cr_input == "s":
			opened_vault()	
		else:
			print "user error. unrecognized input."		

def opened_vault():
	import main as a
	small_drone()
	combat_robot()
	a.waterget()
	print " "
	print "this is the suspiciously opened vault."
	print " "
	while True:
		ov_input = raw_input("you can go to the ward, corner room, or the armory. ")
		if ov_input == "menu":
			a.menu_call()
		elif ov_input == "w":
			ward()
		elif ov_input == "c":
			corner_room()
		elif ov_input == "a":
			armory()	
		else:
			print "user error. unrecognized input."			

def armory():
	import main as a
	small_drone()
	combat_robot()
	a.waterget()
	if 100 not in a.weaponlist:
		a.weaponlist.append(100)
		a.weapon = 100
		print " "
		print "you found an even better mech suit!"
		print "better not just leave it lying around."
		print " "
	print " "	
	print "this is the armory."
	print " "
	while True:
		a_input = raw_input("you can go to the suspiciously opened vault, or the prominent hallway. ")
		if a_input == "menu":
			a.menu_call()
		elif a_input == "s":
			opened_vault()	
		elif a_input == "p":
			prominent_hallway()
		else:
			print "user error. unrecognized input."		

def prominent_hallway():
	import main as a
	small_drone()
	small_drone()
	small_drone()
	combat_robot()
	combat_robot()
	combat_robot()
	print " "
	print "this is the prominent hallway."
	print " "
	while True:
		ph_input = raw_input("you can go to the vault or the narrow hallway. ")
		if ph_input == "menu":
			a.menu_call()
		elif ph_input == "v":
			opened_vault()
		elif ph_input == "n":
			narrow_hallway()
		else:
			print "user error. unrecognized input."			

def narrow_hallway():
	import main as a			
	small_drone()
	small_drone()
	small_drone()
	combat_robot()
	combat_robot()
	combat_robot()
	print " "
	print "this is the narrow hallway."
	print " "
	while True:
		nh_input = raw_input("you can go to the prominent hallway or the strategy room. ")
		if nh_input == "menu":
			a.menu_call()
		elif nh_input == "p":
			prominent_hallway()
		elif nh_input == "s":
			if a.Note != 0:
				stratagy_room()
			else:
				print "you cant go to the strategy room yet."		
				print "search around and come back later."		
		else:
			print "user error. unrecognized input."	

def stratagy_room():
	battle_again()
	shelter()

def shelter():
	import time
	time.sleep(2)
	print " "	
	print " "
	print "you enter the shelter..."
	time.sleep(5)
	print " "
	print " "
	print '"Please dont kill us again," she pleads.'
	time.sleep(5)
	quit()

#battle functions
def small_drone():
	import random
	import main as a
	sd_chance = random.randint(1,5)
	if sd_chance == 2:
		print " "
		print "a small drone zips in out of nowhere!"
		print " "
		enemy = 500
		while True:
			number = random.randint(1,13) * a.hit_miss()
			enemy_damage = random.randint(0,100) * a.change * a.attack_number()
			print "health =", a.health
			print "enemy health =", enemy
			print "you have", a.water, "water."

			action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)
			if action == "1":
				enemy = enemy - a.user_damage * a.weapon * a.hit_miss()
			elif action == "2":
				enemy = enemy - number * a.weapon * a.hit_miss()
			elif action == "3":
				if a.water >= 1:
					print 'you drank water and gained 30 health points.'
					a.health = a.health + 30
					a.water = a.water - 1
				if a.water == 0:
					print "you dont have any water to drink."
			else:
				print "user error. unrecognized input."
				pass
			if enemy <= 0:
				print 'you defeated the enemy.'
				break
			a.health = a.health - enemy_damage * a.attack_number()
			if a.health <= 0:
				quit( "you died. " )
			print 'the small drone hit you', a.attack_number(), 'times for', enemy_damage, 'damage.'
		else:
			pass
	else:
		pass

def combat_robot():
	import random
	import time
	import main as a
	cr_chance = random.randint(0,7)
	if cr_chance == 3:
		print " "
		print "a combot robot wheels toward you."
		print " "
		time.sleep(1.5)
		enemy = 600
		while True:
			number = random.randint(1,13) * a.hit_miss()
			enemy_damage = random.randint(30,40) * a.change * a.attack_number()
			print "health =", a.health
			print "enemy health =", enemy
			print "you have", a.water, "water."

			action = raw_input( """
1. basic attack
2. special attack
3. drink water
"""	)
			if action == "1":
				enemy = enemy - a.user_damage * a.weapon * a.hit_miss()
			elif action == "2":
				enemy = enemy - number * a.weapon * a.hit_miss()
			elif action == "3":
				if a.water >= 1:
					print 'you drank water and gained 30 health points.'
					a.health = a.health + 30
					a.water = a.water - 1
				if a.water == 0:
					print "you dont have any water to drink."
			else:
				print "user error. unrecognized input."
				pass
			if enemy <= 0:
				print 'you defeated the enemy.'
				break
			a.health = a.health - enemy_damage * a.attack_number()
			if a.health <= 0:
				quit( "you died. " )
			print 'the combat robot hit you', a.attack_number(), 'times for', enemy_damage, 'damage.'
		else:
			pass

def battle_again():
	import main as a
	import time
	import random
	enemy = 2000
	time.sleep(1)
	print " "
	print " "
	print " "
	print "A MECH SUIT STANDS IN FRONT OF YOU."
	print " "
	print " "
	print " "
	time.sleep(3)
	while True:
		number = random.randint(1,13) * a.hit_miss()
		enemy_damage = random.randint(20,400) * a.change * a.attack_number()
		print "health =", a.health
		print "enemy health =", enemy
		print "you have", a.water, "water."

		action = raw_input( """
1. basic attack
2. special attack	
3. drink water 
"""	)
		if action == "1":
			enemy = enemy - a.user_damage * a.weapon * a.hit_miss()	
		elif action == "2":
			enemy = enemy - number * a.weapon * a.hit_miss()
		elif action == "3":
			if a.water >= 1:
				print 'you drank water and gained 30 health points.'
				a.health = a.health + 30
				a.water = a.water - 1
			if a.water == 0:		
				print "you dont have any water to drink."
		else:
			print "user error. unrecognized input."
			pass
		if enemy <= 0:
			print 'you defeated the mech suit.'
			break
		a.health = a.health - enemy_damage * a.attack_number()
		if a.health <= 0:
			quit( "you died. " )
		print 'the mech suit hit you', a.attack_number(), 'times for', enemy_damage, 'damage.'
	else:
		pass			

#ventilation battle functions
def heat():
	import main as a			
	import random
	import time
	hchance = random.randint(0,4)
	if hchance == 2:
		time.sleep(1.5)
		print " "
		print "Oh no! Someone turned on the heat!"
		print " "
		time.sleep(1.5)
		a.health = a.health - 40
		a.water = 0
		print "the hot air burned you, but you'll be ok."
		print "all your water evaporated."

def AC():
	import main as a	
	import random
	import time	
	ACchance = random.randint(0,6)
	if ACchance == 5:
		time.sleep(1.5)
		print " "
		print "Oh no! Someone turned on the AC!"
		print " "
		time.sleep(1.5)
		a.health = a.health - 60
		print "the cold air really shook you up."