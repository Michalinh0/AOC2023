file = open("input.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

minimum = {"red" : 0 , "green" : 0 , "blue" : 0}

sum = 0
for line in lines:
    line = line.replace(':' , ';')
    line = line.split(';')
    minimum = {"red" : 0 , "green" : 0 , "blue" : 0}
    for game in line:
        if "Game" in game:
            game = game.split(' ')
            id = int(game[1])
        else:
            game = game.replace(',' , '')
            game = game.split(' ')
            for i in range(1 , len(game) , 2):
                if int(game[i]) > minimum[game[i+1]]:
                    minimum[game[i+1]] = int(game[i])
    sum += minimum["red"] * minimum["green"] * minimum["blue"]
print(sum)