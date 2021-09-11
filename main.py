import json
import openingClasses



movesjson = open("data/eco.json").read()

openingList = openingClasses.OpeningList(json.loads(movesjson))

print('Enter a move: ')
halfturn = input()
halfturn = '1. ' + halfturn

print("\n")

opening = openingList.getOpening(halfturn)
possibleOpenings = openingList.getPossibleOpenings(halfturn)

print('\nThis is the "' + opening.name + '" opening.\n\tMost commonly reached by these moves: ' + opening.moves + "\n")

possibleOpenings.sort(key=lambda x: x.moves)

print("\n" + 'From here the possibles openings are:\n')
for opn in possibleOpenings:
    print("\t" + opn.name + ":\n\t\t" + str(opn.moves) + "\n")