import unittest

# Fonction à tester
def soustraction(a, b):
    return a - b

# Création d'un objet TestCase manuel
def test_soustraction():
    test_case = unittest.TestCase()
    test_case.assertEqual(soustraction(5, 2), 3)
    test_case.assertEqual(soustraction(0, 0), 0)
    test_case.assertEqual(soustraction(-3, -2), -1)
    test_case.assertEqual(soustraction(10, 20), -10)

# Exécution du test
test_soustraction()
print("Tous les tests ont été exécutés avec succès.")