class randomNumbersGenerator:
    def __init__(self, m, a, c, x0):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def generateIntNumber(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x


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


    with open(filename, 'w') as file:
        file.write('----Results----\n')
        file.write(f'm = {m}, a = {a}, c = {c}, x0 = {x0}\n')
        file.write(f'Number of generated integers: {numbersToGenerate}\n')
        for i in range(numbersToGenerate):
            generatedNumber = random.generateIntNumber()

            resultTemp = f'X_{i} = {generatedNumber}'

            print(resultTemp)

            file.write(resultTemp + '\n')

main()


