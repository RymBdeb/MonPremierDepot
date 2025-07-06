import unittest
# Code de la fonction à tester
def puissance(a, b):
    return a ** b
# Classe de test
class TestPuissance(unittest.TestCase):
    def test_entiers(self):
        self.assertEqual(puissance(2, 3), 8)
        self.assertEqual(puissance(5, 0), 1)
        self.assertEqual(puissance(10, 1), 10)
        self.assertEqual(puissance(-2, 3), -8)
        self.assertEqual(puissance(-2, 2), 4)
    def test_floats(self):
        self.assertAlmostEqual(puissance(2.5, 2), 6.25)
        self.assertAlmostEqual(puissance(9, 0.5), 3.0)

# Définition d'un objet test
test_entiers = unittest.TestLoader().loadTestsFromTestCase(TestPuissance)  # On charge les tests depuis la classe, mettre comme argument le nom de la classe définie pour le test
test_floats = unittest.TestLoader().loadTestsFromTestCase(TestPuissance)
# Exécution du test
unittest.TextTestRunner().run(test_entiers)
unittest.TextTestRunner().run(test_floats)