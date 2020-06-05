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

#The function below needs an update.
def getDead(hp, dead, characters, loop, storyFull):
    tempDead = []
    for i in range(len(hp)):
        if hp[i] <= 0 and not dead[i]:
            tempDead.append(True)
            print(characters[1] + " morreru.")
            storyFull = storyFull + characters[i] + " morreu no dia " + str(loop) + ". "
        elif hp[i] <= 0:
            tempDead.append(True)
        else:
            tempDead.append(False)
    return storyFull, tempDead


"""Win/lose Functions"""

def lost(werewolf, dead):
    tempDeathCount = 0
    for i in range(len(werewolf)):
        if not werewolf[i] and dead[i]:
            tempDeathCount = tempDeathCount + 1
    if tempDeathCount >= (len(characters) - int(len(characters)/3)):
        return True
    return False

def won(werewolf, dead):
    tempDeathCount = 0
    for i in range(len(werewolf)):
        if werewolf[i] and dead[i]:
            tempDeathCount = tempDeathCount + 1
    if tempDeathCount >= int(len(werewolf)/3):
        return True
    return False

def isFinished(werewolf, dead, storyFull):
    if lost(werewolf, dead):
        storyFull = storyFull + "\n \nOs lobos vencem."
        return storyFull,False

    elif won(werewolf, dead):
        storyFull = storyFull + "\n \nOs náufragos vencem."
        return storyFull,False
    return storyFull, True


"""Cycle Functions"""

def night(characters, werewolf, sleepy, inside, hp, dead, storyFull):
    attacked = []
    sleepy_next = sleepy
    i = 0
    storyFull = storyFull + " " + "O dia virou noite."
    print("O dia virou noite.")
    storyFull = storyFull + " " + "Os lobos acordam."
    print("Os lobos acordam.")
    for isWerewolf in werewolf:
        if isWerewolf:
            victim = input(characters[i] + ", Quem você gostaria de visistar?")
            if victim in characters:
                if randint(0, 2) > 1:
                    sleepy_next[i] = True
                attacked.append(victim)
                inside[i] = False
                storyFull = (storyFull + " " + str(characters[i]) + " ataca "
                + str(attacked[-1]) + ".")
                print(str(characters[i]) + " ataca " + str(attacked[-1]) + ".")
        i = i + 1

    i = 0
    storyFull = storyFull + " " + "Os dorminhocos acordam."
    print("Os dorminhocos acordam.")
    for isSleepy in sleepy:
        if isSleepy:
            sleepy_next[i] = False
            visit = input(characters[i] + ", Escolha alguma casa para visitar ")
            if visit in characters:
                inside[i] = False
                if inside[getCharacter(visit, characters)]:
                    print(str(characters[i]) + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + " e o encountra ")
                    storyFull = (storyFull + " " + str(characters[i])
                    + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + " e o encountra " + ".")
                else:
                    print(str(characters[i]) + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + ",porém não o encountra")
                    storyFull = (storyFull + " " + str(characters[i])
                    + " visita "
                    + str(characters[getCharacter(visit, characters)])
                    + ",porém não o encountra" + ".")
        i = i + 1
    for victims in attacked:
        if not inside[getCharacter(victims, characters)]:
            hp[getCharacter(victims, characters)] = hp[getCharacter(victims, characters)] - 4
        else:
            hp[getCharacter(victims, characters)] = hp[getCharacter(victims, characters)] - 2

    return characters, werewolf, sleepy_next, inside, hp, dead, storyFull

def day(characters, werewolf, sleepy, inside, hp, dead, storyFull):
    executed = input("A noite virou dia. Os náufragos escolhem alguém para executar: ")
    storyFull = storyFull + "\n \nA noite virou dia, os sobreviventes acordam e escolhem " + str(executed) + " para ser executado. "
    hp[getCharacter(executed, characters)] = 0

    return characters, werewolf, sleepy, inside, hp, dead, storyFull


"""Main loop"""
loop = 0
while requesting:
    """Does night cycle and update deaths"""
    characters, werewolf, sleepy, inside, hp, dead, storyFull = night(characters,
                                                            werewolf, sleepy,
                                                            inside, hp, dead,
                                                            storyFull)
    storyFull, dead = getDead(hp, dead, characters, loop, storyFull)
    print(hp)
    storyFull, requesting = isFinished(werewolf, dead, storyFull)

    loop = loop + 1

    if requesting:
        """Does day cycle and update deaths"""
        characters, werewolf, sleepy, inside, hp, dead, storyFull = day(characters,
                                                                werewolf, sleepy,
                                                                inside, hp, dead,
                                                                storyFull)
        storyFull, dead = getDead(hp, dead, characters, loop, storyFull)

    print(hp)
    storyFull, requesting = isFinished(werewolf, dead, storyFull)

    loop = loop + 1
print(storyFull)
    
