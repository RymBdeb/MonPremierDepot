import unittest 
# Fonction à tester : somme des entiers strictement inférieurs à n
def somme_entiers_inferieurs(n):
    if type(n) != int:
        raise TypeError("Le paramètre doit être un entier.")
    if n <= 0:
        return 0
    return sum(range(n))
    
# Classe de test
class TestSommeEntiersInferieurs(unittest.TestCase):
    
    def test_valeurs_positives(self):
        self.assertEqual(somme_entiers_inferieurs(4), 6)   # 0 + 1 + 2 + 3
        self.assertEqual(somme_entiers_inferieurs(1), 0)   # aucun entier < 1
    
    def test_zero_et_negatifs(self):
        self.assertEqual(somme_entiers_inferieurs(0), 0)
        self.assertEqual(somme_entiers_inferieurs(-2), 0)

    def test_grande_valeur(self):
        self.assertEqual(somme_entiers_inferieurs(101), 5050)  # somme de 0

# Définition d'un objet test
test_valeurs_positives = unittest.TestLoader().loadTestsFromTestCase(TestSommeEntiersInferieurs)  # On charge les tests depuis la classe, mettre comme argument le nom de la classe définie pour le test
test_zero_et_negatifs = unittest.TestLoader().loadTestsFromTestCase(TestSommeEntiersInferieurs)
test_grande_valeur = unittest.TestLoader().loadTestsFromTestCase(TestSommeEntiersInferieurs)
# Exécution du test
unittest.TextTestRunner().run(test_valeurs_positives)
unittest.TextTestRunner().run(test_zero_et_negatifs)
unittest.TextTestRunner().run(test_grande_valeur)