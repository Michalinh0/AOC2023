file = open("input.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

first_digit = -1
last_digit = -1
sum = 0

numbers = {"one" : 1 , "two" : 2 , "three" : 3 , "four" : 4 , "five" : 5 , "six" : 6 , "seven" : 7 , "eight" : 8 , "nine" : 9}

for line in lines:
    first_digit = -1
    last_digit = -1
    str = ""
    for char in line:
        if char.isdigit():
            if first_digit == -1:
                first_digit = int(char)
            last_digit = int(char)
            str = ""
        else:
            str = str + char
            for key in numbers.keys():
                if key in str:
                    print(str)
                    if first_digit == -1:
                        first_digit = numbers[key]
                    last_digit = numbers[key]
                    str = char
    sum += first_digit * 10
    sum += last_digit
    print(line , first_digit , last_digit)

print(sum)