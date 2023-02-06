# Contador de palabras

Este es un analizador de texto sencillo en Python. El objetivo es contar las palabras en un texto para después hacer un análisis del mismo.

## Ejecución

Para ejecutar el contador, se debe pasar el archivo a leer como argumento. El texto proporcionado se encuentra en el directorio `data`. Adicionalmente, se puede especificar un archivo de sinónimos con la opción `--syn-file`.

    python3 count_words.py --syn-file synonyms.txt data/raw_text.txt

La salida del comando es a través de la salida estándar, la cual puede ser redirigida a un archivo.

### Orden de salida

Por defecto, la salida está ordenada por frecuencia de palabras, de tal manera que las más frecuentes aparecen al inicio. Este comportamiento puede controlarse con la opción `--sort`. El valor de esta opción puede ser 'freq' (por defecto), o 'alpha'. Si se elige 'alpha', la salida estará en orden alfabético.

    python3 count_words.py --sort alpha data/raw_text.txt

### Reducción de sinónimos

Este script de Python tiene la capacidad de reducir sinónimos en el texto. Para usar esta característica se debe especificar un archivo de sinónimos en la línea de comandos con el argumento `--syn-file`. Si no se especifica ningún archivo, no se realiza la reducción de sinónimos.

En el archivo de sinónimos, cada línea se divide en dos secciones, separadas por un caracter `:`. La primera sección es la cadena que será colocada en el texto cada vez que se encuentre un sinónimo. La segunda sección es una lista separada por comas de cadenas que, cuando se encuentren en el texto, serán reemlazadas por la cadena en la primera sección. Si no se especifica ningún archivo de sinónimos, este paso del procesamiento se omite.

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

### Reducción de sinónimos

Tag: `v3`

Salidas: `output/3-sinonimos-alpha.txt`, `output/3-sinonimos-freq.txt`

En el texto dado existen algunos conceptos que requieren de dos palabras para expresar su significado, por ejemplo "junk food". Si estas palabras se extrajeran por separado se perdería este significado. Para atacar este problema se implementó un sistema para reemplazar palabras por otras. Los patrones a reemplazar se dan en un archivo de texto.

El mecanismo para reemplazar sinónimos también puede servir para otros propósitos. Uno de ellos  es arreglar palabras que estén mal escritas o separar contracciones (`didn't` -> `did not`). En cualquier caso, los contenidos del archivo de sinónimos deben ser definidos manualmente a partir del texto que se esté analizando.
