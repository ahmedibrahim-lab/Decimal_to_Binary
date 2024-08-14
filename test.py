import unittest

from d2b import decimal_to_binary

class TestB2D(unittest.TestCase):
    
    # Test cases for correct results
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary('1'), '1')
        self.assertEqual(decimal_to_binary('2'), '10')
        self.assertEqual(decimal_to_binary('3'), '11')
        self.assertEqual(decimal_to_binary('34'), '100010')
        self.assertEqual(decimal_to_binary('101'), '1100101')
        self.assertEqual(decimal_to_binary('1231'), '10011001111')
        self.assertEqual(decimal_to_binary('15009'), '11101010100001')
        self.assertEqual(decimal_to_binary('964352'), '11101011011100000000')

    # Test cases for invalid inputs
    def test_invalid_input(self):
        
        with self.assertRaises(ValueError):
            decimal_to_binary('abc')    
        with self.assertRaises(ValueError):
            decimal_to_binary('10a1')    
        with self.assertRaises(ValueError):
            decimal_to_binary('')
        
if __name__ == '__main__':
    unittest.main()