from src.palindromo.dinamica.dinamica import lps, normalizar

def test_palindromo_simple():
    s = "Dabale arroz a la zorra el abad"
    assert lps(normalizar(s)) == "dabalearrozalazorraelabad"
