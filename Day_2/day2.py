file = open("input.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

limits = {"red" : 12 , "green" : 13 , "blue" : 14}

sum = 0
id = 0
for line in lines:
    line = line.replace(':' , ';')
    line = line.split(';')
    possible = True
    for game in line:
        if "Game" in game:
            game = game.split(' ')
            id = int(game[1])
        else:
            game = game.replace(',' , '')
            game = game.split(' ')
            for i in range(1 , len(game) , 2):
                if int(game[i]) > limits[game[i+1]]:
                    possible = False
    if (possible):
        sum += id
print(sum)