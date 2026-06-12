"""
Modulo de logica de ABM (Alta, Baja, Modificacion), busqueda y filtros.
"""

from interfaz import mostrar_tabla_paises


# ============================================================================
# FUNCIONES DE GESTIÓN DE DATOS (AGREGAR, ACTUALIZAR, BUSCAR)
# ============================================================================


def validar_numero_positivo(mensaje, es_entero=True):
    """
    Solicita y valida un número positivo del usuario.

    Args:
        mensaje (str): Mensaje a mostrar al usuario
        es_entero (bool): Si True, valida entero; si False, acepta decimales

    Returns:
        int/float: Número válido, o None si el usuario cancela
    """
    mientras_intenta = True

    while mientras_intenta:
        try:
            entrada = input(mensaje).strip()

            if entrada == "":
                print("El campo no puede estar vacio.")
                continue

            if es_entero:
                numero = int(entrada)
            else:
                numero = float(entrada)

            if numero <= 0:
                print("El numero debe ser positivo.")
                continue

            mientras_intenta = False
            return numero

        except ValueError:
            print("Ingrese un numero valido.")
    return None


def agregar_pais(lista_paises):
    """
    Permite al usuario ingresar un nuevo país a la lista.

    Valida campos y verifica que no haya duplicados.

    Args:
        lista_paises (list): Lista de diccionarios con datos de países

    Returns:
        list: Lista actualizada con el nuevo país, o sin cambios si hay error
    """
    print("\n" + "=" * 60)
    print("AGREGAR NUEVO PAIS")
    print("=" * 60)

    # Obtener nombre del país
    mientras_intenta = True
    nombre_pais = ""

    while mientras_intenta:
        nombre_pais = input("Nombre del país: ").strip()

        if nombre_pais == "":
            print("❌ El nombre no puede estar vacío.")
            continue

        # Verificar duplicados
        pais_existe = False
        for pais in lista_paises:
            if pais["nombre"].lower() == nombre_pais.lower():
                pais_existe = True
                break

        if pais_existe:
            print(f"❌ El país '{nombre_pais}' ya existe en la lista.")
            continue

        mientras_intenta = False

    # Obtener población
    poblacion_pais = validar_numero_positivo("Población: ", es_entero=True)
    if poblacion_pais is None:
        print("❌ Operación cancelada.")
        return lista_paises

    # Obtener superficie
    superficie_pais = validar_numero_positivo("Superficie (km²): ", es_entero=True)
    if superficie_pais is None:
        print("❌ Operación cancelada.")
        return lista_paises

    # Obtener continente
    mientras_intenta = True
    continente_pais = ""

    while mientras_intenta:
        continente_pais = input("Continente: ").strip()

        if continente_pais == "":
            print("❌ El continente no puede estar vacío.")
            continue

        mientras_intenta = False

    # Agregar nuevo país
    nuevo_pais = {
        "nombre": nombre_pais,
        "poblacion": poblacion_pais,
        "superficie": superficie_pais,
        "continente": continente_pais,
    }

    lista_paises.append(nuevo_pais)
    print(f"✓ País '{nombre_pais}' agregado exitosamente.")

    return lista_paises


def actualizar_pais(lista_paises):
    """
    Permite al usuario modificar población y superficie de un país.

    Args:
        lista_paises (list): Lista de diccionarios con datos de países

    Returns:
        list: Lista actualizada, o sin cambios si hay error
    """
    if not lista_paises:
        print("No hay paises para actualizar.")
        return lista_paises

    print("\n" + "=" * 60)
    print("ACTUALIZAR PAIS")
    print("=" * 60)

    # Se busca el pais
    nombre_busqueda = input("Nombre del pais a actualizar: ").strip()

    indice_encontrado = -1
    for indice in range(len(lista_paises)):
        if lista_paises[indice]["nombre"].lower() == nombre_busqueda.lower():
            indice_encontrado = indice
            break

    if indice_encontrado == -1:
        print(f"País '{nombre_busqueda}' no encontrado.")
        return lista_paises

    pais_actual = lista_paises[indice_encontrado]

    print(f"\nDatos actuales de {pais_actual['nombre']}:")
    print(f"  - Población: {pais_actual['poblacion']:,}")
    print(f"  - Superficie: {pais_actual['superficie']:,} km²")

    # Actualizar población
    print("\nIngrese los nuevos valores (deje vacío para no cambiar):")
    entrada_poblacion = input("Nueva población: ").strip()

    if entrada_poblacion != "":
        try:
            nueva_poblacion = int(entrada_poblacion)
            if nueva_poblacion <= 0:
                print("La población debe ser positiva.")
                return lista_paises
            lista_paises[indice_encontrado]["poblacion"] = nueva_poblacion
        except ValueError:
            print("Población inválida.")
            return lista_paises

    # Actualizar superficie
    entrada_superficie = input("Nueva superficie (km²): ").strip()

    if entrada_superficie != "":
        try:
            nueva_superficie = int(entrada_superficie)
            if nueva_superficie <= 0:
                print("La superficie debe ser positiva.")
                return lista_paises
            lista_paises[indice_encontrado]["superficie"] = nueva_superficie
        except ValueError:
            print("Superficie inválida.")
            return lista_paises

    print(f"País '{pais_actual['nombre']}' actualizado exitosamente.")
    return lista_paises


