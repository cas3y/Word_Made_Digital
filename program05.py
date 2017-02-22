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

text = "Intro We Dont Care Graduation Day All Falls Down Ill Fly Away Spaceship Jesus Walks Never Let Me Down Get Em High Workout Plan The New Workout Plan Slow Jamz Breathe In Breathe Out School Spirit Skit 1 School Spirit School Spirit Skit 2 Lil Jimmy Skit Two Words Through The Wire Family Business Last Call Wake Up Mr West Heard Em Say Touch The Sky Gold Digger Skit 1 Drive Slow My Way Home Crack Music Roses Bring Me Down Addiction Skit 2 Diamonds From Sierra Leone We Major Skit 3 Hey Mama Celebration Skit 4 Gone Diamonds From Sierra Leone Late Good Morning Champion Stronger I Wonder Good Life Cant Tell Me Nothing Barry Bonds Drunk & Hot Girls Flashing Lights Everything I Am The Glory Homecoming Big Brother Good Night Bittersweet Poetry Say You Will Welcome To Heartbreak Heartless Amazing Love Lockdown Paranoid RoboCop Street Lights Bad News See You In My Nightmares Coldest Winter Pinocchio Story Dark Fantasy Gorgeous Power All Of The Lights Monster So Appalled Devil In A New Dress Runaway Hell Of A Life Blame Game Lost In The World Who Will Survive In America See Me Now No Church In The Wild Lift Off Niggas In Paris Otis Gotta Have It New Day Thats My Bitch Welcome To The Jungle Who Gon Stop Me Murder To Excellence Made In America Why I Love You Illest Motherfucker Alive H.A.M Primetime The Joy To The World Clique Mercy New God Flow The Morning Cold Higher Sin City The One Creepers Bliss I Dont Like On Sight Black Skinhead I Am A God New Slaves Hold My Liquor Im In It Blood On The Leaves Guilt Trip Send It Up Bound 2 Ultralight Beam Father Stretch My Hands Pt 1 Father Stretch My Hands Pt 2 Famous Feedback Low Lights Highlights Freestyle 4 I Love Kanye Waves FML Real Friends Wolves Franks Track Siiiiiiiiilver Surffffeeeeer Intermission 30 Hours No More Parties In LA Facts Charlie Heat Version Fade Saint Pablo "
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50) 
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50) 
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50) 
if __name__ == "__main__":
    generateText(text, 2, 50)
if __name__ == "__main__":
    generateText(text, 2, 50) 
if __name__ == "__main__":
    generateText(text, 2, 50)