"""
Modulo de manejo de archivos CSV y validacion/limpieza inicial de datos.
"""

import csv
from pathlib import Path


# ============================================================================
# FUNCIONES DE LECTURA Y VALIDACIÓN
# ============================================================================


def leer_archivo_csv(nombre_archivo):
    """
    Lee un archivo CSV y retorna una lista de diccionarios con los datos.

    Maneja excepciones para archivo no encontrado, formato incorrecto y datos vacíos.

    Args:
        nombre_archivo (str): Ruta del archivo CSV a leer

    Returns:
        list: Lista de diccionarios con los datos, o lista vacía si hay error
    """
    lista_paises = []

    try:
        # Verificar existencia del archivo
        ruta_archivo = Path(nombre_archivo)
        if not ruta_archivo.exists():
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            return lista_paises

        # Leer archivo CSV
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo)

            # Validar encabezados
            if lector_csv.fieldnames is None:
                print("Error: El archivo CSV está vacío o no tiene formato válido.")
                return lista_paises

            # Leer y validar cada fila
            numero_fila = 1
            for fila in lector_csv:
                numero_fila += 1

                if fila is None:
                    print(f"Advertencia: Fila {numero_fila} ignorada (nula)")
                    continue

                # Validar campos requeridos
                campos_requeridos = ["nombre", "poblacion", "superficie", "continente"]
                if not all(campo in fila for campo in campos_requeridos):
                    print(f"Error en fila {numero_fila}: Faltan campos requeridos")
                    return lista_paises

                lista_paises.append(fila)

        print(f"Se cargaron exitosamente {len(lista_paises)} registros.")
        return lista_paises

    except csv.Error as error_csv:
        print(f"Error en formato CSV: {error_csv}")
        return lista_paises
    except Exception as error_general:
        print(f"Error inesperado al leer archivo: {error_general}")
        return lista_paises


def guardar_datos_csv(lista_paises, nombre_archivo):
    """
    Guarda la lista de países en un archivo CSV usando csv.DictWriter.

    Sobrescribe el archivo existente con los datos actualizados.

    Args:
        lista_paises (list): Lista de diccionarios con datos de países
        nombre_archivo (str): Ruta del archivo CSV a guardar

    Returns:
        bool: True si se guardó exitosamente, False si hay error
    """
    try:
        if not lista_paises:
            print("Advertencia: No hay datos para guardar.")
            return False

        # Definir campos del CSV
        campos = ["nombre", "poblacion", "superficie", "continente"]

        # Escribir archivo CSV
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lista_paises)

        print(f"✓ Datos guardados exitosamente en '{nombre_archivo}'.")
        return True

    except IOError as error_io:
        print(f"Error de entrada/salida al guardar archivo: {error_io}")
        return False
    except Exception as error_general:
        print(f"Error inesperado al guardar archivo: {error_general}")
        return False


def validar_datos_completos(lista_paises):
    """
    Valida que todos los registros tengan campos completos.

    Elimina registros incompletos y reporta los descartados.

    Args:
        lista_paises (list): Lista de diccionarios con datos de países

    Returns:
        list: Lista de diccionarios con datos validados
    """
    lista_validada = []
    indices_invalidos = []

    for indice, pais in enumerate(lista_paises):
        # Detectar campos vacíos o nulos
        campos_vacios = [
            campo
            for campo, valor in pais.items()
            if valor is None or str(valor).strip() == ""
        ]

        if campos_vacios:
            indices_invalidos.append(
                (indice, pais.get("nombre", "desconocido"), campos_vacios)
            )
        else:
            lista_validada.append(pais)

    # Reportar registros inválidos encontrados
    if indices_invalidos:
        print(f"\nSe encontraron {len(indices_invalidos)} registro(s) incompleto(s):")
        for indice, nombre, campos in indices_invalidos:
            print(f"   - {nombre}: campos vacíos {campos}")

    print(f"Validacion completada: {len(lista_validada)} registros validos.\n")
    return lista_validada


def convertir_tipos_numericos(lista_paises):
    """
    Convierte campos numéricos (poblacion, superficie) a tipo int.

    Maneja excepciones para valores no numéricos.

    Args:
        lista_paises (list): Lista de diccionarios con datos de paises

    Returns:
        list: Lista con valores numéricos convertidos
    """
    lista_convertida = []

    for pais in lista_paises:
        try:
            pais_convertido = {
                "nombre": pais["nombre"].strip(),
                "poblacion": int(pais["poblacion"]),
                "superficie": int(pais["superficie"]),
                "continente": pais["continente"].strip(),
            }
            lista_convertida.append(pais_convertido)
        except ValueError as error:
            print(
                f"Error al convertir datos de {pais.get('nombre', 'pais desconocido')}: {error}"
            )

    return lista_convertida
