import sys
sys.path.append('..')
import unittest
from core.primes import is_prime

class PrimesTestCase(unittest.TestCase):
    ''' Tests for `primes.py`.'''

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        self.assertFalse(is_prime(4), msg='Four is not prime!')

    def test_is_zore_not_prime(self):
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))

if __name__ == '__main__':
    unittest.main()
