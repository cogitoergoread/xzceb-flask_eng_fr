import unittest
from translator import englishToFrench, frenchToEnglish
class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(""), "") # Test for null input for englishToFrench
    def test2(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") # Test for the translation of the world ‘Hello’ and ‘Bonjour’.
    def test3(self): 
        self.assertEqual(englishToFrench("Hello, how are you today?"), "Bonjour, comment vous êtes aujourd'hui?")
        
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(""), "") # Test for null input for frenchToEnglish
    def test2(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") # Test for the translation of the world ‘Bonjour’ and ‘Hello’.
    def test3(self): 
        self.assertEqual(frenchToEnglish("Bonjour, comment vous êtes aujourd'hui?"), "Hello, how are you today?") 
        
unittest.main()
