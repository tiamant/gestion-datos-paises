"""
Modulo de funciones netamente visuales para la consola.
"""

from analisis import (
    calcular_poblacion_promedio,
    calcular_superficie_promedio,
    calcular_poblacion_por_continente,
    contar_paises_por_continente,
    obtener_densidad_maxima,
    obtener_pais_mayor_poblacion,
    obtener_pais_mayor_superficie,
    obtener_pais_menor_poblacion,
)


# ============================================================================
# FUNCIONES DE PRESENTACIÓN DE RESULTADOS
# ============================================================================


def mostrar_tabla_paises(lista_paises, titulo="Tabla de Países"):
    """
    Muestra una tabla formateada con datos de países.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises
        titulo (str): Título de la tabla
    """
    if not lista_paises:
        print("No hay datos para mostrar.")
        return

    print(f"\n{'=' * 100}")
    print(f"{titulo:^100}")
    print(f"{'=' * 100}")
    print(
        f"{'País':<15} {'Población':>15} {'Superficie (km²)':>20} {'Continente':<15} {'Densidad (hab/km²)':>15}"
    )
    print(f"{'-' * 100}")

    for pais in lista_paises:
        densidad = pais["poblacion"] / pais["superficie"]
        print(
            f"{pais['nombre']:<15} "
            f"{pais['poblacion']:>15,} "
            f"{pais['superficie']:>20,} "
            f"{pais['continente']:<15} "
            f"{densidad:>15.2f}"
        )

    print(f"{'=' * 100}\n")


def mostrar_estadisticas_completas(lista_paises):
    """
    Muestra estadísticas completas de los países.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises
    """
    if not lista_paises:
        print("No hay datos disponibles para mostrar estadísticas.")
        return

    print("\n" + "=" * 80)
    print("ESTADÍSTICAS GENERALES")
    print("=" * 80)

    # Calcular estadísticas básicas
    cantidad_paises = len(lista_paises)
    poblacion_total = sum(pais["poblacion"] for pais in lista_paises)
    superficie_total = sum(pais["superficie"] for pais in lista_paises)
    poblacion_promedio = calcular_poblacion_promedio(lista_paises)
    superficie_promedio = calcular_superficie_promedio(lista_paises)

    print(f"\nDATOS GENERALES:")
    print(f"   - Cantidad de países: {cantidad_paises}")
    print(f"   - Población total: {poblacion_total:,} habitantes")
    print(f"   - Superficie total: {superficie_total:,} km²")
    print(f"   - Población promedio: {poblacion_promedio:,.0f} habitantes")
    print(f"   - Superficie promedio: {superficie_promedio:,.0f} km²")

    # País con mayor y menor población
    pais_max_poblacion = obtener_pais_mayor_poblacion(lista_paises)
    pais_min_poblacion = obtener_pais_menor_poblacion(lista_paises)

    print(f"\nINFORMACIÓN POBLACIONAL:")
    print(
        f"   - Mayor población: {pais_max_poblacion['nombre']} ({pais_max_poblacion['poblacion']:,})"
    )
    print(
        f"   - Menor población: {pais_min_poblacion['nombre']} ({pais_min_poblacion['poblacion']:,})"
    )

    # País con mayor superficie
    pais_mayor_superficie = obtener_pais_mayor_superficie(lista_paises)
    print(f"\nINFORMACIÓN DE SUPERFICIE:")
    print(
        f"   - Mayor superficie: {pais_mayor_superficie['nombre']} ({pais_mayor_superficie['superficie']:,} km²)"
    )

    # Densidad poblacional
    pais_densidad_max, densidad_max = obtener_densidad_maxima(lista_paises)
    print(f"\nINFORMACIÓN DE DENSIDAD POBLACIONAL:")
    print(
        f"   - Mayor densidad: {pais_densidad_max['nombre']} ({densidad_max:.2f} hab/km²)"
    )

    # Distribución por continente
    conteo_continente = contar_paises_por_continente(lista_paises)
    poblacion_continente = calcular_poblacion_por_continente(lista_paises)

    print(f"\nDISTRIBUCIÓN POR CONTINENTE:")
    for continente in sorted(conteo_continente.keys()):
        cantidad = conteo_continente[continente]
        poblacion = poblacion_continente[continente]
        print(f"   - {continente}: {cantidad} país(es) - {poblacion:,} habitantes")

    print("\n" + "=" * 80 + "\n")
