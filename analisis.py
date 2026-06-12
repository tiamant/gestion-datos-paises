"""
Modulo de funciones de calculo, estadisticas y ordenamiento.
"""


# ============================================================================
# FUNCIONES DE ORDENAMIENTO
# ============================================================================


def ordenar_por_poblacion(lista_paises, descendente=False):
    """
    Ordena los países por población.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises
        descendente (bool): Si True, ordena de mayor a menor

    Returns:
        list: Nueva lista ordenada por población
    """
    lista_ordenada = lista_paises.copy()
    lista_ordenada.sort(key=lambda pais: pais["poblacion"], reverse=descendente)
    return lista_ordenada


def ordenar_por_superficie(lista_paises, descendente=False):
    """
    Ordena los países por superficie.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises
        descendente (bool): Si True, ordena de mayor a menor

    Returns:
        list: Nueva lista ordenada por superficie
    """
    lista_ordenada = lista_paises.copy()
    lista_ordenada.sort(key=lambda pais: pais["superficie"], reverse=descendente)
    return lista_ordenada


def ordenar_alfabeticamente(lista_paises):
    """
    Ordena los países alfabéticamente por nombre.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        list: Nueva lista ordenada alfabéticamente
    """
    lista_ordenada = lista_paises.copy()
    lista_ordenada.sort(key=lambda pais: pais["nombre"].lower())
    return lista_ordenada


def ordenar_por_densidad_poblacional(lista_paises, descendente=True):
    """
    Ordena los países por densidad poblacional (hab/km²).

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises
        descendente (bool): Si True, ordena de mayor a menor densidad

    Returns:
        list: Nueva lista ordenada por densidad poblacional
    """
    lista_ordenada = lista_paises.copy()
    lista_ordenada.sort(
        key=lambda pais: pais["poblacion"] / pais["superficie"], reverse=descendente
    )
    return lista_ordenada


# ============================================================================
# FUNCIONES DE CÁLCULO ESTADÍSTICO
# ============================================================================


def calcular_poblacion_promedio(lista_paises):
    """
    Calcula la población promedio de todos los países.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        float: Población promedio, 0 si la lista está vacía
    """
    if not lista_paises:
        return 0

    suma_poblacion = sum(pais["poblacion"] for pais in lista_paises)
    promedio_poblacion = suma_poblacion / len(lista_paises)
    return promedio_poblacion


def calcular_superficie_promedio(lista_paises):
    """
    Calcula la superficie promedio de todos los países.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        float: Superficie promedio, 0 si la lista está vacía
    """
    if not lista_paises:
        return 0

    suma_superficie = sum(pais["superficie"] for pais in lista_paises)
    promedio_superficie = suma_superficie / len(lista_paises)
    return promedio_superficie


def obtener_pais_mayor_poblacion(lista_paises):
    """
    Retorna el país con mayor población.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        dict: País con mayor población, None si lista está vacía
    """
    if not lista_paises:
        return None

    pais_mayor = max(lista_paises, key=lambda pais: pais["poblacion"])
    return pais_mayor


def obtener_pais_menor_poblacion(lista_paises):
    """
    Retorna el país con menor población.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        dict: País con menor población, None si lista está vacía
    """
    if not lista_paises:
        return None

    pais_menor = min(lista_paises, key=lambda pais: pais["poblacion"])
    return pais_menor


def obtener_pais_mayor_superficie(lista_paises):
    """
    Retorna el país con mayor superficie.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        dict: País con mayor superficie, None si lista está vacía
    """
    if not lista_paises:
        return None

    pais_mayor = max(lista_paises, key=lambda pais: pais["superficie"])
    return pais_mayor


def obtener_densidad_maxima(lista_paises):
    """
    Retorna el país con densidad poblacional máxima (hab/km²).

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        tuple: (país, densidad) o (None, 0) si lista está vacía
    """
    if not lista_paises:
        return None, 0

    pais_densidad_max = max(
        lista_paises, key=lambda pais: pais["poblacion"] / pais["superficie"]
    )
    densidad = pais_densidad_max["poblacion"] / pais_densidad_max["superficie"]
    return pais_densidad_max, densidad


def agrupar_por_continente(lista_paises):
    """
    Agrupa los países por continente.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        dict: Continentes como claves y listas de países como valores
    """
    grupos_continente = {}

    for pais in lista_paises:
        continente = pais["continente"]

        # Crear entrada si no existe
        if continente not in grupos_continente:
            grupos_continente[continente] = []

        grupos_continente[continente].append(pais)

    return grupos_continente


def contar_paises_por_continente(lista_paises):
    """
    Cuenta la cantidad de países por continente.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        dict: Continentes y cantidad de países
    """
    grupos = agrupar_por_continente(lista_paises)
    conteo = {continente: len(paises) for continente, paises in grupos.items()}
    return conteo


def calcular_poblacion_por_continente(lista_paises):
    """
    Calcula la población total por continente.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        dict: Continentes y población total
    """
    grupos = agrupar_por_continente(lista_paises)
    poblacion_total = {
        continente: sum(pais["poblacion"] for pais in paises)
        for continente, paises in grupos.items()
    }
    return poblacion_total
