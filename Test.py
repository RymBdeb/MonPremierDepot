import unittest

# Fonction à tester
def addition(a, b):
    return a + b 

# Classe de test
class TestAddition(unittest.TestCase):
    def test_addition(self):
        # Assertions pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(7, 8), 15)
        self.assertEqual(addition(9, 3), 12)

# Définition d'un objet test
test_addition = unittest.TestLoader().loadTestsFromTestCase(TestAddition)  # On charge les tests depuis la classe

# Exécution du test
unittest.TextTestRunner().run(test_addition)