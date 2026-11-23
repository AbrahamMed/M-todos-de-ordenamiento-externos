# Ejercicio 2: Ordenamiento de códigos de inventario - Mezcla directa

def leer_siguiente(archivo):
  linea = archivo.readline().strip()
  return int(linea) if linea else None


def leer_lista(ruta):
  with open(ruta, "r") as archivo:
    return [int(linea.strip()) for linea in archivo if linea.strip()]


def particionar(ruta_original, ruta_aux1, ruta_aux2, tamano_bloque):
  with (
      open(ruta_original, "r") as origen,
      open(ruta_aux1, "w") as aux1,
      open(ruta_aux2, "w") as aux2,
  ):
    hacia_primero = True
    contador = 0
    valor = leer_siguiente(origen)

    while valor is not None:
      destino = aux1 if hacia_primero else aux2
      destino.write(f"{valor}\n")
      contador += 1
      if contador == tamano_bloque:
        hacia_primero = not hacia_primero
        contador = 0
      valor = leer_siguiente(origen)


def fusionar(ruta_aux1, ruta_aux2, ruta_original, tamano_bloque):
  with (
      open(ruta_aux1, "r") as aux1,
      open(ruta_aux2, "r") as aux2,
      open(ruta_original, "w") as destino,
  ):
    valor1 = leer_siguiente(aux1)
    valor2 = leer_siguiente(aux2)

    while valor1 is not None or valor2 is not None:
      cont1, cont2 = 0, 0
      # Mezclar un par de bloques ordenadamente
      while (
          valor1 is not None
          and cont1 < tamano_bloque
          and valor2 is not None
          and cont2 < tamano_bloque
      ):
        print(f"   Comparando {valor1} con {valor2}")
        if valor1 <= valor2:
          print(f"      -> Guardando {valor1}")
          destino.write(f"{valor1}\n")
          valor1 = leer_siguiente(aux1)
          cont1 += 1
        else:
          print(f"      -> Guardando {valor2}")
          destino.write(f"{valor2}\n")
          valor2 = leer_siguiente(aux2)
          cont2 += 1

      while valor1 is not None and cont1 < tamano_bloque:
        print(f"      -> Guardando sobrante del bloque 1: {valor1}")
        destino.write(f"{valor1}\n")
        valor1 = leer_siguiente(aux1)
        cont1 += 1

      while valor2 is not None and cont2 < tamano_bloque:
        print(f"      -> Guardando sobrante del bloque 2: {valor2}")
        destino.write(f"{valor2}\n")
        valor2 = leer_siguiente(aux2)
        cont2 += 1


def mezcla_directa(ruta_original):
  total = len(leer_lista(ruta_original))
  tamano_bloque = 1
  pasada = 1

  print(f"\n[Paso a paso Mezcla Directa] Archivo inicial: {leer_lista(ruta_original)}")
  while tamano_bloque < total:
    print(f"\n-> Pasada {pasada} (tamaño de bloque = {tamano_bloque})")
    particionar(ruta_original, "aux1.txt", "aux2.txt", tamano_bloque)
    print(f"   Auxiliar 1: {leer_lista('aux1.txt')}")
    print(f"   Auxiliar 2: {leer_lista('aux2.txt')}")

    fusionar("aux1.txt", "aux2.txt", ruta_original, tamano_bloque)
    print(f"   Estado tras fusión: {leer_lista(ruta_original)}")

    tamano_bloque *= 2
    pasada += 1


if __name__ == "__main__":
  codigos_inventario = [45, 12, 89, 23, 7, 56, 31, 18]
  with open("inventario.txt", "w") as archivo:
    for codigo in codigos_inventario:
      archivo.write(f"{codigo}\n")

  mezcla_directa("inventario.txt")
  print(f"\n=== Resultado Final ===\n{leer_lista('inventario.txt')}")