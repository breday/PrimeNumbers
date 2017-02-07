import unittest
from simple import primeNum


class SimpleTestCase(unittest.TestCase):
    """Testing simple.py`."""

    def test_primeNum_seven_prime(self):
        """test if 7 is a prime number"""
        self.assertTrue(primeNum(7))

    def test_primeNum_fiftythree_prime(self):
        """test if 53 is a prime number?"""
        self.assertTrue(primeNum(53))
 
    def test_primeNum_five_prime(self):
        """test if 5 is a prime number?"""
        self.assertTrue(primeNum(5))

    def test_primeNum_two_prime(self):
        """test if 2 is a prime number"""
        self.assertTrue(primeNum(2))

    def test_primeNum_twentyeight_on_prime(self):
        """test if 28 is not a prime number"""
        self.assertFalse(primeNum(28), msg='28 is not prime!')

    def test_primeNum_eight_non_prime(self):
        """test if 8 is not a prime number"""
        self.assertFalse(primeNum(8), msg='Eight is not prime!')

    def test_primeNum_zero_non_prime(self):
        """test if zero is not a prime number"""
        self.assertFalse(primeNum(0), msg='zero is not prime!')

    def test_primeNum_ninety_not_prime(self):
        """test if ninety is not a prime number"""
        self.assertFalse(primeNum(90))

    def test_negative_number(self):
        """test if -tive numbers are not  prime"""
        for index in range(-1, -10, -1):
            self.assertFalse(primeNum(index))

if __name__ == '__main__':
    unittest.main()
