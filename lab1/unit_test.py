import unittest
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

if __name__ == '__main__':
    unittest.main()