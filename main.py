from os import listdir
from random import randint

"""Essa seção inteira existe para criação de jogadores e de eventos"""

storyFull = ''

requesting = True
characters = []

while requesting:
    player = input('Type the name of a player, type "Done" when done: ')
    if player != "Done":
        characters.append(player)
    else:
        requesting = False

trust = [[100]*len(characters) for i in characters]
hp = [4]*len(characters)
inside = [True]*len(characters)
werewolf = [False]*len(characters)
healingpotion = [False]*len(characters)
knife = [False]*len(characters)
sleepy = [False]*len(characters)

for i in range(int(len(characters)/3)):
    werewolf[randint(0, len(characters) - 1)] = True

requesting = True

events = []

for event in listdir("Events/"):
    events.append("Events/" + str(event))


"""Essa seção define funções"""


def getCharacter(name, characters):
    num = 0
    for i in characters:
        if i == name:
            return num
        num = num + 1


def noite(characters, werewolf, sleepy, inside, hp, storyFull):
    attacked = []
    sleepy_next = sleepy
    i = 0
    storyFull = storyFull + "\n O dia virou noite."
    for isWerewolf in werewolf:
        storyFull = storyFull + "Os lobos acordam."
        if isWerewolf:
            victim = input(characters[i] + ", Quem você gostaria de visistar?")
            if victim in characters:
                if randint(0, 2) > 1:
                    sleepy_next[i] = True
                attacked.append(victim)
                inside[i] = False
                storyFull = (storyFull + str(characters[i]) + "ataca"
                + str(attacked[-1]) + ".")
        i = i + 1

    i = 0
    for isSleepy in sleepy:
        storyFull = storyFull + "Os dorminhocos acordam."
        if isSleepy:
            sleepy_next[i] = False
            visit = input(characters[i] + ", Escolha alguma casa para visitar")
            if visit in characters:
                inside[i] = False
                if inside[getCharacter(visit, characters)]:
                    print(str(characters[i]) + "visita"
                    + str(characters[getCharacter(visit, characters)])
                    + " e o encountra")
                    storyFull = (storyFull + str(characters[i])
                    + "visita"
                    + str(characters[getCharacter(visit, characters)])
                    + "e o encountra" + ".")
                else:
                    print(str(characters[i]) + "visita"
                    + str(characters[getCharacter(visit, characters)])
                    + ",porém não o encountra")
                    storyFull = (storyFull + str(characters[i])
                    + "visita"
                    + str(characters[getCharacter(visit, characters)])
                    + ",porém não o encountra" + ".")
        i = i + 1
    for victims in attacked:
        if not inside[getCharacter(victims, characters)]:
            hp[getCharacter(victims, characters)] = hp[getCharacter(victims, characters)] - 4
        else:
            hp[getCharacter(victims, characters)] = hp[getCharacter(victims, characters)] - 2
    return characters, werewolf, sleepy_next, inside, hp, storyFull


while requesting:
    characters, werewolf, sleepy, inside, hp, storyFull = noite(characters,
                                                            werewolf, sleepy,
                                                            inside, hp,
                                                            storyFull)
    print(hp)
