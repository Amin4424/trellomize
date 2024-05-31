import unittest
from libs.user import is_valid_email
from libs.user import hash_password_with_salt

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
        self.assertEqual(hash_password_with_salt("amir"),"e39c35e6bd9bd5557015119ed6018ec879cf43da48e3e24e274575491011379f")
    def test_2(self):
        self.assertEqual(hash_password_with_salt("314"),"0c42661778dd4fd5402690aec2d5aac08ffbeea38821e6f34310d93441db12c1")
    def test_3(self):
        self.assertEqual(hash_password_with_salt("amin1234"),"f74f1d5bc74ae513039f5dfb096025d78b8f342c2f789d3f967cc9f79cab8610")
    def test_4(self):
        self.assertNotEqual(hash_password_with_salt("amir"),"1574ad62d48a37f847699d7d2157105a5a5fd6ed323a3497fa41c7731229bf23")
    def test_5(self):
        self.assertNotEqual(hash_password_with_salt("314"),"748064be03a08df81e31bd6f9e7e7c4cc9f84b4401b9a3c6e85b7ff816d3ba68")
    def test_6(self):
        self.assertNotEqual(hash_password_with_salt("amin1234"),"c2ecd48c47ad7469f3c838eb92f17cde5822a500d542831620b615809166c119")

if __name__=='__main__':
	unittest.main()