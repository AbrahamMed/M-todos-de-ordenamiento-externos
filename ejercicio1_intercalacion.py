#Ejercicio 1: Fusión de folios de dos sucursales - intercalación

def leer_siguiente(archivo):
  linea = archivo.readline().strip()
  return int(linea) if linea else None


def intercalacion(ruta_a, ruta_b, ruta_salida):
  print("\n[Paso a paso Intercalación]")
  with (
      open(ruta_a, "r") as archivo_a,
      open(ruta_b, "r") as archivo_b,
      open(ruta_salida, "w") as salida,
  ):
    valor_a = leer_siguiente(archivo_a)
    valor_b = leer_siguiente(archivo_b)

    # Comparar y escribir el menor de ambos archivos
    while valor_a is not None and valor_b is not None:
      print(f"Comparando {valor_a} (Sucursal A) con {valor_b} (Sucursal B)")
      if valor_a <= valor_b:
        print(f"   -> Escribiendo {valor_a} en el archivo final")
        salida.write(f"{valor_a}\n")
        valor_a = leer_siguiente(archivo_a)
      else:
        print(f"   -> Escribiendo {valor_b} en el archivo final")
        salida.write(f"{valor_b}\n")
        valor_b = leer_siguiente(archivo_b)

    # Vaciar datos restantes si un archivo terminó antes
    while valor_a is not None:
      print(f"   -> Copiando restante de Sucursal A: {valor_a}")
      salida.write(f"{valor_a}\n")
      valor_a = leer_siguiente(archivo_a)

    while valor_b is not None:
      print(f"   -> Copiando restante de Sucursal B: {valor_b}")
      salida.write(f"{valor_b}\n")
      valor_b = leer_siguiente(archivo_b)


def crear_archivo(ruta, datos):
  with open(ruta, "w") as archivo:
    for numero in datos:
      archivo.write(f"{numero}\n")


def leer_lista(ruta):
  with open(ruta, "r") as archivo:
    return [int(linea.strip()) for linea in archivo if linea.strip()]


if __name__ == "__main__":
  folios_norte = [102, 115, 130, 148]
  folios_sur = [105, 110, 130, 160, 175]

  crear_archivo("sucursal_norte.txt", folios_norte)
  crear_archivo("sucursal_sur.txt", folios_sur)

  print(f"Sucursal Norte (ordenada): {folios_norte}")
  print(f"Sucursal Sur (ordenada):   {folios_sur}")

  intercalacion("sucursal_norte.txt", "sucursal_sur.txt", "folios_unidos.txt")
  print(f"\n=== Resultado Final ===\n{leer_lista('folios_unidos.txt')}")