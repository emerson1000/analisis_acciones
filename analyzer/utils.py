def save_to_csv(data, filename):
    """
    Guarda un DataFrame en un archivo CSV.
    :param data: DataFrame a guardar.
    :param filename: Nombre del archivo.
    """
    try:
        data.to_csv(filename, index=False)
        print(f"Datos guardados en {filename}")
    except Exception as e:
        print(f"Error guardando el archivo: {e}")