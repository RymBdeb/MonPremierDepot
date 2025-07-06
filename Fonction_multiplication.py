import unittest
#fonction multiplication à tester
def multiplaction(a,b):
    return a * b
# Classe de test
class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiplaction(3, 4), 12)
        self.assertEqual(multiplaction(8, 10), 80)
    def test_negative_numbers(self):
        self.assertEqual(multiplaction(-5, -2), 10)
    def test_positive_and_negative(self):
        self.assertEqual(multiplaction(-3, 6), -18)
        
# Définition d'un objet test
test_positive_numbers = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication) # mettre comme argument le nom de la classe définie pour le test
test_negative_numbers = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication)
test_positive_and_negative = unittest.TestLoader().loadTestsFromTestCase(TestMultiplication)
# Exécution du test
unittest.TextTestRunner().run(test_positive_numbers)
unittest.TextTestRunner().run(test_negative_numbers)
unittest.TextTestRunner().run(test_positive_and_negative)