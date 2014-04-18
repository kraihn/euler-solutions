def p1():
    print('If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.')

    multiples = []
    for i in range(1, 1000):
        if i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)

    sum = 0
    for i in range(0, len(multiples)):
        sum += multiples[i]

    print(sum)

def p16():

    num = str(pow(2, 1000))
    sum = 0

    for i in num:
        sum += int(i)

    print(sum)

def p48():

    sum = 0

    for i in range(1, 1001):
        sum += pow(i, i)
        print(i)

    print(str(sum)[(len(str(sum))-10):])
