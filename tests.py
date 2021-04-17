import unittest
from credit_card_validator import credit_card_validator


class TestCC(unittest.TestCase):
    # Should fail with no number
    # edge case
    def test1(self):
        self.assertFalse(credit_card_validator(''))

    # Should validate a good visa
    # Category Partition Testing
    def test2(self):
        self.assertTrue(credit_card_validator('4156154215421545'))

    # Should fail Luhn valid visa with 15 digits
    # Picked using Category Partition Testing
    def test3(self):
        self.assertFalse(credit_card_validator('415615421542154'))

    # Should fail Luhn valid visa with 17 digits
    # Picked using Category Partition Testing
    def test4(self):
        self.assertFalse(credit_card_validator('48961021637942063'))

    # Should fail Luhn invalid with 16 digits
    # Picked using Category Partition Testing
    def test5(self):
        self.assertFalse(credit_card_validator('4896102163794206'))


if __name__ == '__main__':
    unittest.main()
