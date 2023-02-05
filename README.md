# Contador de palabras

Este es un analizador de texto sencillo en Python. El objetivo es contar las palabras en un texto para después hacer un análisis del mismo.

## Ejecución

Para ejecutar el contador, se debe pasar el archivo a leer como argumento. El archivo proporcionado se encuentra en el directorio `data`.

    python3 count_words.py data/raw_text.txt

La salida del comando es a través de la salida estándar, la cual puede ser redirigida a un archivo.

### Orden de salida

Por defecto, la salida está ordenada por frecuencia de palabras, de tal manera que las más frecuentes aparecen al inicio. Este comportamiento puede controlarse con la opción `--sort`. El valor de esta opción puede ser 'freq' (por defecto), o 'alpha'. Si se elige 'alpha', la salida estará en orden alfabético.

    python3 count_words.py --sort alpha data/raw_text.txt

## Metodología

Cada etapa del proyecto está marcada por una tag de git. Para ir a una versión específica, se usa el comando siguiente:

    git checkout <nombre_de_tag>

### Primera aproximación

Tag: `v1`

Salidas: `output/1-primera_aprox-alpha.txt`, `output/1-primera_aprox-freq.txt`

La versión más sencilla de este contador de palabras sencillamente extrae las palabras del texto e imprime sus frecuencias en orden descendente.

Antes de extraer las palabras, se hace un preprocesamiento del texto en el cual se cambia todo a letras minúsculas. Esto es porque una palabra sigue siendo la misma independientemente de si está en minúsculas o no. También se elimina toda la puntuación, para hacer más sencillo el tratamiento.

### Stemmer

Tag: `v2`

Salidas: `output/2-stemmer-alpha.txt`, `output/2-stemmer-freq.txt`

En la salida de la primera aproximación se observa que existen varias palabras que significan lo mismo, pero están escritas de diferente manera. Puede ser por las diferencias entre singular y plural (p. ej. `amount` y `amounts`), o bien por diferentes formas verbales (p. ej. `consume` y `consuming`). Ya que estas palabras significan lo mismo, es deseable que se cuenten como una sola entidad. Para ello, es necesario extraer la raíz de la palabra, la cual le da significado.

Para esta tarea se usó el algoritmo de Porter, el cual solamente funciona en inglés. Éste está implementado en la librería `nltk`, diseñada para procesamiento de texto.
