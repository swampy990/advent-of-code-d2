
"""
X requires a loss       A=Rock    1 Point       Beaten by Paper
Y requires a draw       B=Paper   2 Point      Beaten by Scissors
Z requires a win        C=Scissors 3 Point      Beaten by Rock

"""
# Create a function to determine the score
def winner(opponent):
    if opponent == 'A': #Paper beats rock
        return 8
    elif opponent == 'B': #Scissors beat paper
        return 9
    elif opponent == 'C': #Rock beats scissors
        return 7


def drawn(opponent):
    if opponent == 'A':
        return 4
    if opponent == 'B':
        return 5
    if opponent == 'C':
        return 6


def loss(opponent):
    if opponent == 'A':
        return 3
    if opponent == 'B':
        return 1
    if opponent == 'C':
        return 2


data = []
for line in open("strat.txt", "r"):
    split = line.strip().split(' ')
    O = split[0]
    M = split[1]

    if M == 'X':
        data.append(loss(O))
    elif M == 'Y':
        data.append(drawn(O))
    elif M == 'Z':
        data.append(winner(O))

print(sum(data))
