from os import listdir
from random import randint

"""Essa seção inteira existe para criação de jogadores e de eventos"""

storyFull = ''

requesting = True
characters = []

characters = input("Qual é o nome de cada um dos náufragos? Moderador: " +
                   "Insira os nomes separados por Vírgula. Ex: Gustavo,"
                   + " Enzo: ").split(", ")

trust = [[100]*len(characters) for i in characters]
hp = [4]*len(characters)
inside = [True]*len(characters)
werewolf = [False]*len(characters)
healingpotion = [False]*len(characters)
knife = [False]*len(characters)
sleepy = [False]*len(characters)
dead = [False]*len(characters)

for i in range(int(len(characters)/3)):
    werewolf[randint(0, len(characters) - 1)] = True

requesting = True

events = []

for event in listdir("Events/"):
    events.append("Events/" + str(event))


"""Status Functions"""

def getCharacter(name, characters):
    num = 0
    for i in characters:
        if i == name:
            return num
        num = num + 1

def getDead(hp):
    tempDead = []
    for hps in hp:
        if hp <= 0:
            tempDead.append(True)
        else:
            tempDead.append(True)
    return tempDead


"""Win/lose Functions"""

def lost(werewolf, dead):
    tempDeathCount = 0
    num = 0
    for i in len(werewolf):
        print(i)
        if not werewolf[i] == dead[i]:
            tempDeathCount = tempDeathCount + 1
    if tempDeathCount >= 2*int(len(characters)/3):
        return True
    return False


"""Cycle Functions"""

def night(characters, werewolf, sleepy, inside, hp, dead, storyFull):
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
                    print(str(characters[i]) + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + " e o encountra")
                    storyFull = (storyFull + str(characters[i])
                    + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + "e o encountra" + ".")
                else:
                    print(str(characters[i]) + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + ",porém não o encountra")
                    storyFull = (storyFull + str(characters[i])
                    + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + ",porém não o encountra" + ".")
        i = i + 1
    for victims in attacked:
        if not inside[getCharacter(victims, characters)]:
            hp[getCharacter(victims, characters)] = hp[getCharacter(victims, characters)] - 4
        else:
            hp[getCharacter(victims, characters)] = hp[getCharacter(victims, characters)] - 2
    return characters, werewolf, sleepy_next, inside, hp, storyFull

def day(characters, werewolf, sleepy, inside, hp, dead, storyFull):
    executed = input("Exexute alguém: ")
    hp[getCharacter(executed, characters)] = 0
    return characters, werewolf, sleepy, inside, hp, dead, storyFull


"""Main loop"""

while requesting:
    """Does night cycle and update deaths"""
    characters, werewolf, sleepy, inside, hp, dead, storyFull = night(characters,
                                                            werewolf, sleepy,
                                                            inside, hp, dead,
                                                            storyFull)
    dead = getDead(hp)

    """Does day cycle and update deaths"""
    characters, werewolf, sleepy, inside, hp, dead, storyFull = day(characters,
                                                            werewolf, sleepy,
                                                            inside, hp, dead,
                                                            storyFull)
    dead = getDead(hp)

    """Tests win/lost condition and ends game"""
    if lost(werewolf, dead):
        requesting = False

    #elif won(werwolf, dead):
    #    requesting = False

    
