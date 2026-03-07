import math
import random

class randomNumbersGenerator:
    def __init__(self, m, a, c, x0):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def generateIntNumber(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    
    def findPeriod(self):
        originalX = self.x
        seenValues = set()
        counter = 0
        while True:
            randomNumber = self.generateIntNumber()
            if not randomNumber in seenValues:
                counter += 1
                seenValues.add(randomNumber)
            else:
                break
        self.x = originalX
        return counter


def runTest(randomNumbers):
    counter = 0

    for i in range(len(randomNumbers) - 1):
        if gcd(randomNumbers[i], randomNumbers[i+1]) == 1:
            counter += 1
    numberOfPairs = len(randomNumbers) - 1

    if numberOfPairs == 0:
        return 0

    r = counter/numberOfPairs

    if r == 0:
        return 0

    estimatedPi = math.sqrt(6 / r)

    return f'{estimatedPi:.4f}'


def gcd(a, b):
    if not a > b:
        a, b = b, a
    
    while True:
        r = a % b

        if r > 0:
            a = b
            b = r
            continue
        else:
            break

    return b

def generateNumbers(numbersToGenerate):
    m = 2**12 - 1
    a = 4**5
    c = 2
    x0 = 8
    filename = 'randomNumbers.txt'
    random = randomNumbersGenerator(m,a,c,x0)
    period = random.findPeriod()

    randomValues = []

    with open(f'lab1/{filename}', 'w') as file:
        file.write('----Results----\n')
        file.write(f'm = {m}, a = {a}, c = {c}, x0 = {x0}\n')
        file.write(f'Number of generated integers: {numbersToGenerate}\n')
        for i in range(numbersToGenerate):
            generatedNumber = random.generateIntNumber()
            randomValues.append(generatedNumber)
            resultTemp = f'X_{i+1} = {generatedNumber}'

            file.write(resultTemp + '\n')
        file.write(f'Period: {period}')
    return randomValues


