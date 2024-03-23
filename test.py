import unittest
import sys

# Hàm cần kiểm tra
def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Định nghĩa lớp kiểm tra
class TestIsPrime(unittest.TestCase):

    def test_negative(self):
        self.assertFalse(is_Prime(-1))
        self.assertFalse(is_Prime(-2))
        self.assertFalse(is_Prime(-10))

    def test_zero_and_one(self):
        self.assertFalse(is_Prime(0))
        self.assertFalse(is_Prime(1))

    def test_small_primes(self):
        self.assertTrue(is_Prime(2))
        self.assertTrue(is_Prime(3))
        self.assertTrue(is_Prime(5))
        self.assertTrue(is_Prime(7))
        self.assertTrue(is_Prime(11))
        self.assertTrue(is_Prime(13))

    def test_non_prime(self):
        self.assertFalse(is_Prime(4))
        self.assertFalse(is_Prime(6))
        self.assertFalse(is_Prime(8))
        self.assertFalse(is_Prime(9))
        self.assertFalse(is_Prime(10))
        self.assertFalse(is_Prime(12))

    def test_large_prime(self):
        self.assertTrue(is_Prime(9999991))
        
    def test_large_non_prime(self):
        self.assertFalse(is_Prime(9999992))

if __name__ == '__main__':
    unittest.main()
