from random import choice
import sys

def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i+order]
        next_letter = text[i+order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model

def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)

def generateText(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0:order]
    output = ""
    for i in range(0, length-order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    print output

text = "Intro we dont care graduation day all falls down Ill fly away spaceship jesus walks never let me down get em high workout plan the new workout plan slow jamz breathe in breathe out school spirit skit 1 school spirit school spirit skit 2 lil jimmy skit two words through the wire family business last call wake up mr west heard em say touch the sky gold digger skit 1 drive slow my way home crack music roses bring me down addiction skit 2 diamonds from sierra leone we major skit 3 Hey mama celebration skit 4 gone diamonds from sierra leone late good morning champion stronger I wonder good life cant tell me nothing barry bonds drunk & hot girls flashing lights everything I am the glory homecoming big brother good night bittersweet poetry say you will welcome to heartbreak heartless amazing love lockdown paranoid robocop street lights bad news see you in my nightmares coldest winter pinocchio story dark fantasy gorgeous power all of the lights monster so appalled devil in a new dress runaway hell of a life blame game lost in the world who will survive in america see me now no church in the wild lift off niggas in paris otis gotta have it new day thats my bitch welcome to the jungle who gon stop me murder to excellence made in america why I love you illest motherfucker alive h.a.m primetime the joy to the world clique mercy new god flow the morning cold higher sin city the one creepers bliss I dont like on sight black skinhead I am a god new slaves hold my liquor im in it blood on the leaves guilt trip send it up bound 2 ultralight beam father stretch my hands pt 1 father stretch my hands pt 2 famous feedback low lights highlights freestyle 4 I love kanye waves fml real friends wolves franks track siiiiiiiiilver surffffeeeeer intermission 30 hours no more parties in la facts charlie heat version fade saint pablo "
if __name__ == "__main__":
    generateText(text, 2, 65)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 75) 
if __name__ == "__main__":
    generateText(text, 2, 60)
if __name__ == "__main__":
    generateText(text, 2, 65)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 55) 
if __name__ == "__main__":
    generateText(text, 2, 60)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 60)
if __name__ == "__main__":
    generateText(text, 2, 50) 
if __name__ == "__main__":
    generateText(text, 2, 60)
if __name__ == "__main__":
    generateText(text, 2, 50)
print ""
if __name__ == "__main__":
    generateText(text, 2, 50)