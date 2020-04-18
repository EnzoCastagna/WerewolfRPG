from os import listdir

requesting = True
characters = []

while requesting:
    player = input('Type the name of a player, type "Done" when done: ')
    if player != "Done":
        characters.append(player)
    else:
        requesting = False

requesting = True

events = []

for event in listdir("Events/"):
    events.append("Events/" + str(event))


