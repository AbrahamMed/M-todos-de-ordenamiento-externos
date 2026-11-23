# Ejercicio 3: Ordenamiento de puntajes de evaluación - Mezcla equilibrada

def leer_lista(ruta):
  with open(ruta, "r") as archivo:
    return [int(linea.strip()) for linea in archivo if linea.strip()]


def extraer_corridas(ruta):
  datos = leer_lista(ruta)
  if not datos:
    return []

  corridas = []
  corrida_actual = [datos[0]]
  # Agrupar elementos mientras mantengan orden ascendente
  for numero in datos[1:]:
    if numero >= corrida_actual[-1]:
      corrida_actual.append(numero)
    else:
      corridas.append(corrida_actual)
      corrida_actual = [numero]
  corridas.append(corrida_actual)
  return corridas


def escribir_corridas(ruta, lista_corridas):
  with open(ruta, "w") as archivo:
    for corrida in lista_corridas:
      for numero in corrida:
        archivo.write(f"{numero}\n")


def fusionar_dos_corridas(corrida_a, corrida_b):
  resultado = []
  i, j = 0, 0
  while i < len(corrida_a) and j < len(corrida_b):
    print(f"   Comparando {corrida_a[i]} con {corrida_b[j]}")
    if corrida_a[i] <= corrida_b[j]:
      print(f"      -> Seleccionado {corrida_a[i]}")
      resultado.append(corrida_a[i])
      i += 1
    else:
      print(f"      -> Seleccionado {corrida_b[j]}")
      resultado.append(corrida_b[j])
      j += 1

  resultado.extend(corrida_a[i:])
  resultado.extend(corrida_b[j:])
  return resultado


def mezcla_equilibrada(ruta_original):
  corridas_iniciales = extraer_corridas(ruta_original)
  print(f"\n[Paso a paso Mezcla Equilibrada] Corridas naturales: {corridas_iniciales}")

  # Distribución inicial en dos archivos auxiliares
  f1_corridas = [c for idx, c in enumerate(corridas_iniciales) if idx % 2 == 0]
  f2_corridas = [c for idx, c in enumerate(corridas_iniciales) if idx % 2 != 0]
  escribir_corridas("f1.txt", f1_corridas)
  escribir_corridas("f2.txt", f2_corridas)

  origenes = ("f1.txt", "f2.txt")
  destinos = ("f3.txt", "f4.txt")
  pasada = 1

  while len(leer_lista(origenes[1])) > 0:
    print(f"\n-> Pasada {pasada}: leyendo de {origenes[0]} y {origenes[1]}")
    corridas_1 = extraer_corridas(origenes[0])
    corridas_2 = extraer_corridas(origenes[1])
    print(f"   Corridas en {origenes[0]}: {corridas_1}")
    print(f"   Corridas en {origenes[1]}: {corridas_2}")

    salida_1, salida_2 = [], []
    total_pares = max(len(corridas_1), len(corridas_2))

    for indice in range(total_pares):
      if indice < len(corridas_1) and indice < len(corridas_2):
        mezclada = fusionar_dos_corridas(corridas_1[indice], corridas_2[indice])
      elif indice < len(corridas_1):
        mezclada = corridas_1[indice]
      else:
        mezclada = corridas_2[indice]

      if indice % 2 == 0:
        salida_1.append(mezclada)
      else:
        salida_2.append(mezclada)

    escribir_corridas(destinos[0], salida_1)
    escribir_corridas(destinos[1], salida_2)
    print(f"   Guardado en {destinos[0]}: {salida_1}")
    print(f"   Guardado en {destinos[1]}: {salida_2}")

    # Intercambiar archivos de lectura y escritura
    origenes, destinos = destinos, origenes
    pasada += 1

  resultado_final = leer_lista(origenes[0])
  escribir_corridas(ruta_original, [resultado_final])


if __name__ == "__main__":
  puntajes = [70, 85, 62, 78, 91, 55, 68, 80, 74]
  with open("puntajes.txt", "w") as archivo:
    for puntaje in puntajes:
      archivo.write(f"{puntaje}\n")

  mezcla_equilibrada("puntajes.txt")
  print(f"\n=== Resultado Final ===\n{leer_lista('puntajes.txt')}")