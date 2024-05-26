import unittest
from libs.user import is_valid_email
from libs.user import pass_hash

class ValidationEmail(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_valid_email("amir@gmail.com"))
    def test_2(self):
        self.assertTrue(is_valid_email("amin@hotmail.com"))
    def test_3(self):
        self.assertTrue(is_valid_email("a@mymail.ir"))
    def test_4(self):
        self.assertTrue(is_valid_email("mammad@yahoo.org"))
    def test_5(self):
        self.assertFalse(is_valid_email("amir.org"))
    def test_6(self):
        self.assertFalse(is_valid_email("amir.com"))
    def test_7(self):
        self.assertFalse(is_valid_email("amir@gmail"))
    def test_8(self):
        self.assertFalse(is_valid_email("amir.gmail@com"))
        
class ValidationHash(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pass_hash("amir"),"4a5fae827ed25de0df79967763b7df467f1a11ea9d3d1945b93c0018c3dfb30b")
    def test_2(self):
        self.assertEqual(pass_hash("314"),"21c59ef795708b592004ddbc343784a561e3d5dc56afadddec4308e6160dfe6c")
    def test_3(self):
        self.assertEqual(pass_hash("amin1234"),"340d28ad93b3a3ba53454468e2b1c891255a449e37e5e3a9d9c0205821cd1a85")
    def test_4(self):
        self.assertNotEqual(pass_hash("amir"),"1574ad62d48a37f847699d7d2157105a5a5fd6ed323a3497fa41c7731229bf23")
    def test_5(self):
        self.assertNotEqual(pass_hash("314"),"748064be03a08df81e31bd6f9e7e7c4cc9f84b4401b9a3c6e85b7ff816d3ba68")
    def test_6(self):
        self.assertNotEqual(pass_hash("amin1234"),"c2ecd48c47ad7469f3c838eb92f17cde5822a500d542831620b615809166c119")

if __name__=='__main__':
	unittest.main()