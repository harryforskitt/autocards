from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

import random

class player:
    def __init__(self, number, name, cards):
        self.number = number
        self.name = name
        self.cards = cards

    def addcard(self, card):
        self.cards.append(card)

    def removecard(self, card):
        self.cards.remove(card)

class card:
    def __init__(self, name, number, dpsec, dpshot, rate, mag, rating):
        self.name = name
        self.number = number
        self.dpsec = dpsec
        self.dpshot = dpshot
        self.rate = rate
        self.mag = mag
        self.rating = rating

cards = []

#get adjectives
f=open('adj.txt')
lines=f.readlines()

guns = ["Revolver", "Pistol", "Shotgun", "Rifle", "Sub-machine Gun", "Machine gun"]

def makename():
    adj1 = str(lines[random.randrange(0, len(lines)-1)])
    adj1 = adj1.strip().capitalize()
    adj2 = str(lines[random.randrange(0, len(lines)-1)])
    adj2 = adj2.strip().capitalize()
    gun = guns[random.randrange(0, len(guns)-1)]
    gun = gun.strip()
    name = str(adj1+" "+adj2+" "+gun)
    return(name)


@app.route("/makecards/<int:number>", methods = ['GET', 'POST'])
def makecards(number):
    newcards = []
    for i in range(len(cards), len(cards)+number):
        name = makename()
        number = i
        dpshot = random.randrange(0, 100)
        rate = random.randrange(0, 100)
        dpsec = dpshot*rate
        mag = random.randrange(0, 100)
        rating = random.randrange(0, 100)
        cards.append(card(name, number, dpsec, dpshot, rate, mag, rating))
        newcards.append(card(name, number, dpsec, dpshot, rate, mag, rating))
        print(newcards)
    return(newcards)

@app.route("/getcard/<int:number>", methods = ['GET'])
def getcard(number):
    result = ""
    result+=(str(cards[number].name)+",")
    result+=(str(cards[number].number)+",")
    result+=(str(cards[number].dpsec)+",")
    result+=(str(cards[number].dpshot)+",")
    result+=(str(cards[number].rate)+",")
    result+=(str(cards[number].mag)+",")
    result+=(str(cards[number].rating)+"")
    return(result)

def compare(card1, card2, attribute):
    if card1.attribute > card2.attribute:
        return("card1")
    elif card2.attribute > card1.attribute:
        return("card2")
    else:
        return("draw")

human = player(0, "human", makecards(26))
computer = player(1, "computer", makecards(26))
players = []
players.append(human)
players.append(computer)
drawpile=[]

currentplayer = human
nocards = False
drew = False

@app.route("/play/<int:attribute>/<int:currentplayer>", methods = ['GET'])
def play(attribute, currentplayer):
    currentplayer=currentplayer
    attribute = attributes[int(attribute)-1]
    if getattr(human.cards[0], attribute) > getattr(computer.cards[0], attribute):
        print("Human wins!\n")
        winner = "human"
        drew = False
        human.cards.append(human.cards.pop(0))
        human.addcard(computer.cards[0])
        computer.removecard(computer.cards[0])
        for i in range(0, len(drawpile)):
            human.addcard(drawpile[i])
            drawpile.remove[i]
        currentplayer = "human"

    elif getattr(human.cards[0], attribute) < getattr(computer.cards[0], attribute):
        print("Computer wins!\n")
        winner = "computer"
        drew = False
        computer.cards.append(computer.cards.pop(0))
        computer.addcard(human.cards[0])
        human.removecard(human.cards[0])
        for i in range(0, len(drawpile)):
            computer.addcard(drawpile[i])
            drawpile.remove[i]
        currentplayer = "computer"
    else:
        print("Draw")
        winner = "draw"
        drew = True
        drawpile.append(human.cards[0])
        human.removecard(human.cards[0])
        drawpile.append(computer.cards[0])
        computer.removecard(computer.cards[0])
        currentplayer = "computer"

    result=str(currentplayer)
    return(result)

attributes = ["dpsec", "dpshot", "rate", "mag", "rating"]
attributenames = ["damage per second", "damage per shot", "fire rate", "magazine size", "Top Trumps rating"]

@app.route("/")
@cross_origin()
def home():
    return render_template("cards.html")


@app.route("/playercards/<int:player>")
def say(player):
    return(str(len(players[player].cards)))

@app.route("/playercard/<int:player>")
def getplayercard(player):
    currentCard = players[player].cards[0]
    result = ""
    result+=(str(currentCard.name)+",")
    result+=(str(currentCard.number)+",")
    result+=(str(currentCard.dpsec)+",")
    result+=(str(currentCard.dpshot)+",")
    result+=(str(currentCard.rate)+",")
    result+=(str(currentCard.mag)+",")
    result+=(str(currentCard.rating)+"")
    return(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')







# while nocards == False:
#     print("Current player is: "+currentplayer.name)
#     if currentplayer == human:
#         print("This is your card:\n")
#         printcard(human.cards[0].number)
#         if drew == False:
#             category = input("What category would you like to use? (1/2/3/4/5)")
#             attribute = attributes[int(category)-1]
#             attributename = attributenames[int(category)-1]
#             print("\nYou used the category " + attributename + ".\n")
#         else:
#             print("\nYou used the same category, " + attributename + ", because you drew last turn.\n")

#     else:
#         print("This is your card:\n")
#         printcard(human.cards[0].number)
#         if drew == False:
#             attribute = attributes[int(random.randrange(0, 4))]
#             attributename = attributenames[int(category) - 1]
#             print("\nThe computer used the category " + attributename + ".\n")
#         else:
#             print("\nThe computer used the same category, " + attributename + ", because you drew last turn.\n")

#     currentplayer = play(attribute, currentplayer)
#     print("Human has " + str(len(human.cards)) + " cards.")
#     print("Computer has " + str(len(computer.cards)) + " cards.\n")
#     if len(human.cards) == 0 or len(computer.cards) == 0:
#         nocards = True


# if len(human.cards) == 0:
#     print("Game over. Computer won.")
# else:
#     print("Game over. Human won.")
