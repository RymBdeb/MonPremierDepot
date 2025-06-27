def addition(a, b):
    return a + b


# TDD : développement dirigé par les tests
# Écrivez une méthode de test pour la fonction
def test_addition():
    # Appeler la fonction à tester
    result = addition(3, 5)
    # Assertion pour vérifier si le résultat est celui attendu
    assert result == 8, f"Le résultat attendu est 8, mais le résultat obtenu est {result}"

    result = addition(3, 9)
    assert result == 12, f"Le résultat attendu est 12, mais le résultat obtenu est {result}"


# Créez une suite de tests et exécutez-les
test_addition()
print("Test terminé ...")
