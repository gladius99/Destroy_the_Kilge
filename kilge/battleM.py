	global health
	global user_damage
	global water
	global weapon
	global battlevar
	global random
	global change

	while True:
		number = random.randint(1,13) * hit_miss()
		enemy_damage = random.randint(5,12) * change * attack_number()
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
			enemy = enemy - number * weapon * hit_miss()
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
			print 'you defeated the enemy.'
			break
		health = health - enemy_damage * attack_number()
		if health <= 0:
			quit( "you died. " )
		print 'the enemy hit you', attack_number(), 'times for', enemy_damage, 'damage.'
	else:
		pass

#for the second file
	enemy = 100
	while True:
		number = random.randint(1,13) * a.hit_miss()
		enemy_damage = random.randint(5,12) * a.change * a.attack_number()
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
		print 'the enemy hit you', a.attack_number(), 'times for', enemy_damage, 'damage.'
	else:
		pass		