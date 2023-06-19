from easyinput import read

dicPlayers = {}

for i in range(read(int)):
	
	name, puntuation = read(str,int)
	
	player = {puntuation : name}
	
	dicPlayers.update(player)

orderdicplayers = sorted(dicPlayers, reverse = True)

for i in range(len(orderdicplayers)):
	if i == 0:
		print(f"Gold: {dicPlayers.get(orderdicplayers[i])}")
	elif i == 1:
		print(f"Silver: {dicPlayers.get(orderdicplayers[i])}")
	elif i == 2:
		print(f"Bronze: {dicPlayers.get(orderdicplayers[i])}")
	else:
		print(f"{dicPlayers.get(orderdicplayers[i])}")
