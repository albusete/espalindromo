import unittest
from charfun.charfun import esPalindromo

class TestPalindromo(unittest.TestCase):
    def test_palindromo_simple(self):
        """Verifica que 'Anita lava la tina' es palíndroma."""
        resultado, _ = esPalindromo("Anita lava la tina")
        self.assertEqual(resultado, True, f"Se esperaba True, pero se obtuvo {resultado}")

    def test_no_palindromo(self):
        """Verifica que 'Esto no es un palíndromo' no es palíndroma."""
        resultado, _ = esPalindromo("Esto no es un palíndromo")
        self.assertEqual(resultado, False, f"Se esperaba False, pero se obtuvo {resultado}.")

    def test_con_ñ(self):
        """Verifica que 'Añita lava la tina' no es palíndroma."""
        resultado, _ = esPalindromo("Añita lava la tina")
        self.assertEqual(resultado, False, f"Se esperaba False, pero se obtuvo {resultado}.")

    def test_con_diacriticos(self):
        """Verifica que 'Ánita lava la tina' es palíndroma."""
        resultado, _ = esPalindromo("Ánita lava la tina")
        self.assertEqual(resultado, True, f"Se esperaba True, pero se obtuvo {resultado}")

    def test_palindromo_con_signos(self):
        """Verifica que '¡Amo la pacífica paloma!' es palíndroma."""
        resultado, _ = esPalindromo("¡Amo la pacífica paloma!")
        self.assertEqual(resultado, True, f"Se esperaba True, pero se obtuvo {resultado}")

    def test_cadena_vacia(self):
        """Verifica que una cadena vacía lanza una excepción."""
        with self.assertRaises(ValueError):
            esPalindromo("")

    def test_cadena_solo_espacios(self):
        """Verifica que una cadena con solo espacios lanza una excepción."""
        with self.assertRaises(ValueError):
            esPalindromo("   ")

    def test_cadena_menor_de_tres_letras(self):
        """Verifica que una cadena con menos de 3 letras lanza una excepción."""
        with self.assertRaises(ValueError):
            esPalindromo("aa")
    
    def test_cadena_excede_tamano_maximo(self):
        """Verifica que una cadena que excede el tamaño máximo lanza una excepción."""
        cadena_larga = "a" * 101  # 101 caracteres
        with self.assertRaises(ValueError):
            esPalindromo(cadena_larga)

    def test_cadena_solo_numeros(self):
        """Verifica que una cadena con solo números lanza una excepción."""
        with self.assertRaises(ValueError):
            esPalindromo("12321")

    def test_cadena_numeros_mezclados(self):
        """Verifica que una cadena con números mezclados con letras lanza una excepción."""
        with self.assertRaises(ValueError):
            esPalindromo("Anita 123 lava la tina")

    def test_parametro_no_string(self):
        """Verifica que pasar un tipo no string lanza una excepción."""
        with self.assertRaises(TypeError):
            esPalindromo(12345)

if __name__ == "__main__":
    unittest.main()