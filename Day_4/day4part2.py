file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

def remove_empty(target):
    result = [item for item in target if item != '']
    return result

count = [1] * len(lines)

for i in range (len(lines)):
    lines[i] = lines[i].replace(": ",'|')
    lines[i] = lines[i].replace("| " , '|')
    lines[i] = lines[i].split('|')
    winning = lines[i][1]
    yours = lines[i][2]
    winning = winning.split(" ")
    yours = yours.split(" ")
    winning = remove_empty(winning)
    yours = remove_empty(yours)
    next = 1
    for number in winning:
        if number in yours and i+next < len(lines):
            count[i+next] += count[i]
            next += 1
print (sum(count))