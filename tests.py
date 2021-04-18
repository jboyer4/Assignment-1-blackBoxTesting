import unittest
from credit_card_validator import credit_card_validator


class TestCC(unittest.TestCase):

    # Should fail with no number
    # Picked using edge case
    def test1(self):
        self.assertFalse(credit_card_validator(''))

    # Check Visa:

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

    # Check Amex:

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

    # Should fail Luhn invalid prefix 34 with 15 digits
    # Picked using edge case
    def test8b(self):
        self.assertFalse(credit_card_validator('345524355673205'))

    # Should pass valid Amex prefix 37
    # Picked using edge case
    def test9(self):
        self.assertTrue(credit_card_validator('375313925744609'))

    # Should fail Luhn valid prefix 34 with 16 digits
    # Picked using Category Partition Testing / common error
    def test10(self):
        self.assertFalse(credit_card_validator('3753139257446426'))

    # Should fail Luhn valid prefix 34 with 14 digits
    # Picked using edge case
    def test11(self):
        self.assertFalse(credit_card_validator('37531392574464'))

    # Should fail Luhn invalid prefix 34 with 15 digits
    # Picked using edge case
    def test11b(self):
        self.assertFalse(credit_card_validator('345524355673205'))

    # Check invalid prefixes:

    # Should fail Luhn valid cc number with length 16 and invalid prefix
    # Picked using common error
    def test12(self):
        self.assertFalse(credit_card_validator('8993978879746468'))

    # Should fail Luhn valid cc number with length 15 and invalid prefix
    # Picked using common error
    def test13(self):
        self.assertFalse(credit_card_validator('030851177275070'))

    # Check MasterCard:

    # Should pass valid MasterCard lower bound 51
    # Picked using edge case
    def test14(self):
        self.assertTrue(credit_card_validator('5193662224770241'))

    # Should pass valid MasterCard upper bound 55
    # Picked using edge case
    def test15(self):
        self.assertTrue(credit_card_validator('5593083929907796'))

    # Should fail Luhn valid MC number in 51-55 when length is 15
    # Picked using Category Partition Testing
    def test16(self):
        self.assertFalse(credit_card_validator('519366222477027'))

    # Should fail Luhn valid MC number in 51-55 when length is 17
    # Picked using Category Partition Testing
    def test17(self):
        self.assertFalse(credit_card_validator('51936622247702718'))

    # Should fail Luhn invalid MC number in 51-55 when length is 16
    # Picked using Category Partition Testing
    def test17a(self):
        self.assertFalse(credit_card_validator('5372899445328342'))

    # Should pass valid MasterCard lower bound 51
    # Picked using edge case
    def test18(self):
        self.assertTrue(credit_card_validator('5193662224770241'))

    # Should pass valid MasterCard lower bound 2221
    # Picked using Category Partition Testing
    def test19(self):
        self.assertTrue(credit_card_validator('2221012312306560'))

    # Should fail valid MasterCard below lower bound 2220
    # Picked using edge case
    def test20(self):
        self.assertFalse(credit_card_validator('2220012312306561'))

    # Should pass valid MasterCard upper bound 2720
    # Picked using Category Partition Testing
    def test21(self):
        self.assertTrue(credit_card_validator('2720012312306566'))

    # Should fail valid MasterCard above upper bound 2721
    # Picked using edge case
    def test22(self):
        self.assertFalse(credit_card_validator('2721012312306565'))

    # Check lengths
    # Check invalid Luhn
    # Check fail boundaries on other ccs


if __name__ == '__main__':
    unittest.main()
