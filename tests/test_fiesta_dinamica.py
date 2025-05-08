from src.fiesta.dinamica.dinamica import resolver_fiesta

def test_caso_juguete(capsys):
    matriz = [
        [0, 1],
        [0, 0]
    ]
    valores = [10, 20]
    resolver_fiesta(matriz, valores)
    captured = capsys.readouterr()
    assert "1 0 10" in captured.out or "0 1 20" in captured.out
