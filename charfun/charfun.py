from typing import Tuple  # Tuple se utiliza para indicar el tipo de retorno de la función: un par de valores (bool y str).
import unicodedata   # unicodedata se usa para normalizar caracteres eliminando diacríticos (tildes, diéresis, etc.).

def esPalindromo(cadena: str) -> Tuple[bool, str]:
    """Verifica si una cadena es un palíndromo considerando solo las letras.
    Tiene que tener mínimo tres letras.
    Ignora espacios, signos de puntuación, símbolos y diacríticos (excepto la 'ñ', que se trata como distinta de 'n').
    Además, no distingue entre mayúsculas y minúsculas.

    Parámetros:
        cadena (str): La cadena de texto que se va a verificar.
    
    Retorna:
        Tuple[bool, str]:
        - El primer valor (bool) indica si la cadena es un palíndromo (True) o no (False).
        - El segundo valor (str) es la versión limpia de la cadena utilizada para la comparación.

    Excepciones:
        TypeError: Si el parámetro no es un string.
        ValueError: Si la cadena está vacía, contiene menos de 3 letras, excede el tamaño máximo
                    o mezcla letras con números.
    
        Ejemplo de Uso:
        >>> esPalindromo("Anita lava la tina")
        (True, 'anitalavalatina')

        >>> esPalindromo("Añita lava la tina")
        (False, 'añitalavalatina')

        >>> esPalindromo("123anita")
        Error: La cadena no puede contener números mezclados con letras.
        
    """
    # Tamaño máximo permitido
    TAMANO_MAXIMO = 100

    # Verifica que el parámetro sea un string
    if not isinstance(cadena, str):
        raise TypeError("El parámetro debe ser un string.")
    
    # Verifica el tamaño de la cadena
    if len(cadena) > TAMANO_MAXIMO:
        raise ValueError(f"La cadena no puede tener más de {TAMANO_MAXIMO} caracteres.")

    # Verifica que la cadena no esté vacía y que contenga letras
    if not cadena.strip() or not any(caracter.isalpha() for caracter in cadena):
        raise ValueError("La cadena debe contener al menos una letra, palabra u oración y no puede estar vacía ni contener solo espacios.")
    
    # Verifica si la cadena contiene números mezclados con letras
    if any(caracter.isdigit() for caracter in cadena) and any(caracter.isalpha() for caracter in cadena):
        raise ValueError("La cadena no puede contener números mezclados con letras.")

    # Normaliza la cadena para eliminar diacríticos de todas las letras excepto la 'ñ'.
    # Convierte caracteres con diacríticos (p.ej., á, é) en sus equivalentes base (a, e).
    # Luego, se eliminan los diacríticos codificando el texto en ASCII.
    cadena_normalizada = ''.join(
        caracter if caracter == 'ñ' else unicodedata.normalize('NFD', caracter).encode('ascii', 'ignore').decode('utf-8')
        for caracter in cadena
    ).lower()

    # Filtrado para tener solo caracteres alfabéticos
    cadena_limpia = ''.join(caracter for caracter in cadena_normalizada if caracter.isalpha())

    # Verifica que la cadena tenga al menos 3 letras
    if len(cadena_limpia) < 3:
        raise ValueError("La cadena debe tener al menos 3 letras.")

    # Invierte la cadena y compara para delimitar si es palindromo o no. Además retorna una tupla con el resultado y la cadena limpia.
    cadena_invertida = cadena_limpia[::-1]
    es_palindromo = cadena_limpia == cadena_invertida
    return es_palindromo, cadena_limpia

if __name__ == "__main__":
    print("=" * 50)
    print("     Palíndromo")
    print("=" * 50)
    print(
        "Este programa permite verificar si una cadena de texto es un palíndromo.\n"
        "- Se consideran únicamente las letras (se ignoran espacios, signos de puntuación y símbolos).\n"
        "- No distingue entre mayúsculas y minúsculas.\n"
        "- Se eliminan tildes y diacríticos, pero la 'ñ' se trata como distinta de la 'n'.\n"
        "- La cadena debe tener al menos 3 letras para ser válida."
    )
    print("=" * 50)
    cadena = input("Introduce una cadena de texto: ")
    try:
        # Recibe el resultado y la cadena limpia
        resultado, cadena_limpia = esPalindromo(cadena)
        if resultado:
            print(f"\nLa cadena introducida es: '{cadena}' y es palíndroma.")
        else:
            print(f"\nLa cadena introducida es: '{cadena}' y no es palíndroma.")
        # Muestra la cadena limpia
        print(f"\nCadena limpia usada para la verificación: '{cadena_limpia}'")
    except (ValueError, TypeError) as e:
        print(f"\nError: {e}")

