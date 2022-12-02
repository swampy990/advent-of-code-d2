
# Create a function to determine the score
def score(opponent, me):
    if opponent == 'A' and me == 'Z':
        return 3
    elif opponent == 'B' and me == 'X':
        return 1
    elif opponent == 'C' and me == 'Y':
        return 2
    elif opponent == 'A' and me == 'X':
        return 4
    elif opponent == 'B' and me == 'Y':
        return 5
    elif opponent == 'C' and me == 'Z':
        return 6
    elif opponent == 'A' and me == 'Y':
        return 8
    elif opponent == 'B' and me == 'Z':
        return 9
    elif opponent == 'C' and me == 'X':
        return 7
    return False

data = []
for line in open("strat.txt", "r"):
    split = line.strip().split(' ')
    O = split[0]
    M = split[1]

    data.append(score(O, M))

print(sum(data))