def buscar_pais(lista_paises):
    """
    Busca un país por nombre (exacta o parcial, sin importar mayúsculas).

    Args:
        lista_paises (list): Lista de diccionarios con datos de países
    """
    if not lista_paises:
        print("❌ No hay países para buscar.")
        return

    print("\n" + "=" * 60)
    print("BUSCAR PAÍS")
    print("=" * 60)

    nombre_busqueda = input("Ingrese el nombre (o parte del nombre): ").strip().lower()

    if nombre_busqueda == "":
        print("❌ Debe ingresar un nombre.")
        return

    resultados = []

    # Buscar coincidencias
    for pais in lista_paises:
        if nombre_busqueda in pais["nombre"].lower():
            resultados.append(pais)

    if not resultados:
        print(f"❌ No se encontraron países que coincidan con '{nombre_busqueda}'.")
        return

    print(f"\n✓ Se encontraron {len(resultados)} resultado(s):\n")
    mostrar_tabla_paises(resultados, "RESULTADOS DE BÚSQUEDA")


def filtrar_paises(lista_paises):
    """
    Submenú para filtrar países por continente, población o superficie.

    Args:
        lista_paises (list): Lista de diccionarios con datos de países
    """
    if not lista_paises:
        print("No hay paises para filtrar.")
        return

    opciones_validas = True

    while opciones_validas:
        print("\n" + "=" * 60)
        print("FILTRAR PAISES")
        print("=" * 60)
        print("\n1. Filtrar por continente")
        print("2. Filtrar por rango de poblacion")
        print("3. Filtrar por rango de superficie")
        print("4. Volver al menu principal")

        opcion_filtro = input("\nSeleccione una opcion (1-4): ").strip()

        if opcion_filtro == "1":
            # Se obtienen continentes unicos
            continentes = []
            for pais in lista_paises:
                if pais["continente"] not in continentes:
                    continentes.append(pais["continente"])

            continentes.sort()

            print("\nContinentes disponibles:")
            for i, continente in enumerate(continentes, 1):
                print(f"  {i}. {continente}")

            seleccion = input("Seleccione continente (número): ").strip()

            try:
                indice_continente = int(seleccion) - 1
                if 0 <= indice_continente < len(continentes):
                    continente_elegido = continentes[indice_continente]

                    # Filtrar países del continente
                    paises_filtrados = []
                    for pais in lista_paises:
                        if pais["continente"] == continente_elegido:
                            paises_filtrados.append(pais)

                    mostrar_tabla_paises(
                        paises_filtrados, f"PAÍSES DE {continente_elegido.upper()}"
                    )
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingrese un número válido.")

        elif opcion_filtro == "2":
            print("\nFiltrar por rango de población:")

            poblacion_min = validar_numero_positivo(
                "Población mínima: ", es_entero=True
            )
            if poblacion_min is None:
                continue

            poblacion_max = validar_numero_positivo(
                "Población máxima: ", es_entero=True
            )
            if poblacion_max is None:
                continue

            if poblacion_min > poblacion_max:
                print("La población mínima no puede ser mayor que la máxima.")
                continue

            # Filtrar países por rango
            paises_filtrados = []
            for pais in lista_paises:
                if poblacion_min <= pais["poblacion"] <= poblacion_max:
                    paises_filtrados.append(pais)

            if paises_filtrados:
                mostrar_tabla_paises(
                    paises_filtrados,
                    f"PAÍSES CON POBLACIÓN ENTRE {poblacion_min:,} Y {poblacion_max:,}",
                )
            else:
                print(
                    f"No hay países con población entre {poblacion_min:,} y {poblacion_max:,}."
                )

        elif opcion_filtro == "3":
            print("\nFiltrar por rango de superficie:")

            superficie_min = validar_numero_positivo(
                "Superficie mínima (km²): ", es_entero=True
            )
            if superficie_min is None:
                continue

            superficie_max = validar_numero_positivo(
                "Superficie máxima (km²): ", es_entero=True
            )
            if superficie_max is None:
                continue

            if superficie_min > superficie_max:
                print("La superficie mínima no puede ser mayor que la máxima.")
                continue

            # Filtrar países por rango
            paises_filtrados = []
            for pais in lista_paises:
                if superficie_min <= pais["superficie"] <= superficie_max:
                    paises_filtrados.append(pais)

            if paises_filtrados:
                mostrar_tabla_paises(
                    paises_filtrados,
                    f"PAÍSES CON SUPERFICIE ENTRE {superficie_min:,} Y {superficie_max:,} km²",
                )
            else:
                print(
                    f"No hay países con superficie entre {superficie_min:,} y {superficie_max:,} km²."
                )

        elif opcion_filtro == "4":
            opciones_validas = False
        else:
            print("Opción inválida. Intente nuevamente.")
