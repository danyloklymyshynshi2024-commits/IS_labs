import math
class randomNumbersGenerator:
    def __init__(self, m, a, c, x0):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def generateIntNumber(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

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













def main():
    m = 2**12 - 1
    a = 4**5
    c = 2
    x0 = 8
    filename = 'randomNumbers.txt'

    random = randomNumbersGenerator(m,a,c,x0)

    while True:
        try:
            numbersToGenerate = int(input("How many numbers do you want to generate: "))
            if numbersToGenerate <= 0:
                print('Number must be positive')
                continue
            break
        except ValueError:
            print('Error, enter an integer')

    array = []


    with open(filename, 'w') as file:
        file.write('----Results----\n')
        file.write(f'm = {m}, a = {a}, c = {c}, x0 = {x0}\n')
        file.write(f'Number of generated integers: {numbersToGenerate}\n')
        for i in range(numbersToGenerate):
            generatedNumber = random.generateIntNumber()
            array.append(generatedNumber)
            resultTemp = f'X_{i} = {generatedNumber}'

            print(resultTemp)

            file.write(resultTemp + '\n')

    print(array)


    counter = 0


    for i in range(numbersToGenerate - 1):
        if gcd(array[i], array[i+1]) == 1:
            counter += 1


    print('c: ', counter)
    print('r: ', counter/numbersToGenerate)
    print('r: ', 6/math.pi**2)









main()


