file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

def remove_empty(target):
    result = [item for item in target if item != '']
    return result

sum = 0

for line in lines:
    line = line.replace(": ",'|')
    line = line.replace("| " , '|')
    line = line.split('|')
    winning = line[1]
    yours = line[2]
    winning = winning.split(" ")
    yours = yours.split(" ")
    winning = remove_empty(winning)
    yours = remove_empty(yours)
    score = 0.5
    for number in winning:
        print(number , number in yours)
        if number in yours:
            score = score * 2
    if(score != 0.5):
        sum += score

print(sum)

