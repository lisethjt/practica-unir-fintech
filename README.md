# Práctica UNIR — EIEC / DevOps

Repositorio de prácticas para la asignatura **Entornos de Integración y Entrega Continua (EIEC)** del máster de DevOps de **UNIR**. Sirve como base para ejercitar Git, Docker e integración continua sobre un programa Python mínimo.

## Descripción del programa

[main.py](main.py) es un script que:

1. Lee un fichero de texto con **una palabra por línea**.
2. Opcionalmente elimina las palabras duplicadas.
3. Imprime la lista resultante **ordenada alfabéticamente**.

Si el fichero indicado no existe, el programa avisa por consola y continúa con una lista de ejemplo (`ravenclaw`, `gryffindor`, `slytherin`, `hufflepuff`).

## Requisitos

Elige una de las dos opciones:

- **Python 3.6+** instalado localmente, **o**
- **Docker** (para ejecutar sin instalar Python).

> Los comandos del [Makefile](Makefile) están pensados para Linux y macOS. En Windows pueden requerir adaptación (por ejemplo, usando WSL o una máquina virtual Linux).

## Uso

### Ejecución local

```bash
python3 main.py <filename> <yes|no>
```

Argumentos:

| Argumento  | Descripción                                                        |
|------------|--------------------------------------------------------------------|
| `filename` | Ruta al fichero con la lista de palabras (una por línea).          |
| `yes\|no`  | `yes` para eliminar duplicados, `no` para mantener la lista tal cual. |

Ambos argumentos son **obligatorios**; si no se pasan, el script termina con código de salida `1`.

Ejemplo:

```bash
python3 main.py words.txt yes
```

### Ejecución con Docker (vía Makefile)

Ejecuta el script dentro de un contenedor `python:3.6-slim` sin necesidad de instalar Python:

```bash
make run
```

Equivale a:

```bash
docker run --rm \
  --volume "$(pwd)":/opt/app \
  --env PYTHON_PATH=/opt/app \
  -w /opt/app \
  python:3.6-slim python3 main.py words.txt yes
```

## Estructura del repositorio

```
.
├── main.py      # Script principal: lee, des-duplica y ordena palabras
├── Makefile     # Atajo `make run` para ejecutar en Docker
└── README.md    # Este documento
```

## API del módulo

[main.py](main.py) expone dos funciones reutilizables:

- [`sort_list(items, ascending=True)`](main.py) — devuelve una nueva lista ordenada; lanza `RuntimeError` si `items` no es una lista.
- [`remove_duplicates_from_list(items)`](main.py) — devuelve la lista sin duplicados (sin garantía de orden).

## Licencia

Apache License 2.0.
