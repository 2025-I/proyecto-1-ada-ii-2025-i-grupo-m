# IMPLEMENTACIÓN

# DINÁMICA

## FIESTA

Para todos los algoritmos, implementamos una función llamada `filechooser`, esto con la finalidad de que se abra un explorador que nos permita escoger un archivo de texto plano que contiene el problema a resolver.

![Descripción de Imagen1](../images/Imagen1.png)
	
Luego, se implementó una función que se encarga de leer la matriz del problema y guardar la información de cada uno, por si tiene padre e hijos:

![Descripción de Imagen2](../images/Imagen2.png)

Después, se implementó una función que se encarga de calcular el puntaje hipotético de cada nodo, dependiendo de si es invitado o no, para asegurarse de elegir la mejor combinación posible de invitados a la fiesta: 

![Descripción de Imagen3](../images/Imagen3.png)

Finalmente, creamos una función “reconstruir” qué escoges los nodos que suman el mayor puntaje, y forma una lista de 0 y 1 que indica que nodos fueron invitados:

![Descripción de Imagen4](../images/Imagen4.png)

### Complejidad

La complejidad de este algoritmo es O(n^2) ya que la función que se encarga de leer la matriz y la función que guarda la información de cada nodo es de O(n^2) y es la más alta de entre todo el código


## PALINDROMO

Para este código se implementa una función que se encarga de limpiar la cadena de texto que recibe, eliminando todos los caracteres que no sean letras y convirtiendo todas las letras a minúsculas:

![Descripción de Imagen5](../images/Imagen5.png)

Luego, implementamos una función que crea una matriz para almacenar cada longitud de cada subsecuencia palindrómica, la matriz por defecto tendrá su diagonal iniciada en  1, ya que un solo carácter se considera un palíndromo:

![Descripción de Imagen6](../images/Imagen6.png)

Luego, se creó un bloque de código que se encarga de calcular cuál de las subsecuencias es la más larga:

![Descripción de Imagen7](../images/Imagen7.png)

Finalmente, se creó otro bloque que se encarga de reconstruir la subsecuencia más larga para poder retornarla como respuesta:

![Descripción de Imagen8](../images/Imagen8.png)

### Complejidad

La complejidad de este algoritmo también es O(n^2), ya que la función que inicializa la matriz y la que se encarga de llenarlo tienen dicha complejidad y es la más alta de todas.

# FUERZA BRUTA

## FIESTA

En este código implementamos un bloque que se encarga de guardar el número de personas, la suma más alta y la mejor combinación de invitados:

![Descripción de Imagen9](../images/Imagen9.png)

Luego, implementamos un for que se encarga de recorrer todas las combinaciones posibles de los invitados, usando una máscara binaria:

![Descripción de Imagen10](../images/Imagen10.png)

Después, creamos un for que se encarga de construir el subconjunto de personas invitadas de acuerdo a la función anterior:

![Descripción de Imagen11](../images/Imagen11.png)

Luego, implementamos un for que se encarga de verificar si hay conflicto, tomando la restricción de padre-hijo, y si encuentra conflicto, descarta el subconjunto:

![Descripción de Imagen12](../images/Imagen12.png)

Por último, creamos un bloque para comparar si el subconjunto actual es el de mayor longitud, para retornarlo como solución:

![Descripción de Imagen13](../images/Imagen13.png)

### Complejidad

En este caso la complejidad de la función que recorre todos los subconjuntos es 2^n y la función que verifica si hay conflictos es n^2, y como ambas se realizan en conjunto entonces la complejidad total es O((2^n)*(n^2))

## PALINDROMO

Este código inicia similar al dinámico, con la normalización de la cadena, Después a esa cadena le aplica una función para encontrar todas las subsecuencias posibles y verifica si es un palíndromo: 

![Descripción de Imagen14](../images/Imagen14.png)

Luego, con un if comparamos si la subsecuencia actual es la más larga para actualizarla o no, y eventualmente se retornará el resultado: 

![Descripción de Imagen15](../images/Imagen15.png)

### Complejidad

La complejidad de este código sería O(n) ya que la verificación de las subcadenas y la comparación para encontrar la más larga es O(n).

