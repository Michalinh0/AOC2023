file = open("input.txt" , 'r')
lines = file.readlines()

first_digit = -1
last_digit = -1
sum = 0

for line in lines:
    first_digit = -1
    last_digit = -1
    for char in line:
        if char.isdigit():
            if first_digit == -1:
                first_digit = int(char)
            last_digit = int(char)
    sum += first_digit *10
    sum += last_digit

print(sum)


            