"""
TPI Programacion - Gestion de Datos de Paises
Modulo principal: orquesta el flujo del programa mediante un menu interactivo.
"""

from archivos import (
    leer_archivo_csv,
    guardar_datos_csv,
    validar_datos_completos,
    convertir_tipos_numericos,
)
from analisis import (
    ordenar_por_poblacion,
    ordenar_por_superficie,
    ordenar_alfabeticamente,
    ordenar_por_densidad_poblacional,
)
from operaciones import (
    agregar_pais,
    actualizar_pais,
    buscar_pais,
    filtrar_paises,
)
from interfaz import (
    mostrar_tabla_paises,
    mostrar_estadisticas_completas,
)


# ============================================================================
# FUNCIÓN PRINCIPAL - MENÚ INTERACTIVO
# ============================================================================


def main():
    """
    Función principal con menú interactivo.

    Permite al usuario elegir diferentes opciones hasta salir del programa.
    """
    print("\n" + "=" * 80)
    print("SISTEMA DE ANÁLISIS DE DATOS DE PAÍSES".center(80))
    print("=" * 80 + "\n")

    # Cargar y validar datos iniciales
    print("Cargando datos...")
    lista_paises = leer_archivo_csv("paises.csv")

    if not lista_paises:
        print("No se pudo cargar el archivo. El programa se cerrará.")
        return

    print("Validando datos...")
    lista_paises = validar_datos_completos(lista_paises)

    if not lista_paises:
        print("No hay datos válidos. El programa se cerrará.")
        return

    print("Convirtiendo tipos de datos...")
    lista_paises = convertir_tipos_numericos(lista_paises)
    print(f"{len(lista_paises)} registros cargados exitosamente.\n")

    # Menú interactivo
    programa_activo = True

    while programa_activo:
        print("\n" + "=" * 80)
        print("MENÚ PRINCIPAL")
        print("=" * 80)
        print("\nDATOS Y BÚSQUEDA:")
        print("  1. Ver todos los países")
        print("  2. Agregar nuevo país")
        print("  3. Actualizar país")
        print("  4. Buscar país")
        print("  5. Filtrar países")

        print("\nORDENAMIENTO:")
        print("  6. Ordenar por población")
        print("  7. Ordenar por superficie")
        print("  8. Ordenar alfabéticamente")
        print("  9. Ordenar por densidad poblacional")

        print("\nESTADÍSTICAS:")
        print("  10. Ver estadísticas completas")

        print("\nCONTROL:")
        print("  0. Salir del programa")

        opcion_usuario = input("\nSeleccione una opción (0-10): ").strip()

        # Opción 1: Ver todos los países
        if opcion_usuario == "1":
            mostrar_tabla_paises(lista_paises, "TABLA DE TODOS LOS PAÍSES")

        # Opción 2: Agregar nuevo país
        elif opcion_usuario == "2":
            lista_paises = agregar_pais(lista_paises)
            # Guardar cambios en CSV
            guardar_datos_csv(lista_paises, "paises.csv")

        # Opción 3: Actualizar país
        elif opcion_usuario == "3":
            lista_paises = actualizar_pais(lista_paises)
            # Guardar cambios en CSV
            guardar_datos_csv(lista_paises, "paises.csv")

        # Opción 4: Buscar país
        elif opcion_usuario == "4":
            buscar_pais(lista_paises)

        # Opción 5: Filtrar países
        elif opcion_usuario == "5":
            filtrar_paises(lista_paises)

        # Opción 6: Ordenar por población
        elif opcion_usuario == "6":
            lista_ordenada = ordenar_por_poblacion(lista_paises, descendente=True)
            mostrar_tabla_paises(
                lista_ordenada, "PAÍSES ORDENADOS POR POBLACIÓN (Mayor a Menor)"
            )

        # Opción 7: Ordenar por superficie
        elif opcion_usuario == "7":
            lista_ordenada = ordenar_por_superficie(lista_paises, descendente=True)
            mostrar_tabla_paises(
                lista_ordenada, "PAÍSES ORDENADOS POR SUPERFICIE (Mayor a Menor)"
            )

        # Opción 8: Ordenar alfabéticamente
        elif opcion_usuario == "8":
            lista_ordenada = ordenar_alfabeticamente(lista_paises)
            mostrar_tabla_paises(lista_ordenada, "PAÍSES ORDENADOS ALFABÉTICAMENTE")

        # Opción 9: Ordenar por densidad poblacional
        elif opcion_usuario == "9":
            lista_ordenada = ordenar_por_densidad_poblacional(
                lista_paises, descendente=True
            )
            mostrar_tabla_paises(
                lista_ordenada,
                "PAÍSES ORDENADOS POR DENSIDAD POBLACIONAL (Mayor a Menor)",
            )

        # Opción 10: Estadísticas completas
        elif opcion_usuario == "10":
            mostrar_estadisticas_completas(lista_paises)

        # Opción 0: Salir
        elif opcion_usuario == "0":
            print("\nGracias por usar el Sistema de Análisis de Países.")
            print("¡Hasta luego!\n")
            programa_activo = False

        # Opción inválida
        else:
            print("Opción inválida. Intente nuevamente.")


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()
