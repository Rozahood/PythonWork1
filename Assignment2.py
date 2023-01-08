maximum = 1
count = 0
minimum = 0
second_maximum = 1
while count < 5:
    num = int(input('Please enter a number: '))
    if num > maximum:
        temporary = maximum
        maximum = num
    second_maximum = temporary

    if num < minimum:
        minimum = num

    count += 1
print('maximum number is ', maximum)
print('second maximum number is ', second_maximum)
print('minimum number is ', minimum)
