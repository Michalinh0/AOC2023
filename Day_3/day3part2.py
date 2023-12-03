file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

numbers = []
symbols = []

class Number:
    def __init__(self , x, y, number):
        self.x = x
        self.y = []
        self.y.append(y)
        self.number = number
        self.adjacent_to_symbol = False
    
    def add_number(self , y , number):
        self.number = self.number * 10 + number
        self.y.append(y)

    def print_number(self):
        return self.number
    
    def cords(self):
        return (self.x , self.y)
    
    def adjacent(self):
        self.adjacent_to_symbol = True

    def adjacency_check(self):
        return self.adjacent_to_symbol


class Symbol:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.char = char

    def cords(self):
        return (self.x , self.y)
    
    def symbol(self):
        return self.char

x = 0
y = 0
for line in lines:
    x+=1
    y=0
    current = None
    for char in line:
        y+=1
        if(char == '.'):
            if not current == None:
                numbers.append(current)
                current = None
            current = None
        elif(char.isdigit()):
            if(current == None):
                current = Number(x , y , int(char))
            else:
                current.add_number(y , int(char))
        else:
            if not current == None:
                numbers.append(current)
                current = None
            symbols.append(Symbol(x, y))
    if not current == None:
        numbers.append(current)
        current = None

sum = 0

for symbol in symbols:
    cords = symbol.cords()
    number_adjacent = []
    number_vals = []
    for number in numbers:
        if abs(cords[0] - number.cords()[0]) <= 1:
            for y in number.cords()[1]:
                if abs(cords[1] - y) <= 1:
                    number_adjacent.append(number)
                    break
    if len(number_adjacent) == 2:
        sum += number_adjacent[0].print_number() * number_adjacent[1].print_number()

print(sum)