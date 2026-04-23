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

def remove_duplicates_preserve_order(items):
    seen = set()
    unique_items = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        unique_items.append(item)
    return unique_items
  

def sort_list(items, ascending=True, remove_duplicates=False):
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

    items_to_sort = (
        remove_duplicates_preserve_order(items) if remove_duplicates else items
    )
    return sorted(items_to_sort, reverse=(not ascending))


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
    for arg in sys.argv[1:]:
        if arg.lower() in ("--dedupe", "--remove-duplicates"):
            remove_duplicates = True
        elif filename == DEFAULT_FILENAME:
            filename = arg
        else:
            print(f"Argumento no reconocido: {arg}")
            print("Uso: python main.py [fichero] [--dedupe|--remove-duplicates]")
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

    print(sort_list(word_list, remove_duplicates=remove_duplicates))
