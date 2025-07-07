import unittest
def factorielle(n):
    """
    Calcule la factorielle d'un nombre entier positif n.
    
    Args:
    n (int): Nombre entier positif.
    
    Returns:
    int: Factorielle de n.
    Returns:
        int: Factorielle de n.

    Raises:
        TypeError: Si n n'est pas un entier.
        ValueError: Si n est négatif.
    """ 
    if not isinstance(n, int):
        raise TypeError("n doit être un entier")
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
# Classe de test
class TestFactorielle(unittest.TestCase):

    def test_valeurs_correctes(self):
        self.assertEqual(factorielle(0), 1) # 0! = 1 par convention
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(3), 6)     # 3! = 3×2×1
        self.assertEqual(factorielle(5), 120)   # 5! = 5×4×3×2×1

    def test_valeur_negative(self):
        with self.assertRaises(ValueError):
            factorielle(-1)

    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            factorielle("3")
        with self.assertRaises(TypeError):
            factorielle(2.5)
        with self.assertRaises(TypeError):
            factorielle(None)

# Exécution du test
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFactorielle)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
