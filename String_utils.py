import unittest

def est_palindrome(chaine): # Vérifie si une chaîne est un palindrome.
    chaine = chaine.lower().replace(" ", "")
    return chaine == chaine[::-1]
def inverser_chaine(chaine):# Retourne l’inverse d’une chaîne de caractères
    return chaine[::-1]
def compter_voyelles(chaine):# Compter le nombre de voyelles (a, e, i, o, u, y) dans une chaîne, en ignorant la casse.
    voyelles = "aeiouy"
    return sum(1 for c in chaine.lower() if c in voyelles)

# test_string_utils.py    
class TestStringUtils(unittest.TestCase):

    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("radar"))
        self.assertTrue(est_palindrome("Radar"))  # insensible à la casse
        self.assertFalse(est_palindrome("bonjour"))
        self.assertTrue(est_palindrome("Noon"))
        self.assertTrue(est_palindrome("Laval"))
        self.assertTrue(est_palindrome("Kayak"))
        self.assertFalse(est_palindrome("nuit"))

    def test_inverser_chaine(self):
        self.assertEqual(inverser_chaine("Python"), "nohtyP")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("a"), "a")
        self.assertEqual(inverser_chaine("12345"), "54321")

    def test_compter_voyelles(self):
        self.assertEqual(compter_voyelles("Bonjour"), 3)  # o, u, o
        self.assertEqual(compter_voyelles("PYTHON"), 2)   # y, o
        self.assertEqual(compter_voyelles("xyz"), 1)      # y
        self.assertEqual(compter_voyelles("bcdfg"), 0)

# Exécution des tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringUtils)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)   
    
    