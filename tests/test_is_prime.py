import unittest
import sys
sys.path.append('..')
from leo.core.primes import is_prime

class TestIsPrime(unittest.TestCase):
	''' test for prime '''

	def test_five_is_prime(self):
		self.assertTrue(is_prime(5))
	
	def test_four_is_not_prime(self):
		self.assertFalse(is_prime(4))

if __name__ == '__main__':
	unittest.main()
