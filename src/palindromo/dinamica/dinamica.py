from file_chooser import elegir_archivo

def normalizar(s):
    """Elimina caracteres no alfanuméricos y convierte a minúsculas."""
    return ''.join(c.lower() for c in s if c.isalnum())

def lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1] if cl > 2 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Reconstruir la LPS
    i, j = 0, n - 1
    result = []
    while i <= j:
        if s[i] == s[j]:
            result.append(s[i])
            i += 1
            j -= 1
        elif dp[i + 1][j] > dp[i][j - 1]:
            i += 1
        else:
            j -= 1

    palindrome = ''.join(result)
    palindrome += palindrome[:-1][::-1] if dp[0][n - 1] % 2 != 0 else palindrome[::-1]
    return palindrome

def procesar_entrada_palindromo():
    """Procesa el archivo de entrada y muestra las subsecuencias palindrómicas más largas."""
    print("Resultados del problema de palíndromos:")
    archivo = elegir_archivo()
    with open(archivo, 'r', encoding='utf-8') as f:
        n = int(f.readline())  # Número de cadenas a procesar
        for _ in range(n):
            linea = f.readline().strip()
            if linea:
                cadena = normalizar(linea)
                print(lps(cadena))

