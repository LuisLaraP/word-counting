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

### Primera aproximación

La versión más sencilla de este contador de palabras sencillamente extrae las palabras del texto e imprime sus frecuencias en orden descendente.

Antes de extraer las palabras, se hace un preprocesamiento del texto en el cual se cambia todo a letras minúsculas. Esto es porque una palabra sigue siendo la misma independientemente de si está en minúsculas o no. También se elimina toda la puntuación, para hacer más sencillo el tratamiento.

La salida de esta iteración está almacenada en el archivo `output/1-primera_aprox.txt`.
