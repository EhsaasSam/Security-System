import unittest
from unittest import result
import pw_generator
import string

class Testing(unittest.TestCase):

    #Test Case 1: Length equal to 4
    def test_gen_password_len_4(self):
        length = 4
        result = pw_generator.generate_password(length)
        self.assertEqual(len(result), length)
    
    #Test Case 2: Length greater than 4
    def test_gen_password_len_gt_4(self):
        length = 999
        result = pw_generator.generate_password(length)
        self.assertEqual(len(result), length)
    
    #Test Case 3: Length less than 4 
    def test_gen_password_len_lt_4(self):
        length = 2
        with self.assertRaises(Exception):
            result = pw_generator.generate_password(length)  
    
    #Test Case 4: Negative length
    def test_gen_password_len_neg(self):
        length=-2
        with self.assertRaises(Exception):
            result=pw_generator.generate_password(length)

    #Test Case 5: Key should not be zero
    def test_enc_key_check(self):
        message="hihi"
        key=0
        with self.assertRaises(Exception):
            result=pw_generator.encrypt(message,key)
    
    #Test Case 6: Key should not be zero
    def test_dec_key_check(self):
        message="hihi"
        key=0
        with self.assertRaises(Exception):
            result=pw_generator.decrypt(message,key)

            

if __name__ == '__main__':
    unittest.main()