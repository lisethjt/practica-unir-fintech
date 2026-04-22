"""Lee un fichero de palabras, opcionalmente elimina duplicados y las imprime ordenadas.

Uso:
    python3 main.py <filename> <yes|no>

Argumentos:
    filename : ruta al fichero de texto con una palabra por línea.
    yes|no   : "yes" elimina palabras duplicadas; "no" conserva la lista tal cual.

Si el fichero indicado no existe se usa una lista de ejemplo con las casas de Hogwarts.

License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    """Devuelve una nueva lista con los elementos ordenados.

    Args:
        items: lista de elementos comparables entre sí.
        ascending: si es True (por defecto) ordena de menor a mayor;
            si es False, en orden inverso.

    Returns:
        list: nueva lista ordenada. No modifica la original.

    Raises:
        RuntimeError: si `items` no es una lista.
    """
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    """Elimina los elementos duplicados de una lista.

    Nota: el orden original no se preserva, ya que se usa `set` internamente.
    Si se invoca junto con `sort_list` el orden se restablece al ordenar.

    Args:
        items: lista de elementos hasheables.

    Returns:
        list: lista sin duplicados, en orden indeterminado.
    """
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
