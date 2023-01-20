import unittest
from translator import englishToFrench, frenchToEnglish
class TestE2F(unittest.TestCase): 
    def test_e2f_null(self):
        """Test for null input for englishToFrench"""
        self.assertEqual(englishToFrench(""), "") 
    def test_e2f_hello(self): 
        """englishToFrench - assertEqual - Test for the translation of the world ‘Hello’ and ‘Bonjour’."""
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test_e2f_long(self): 
        """Test E2F for ong text"""
        self.assertEqual(englishToFrench("Hello, how are you today?"), "Bonjour, comment vous êtes aujourd'hui?")
    def test_e2f_ne(self): 
        """englishToFrench - assertNotEqual - Test for the translation of the world ‘Hello’ to change."""
        self.assertNotEqual(englishToFrench("Hello"), "Hello")        
class TestF2E(unittest.TestCase): 
    def test_f2e_null(self):
        """Test for null input for frenchToEnglish"""
        self.assertEqual(frenchToEnglish(""), "") 
    def test_f2e_hello(self):
        """frenchToEnglish - assertEqual - Test for the translation of the world ‘Bonjour’ and ‘Hello’."""
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
    def test_f2e_long(self):
        """Test F2E for long text"""
        self.assertEqual(frenchToEnglish("Bonjour, comment vous êtes aujourd'hui?"), "Hello, how are you today?") 
    def test_f2e_ne(self): 
        """frenchToEnglish - assertNotEqual - Test for the translation of the world Bonjour to change."""
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")        
        
if __name__ == '__main__':
    unittest.main()
