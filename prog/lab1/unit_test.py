import unittest, random
from back_end import generateNumbers, runTest

class TestCryptoLogic(unittest.TestCase):

    def test_generate_numbers_count(self):
        count = 10
        result = generateNumbers(count)
        self.assertEqual(len(result), count)

    def test_generate_numbers_type(self):
        result = generateNumbers(5)
        self.assertIsInstance(result, list)
        for num in result:
            self.assertIsInstance(num, (int, float))

    def test_run_test_pi_range(self):
        numbers = generateNumbers(100)
        pi_val = runTest(numbers)
        self.assertTrue(2.0 <= float(pi_val) <= 4.0, f"Значення Pi ({pi_val}) занадто дивне")


class CompareTwoFunctionsOnEfficiency:
    def test_lemer_algorithm_w_random_library(self):
        numbersLemer = generateNumbers(20000)
        numbersRandom = [random.randint(1, 2**12-1) for _ in range(20000)]

        pi_val_lemer = runTest(numbersLemer)
        pi_val_random = runTest(numbersRandom)

        return pi_val_lemer, pi_val_random



if __name__ == '__main__':

    obj = CompareTwoFunctionsOnEfficiency()
    lemer_results, random_results = obj.test_lemer_algorithm_w_random_library()

    print(f"Approximate pi value by Lemer algorithm: {lemer_results}")
    print(f"Approximate pi value by random algorithm: {random_results}")

    unittest.main()