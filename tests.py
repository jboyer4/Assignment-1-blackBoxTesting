import unittest
from credit_card_validator import credit_card_validator


class TestCC(unittest.TestCase):
    # Should fail with no number
    # Picked using edge case
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

    # Should fail Luhn invalid visa with 16 digits
    # Picked using Category Partition Testing
    def test5(self):
        self.assertFalse(credit_card_validator('4896102163794206'))

    # Should pass valid Amex with prefix 34
    # Picked using edge case
    def test6(self):
        self.assertTrue(credit_card_validator('345524355673206'))

    # Should fail Luhn valid prefix 34 with 16 digits
    # Picked using Category Partition Testing / common error
    def test7(self):
        self.assertFalse(credit_card_validator('3455243556732063'))

    # Should fail Luhn valid prefix 34 with 14 digits
    # Picked using edge case
    def test8(self):
        self.assertFalse(credit_card_validator('34552435567326'))

    # Should pass valid Amex prefix 37
    # Picked using edge case
    def test9(self):
        self.assertTrue(credit_card_validator('375313925744603'))

    # Should fail Luhn valid prefix 34 with 16 digits
    # Picked using Category Partition Testing / common error
    def test10(self):
        self.assertFalse(credit_card_validator('3753139257446426'))

    # Should fail Luhn valid prefix 34 with 14 digits
    # Picked using edge case
    def test11(self):
        self.assertFalse(credit_card_validator('37531392574464'))

if __name__ == '__main__':
    unittest.main()
