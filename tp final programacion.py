import json

with open("comidas_rapidas.json", "rt") as archivo:
    comidas = json.load(archivo)

def guardar_datos(comidas):
    with open("comidas_rapidas.json", "wt") as archivo:
        json.dump(comidas, archivo)

def  mostrar_comidas(comidas):
    if comidas == 0:
            print("No hay comidas registradas.")
    else:
        for comida in comidas:
            print("ID:", comida["id"])

            print("Descripción:", comida["descripcion"])
            print("Precio:", comida["precio"])
            print("ingredientes:\n")
            j=0
            for i in (comida["ingredientes"]):
                    print("  ",j,": ",i)
                    j=j+1
            print("\nTiempo de elaboración:", comida["tiempo"])
            print("Calorías:", comida["calorias"])
            if (comida["vegana"]==False):
                print("Vegana:", "no")
            else:
                print("Vegana:","si")


            if "pasos" in comida:
                print("pasos: \n")
                j=0
                for i in (comida["pasos"]):
                    print("  ",j,": ",i)
                    j=j+1

            else:
                print("Lista de pasos: No hay pasos registrados")
            print()
            print("---------------------")

def agregar_comida(comidas):
    nueva_comida = {}
    mayor=0
    for comida in comidas:
            if(comida["id"]>mayor):
                mayor=(comida["id"])
    nueva_comida["id"] = mayor+1
    nueva_comida["descripcion"] = input("Ingrese la descripción: ")
    nueva_comida["precio"] = float(input("Ingrese el precio: "))
    nueva_comida["ingredientes"] = input("Ingrese los ingredientes (separados por coma): ").split(",")
    nueva_comida["tiempo"] = int(input("Ingrese el tiempo de elaboración en minutos: "))
    nueva_comida["calorias"] = int(input("Ingrese las calorías: "))
    nueva_comida["vegana"] = input("¿Es vegana? (Si/No): ").lower() == "si"
    agregarPasos=input("desea agregar lista de pasos? si o no")


    if (agregarPasos=="si"):
            num_pasos = int(input("Ingrese el número de pasos de elaboración: "))
            pasos = []
            for i in range(num_pasos):
                paso = input(f"Ingrese el paso {i+1}: ")
                pasos.append(paso)
                nueva_comida["pasos"] = pasos
    comidas.append(nueva_comida)
    print("Los pasos de elaboración se han agregado correctamente.")
    print("preparacion agregada")

def modificar_comida(comidas):
    id_comida = int(input("Ingrese el ID de la comida a modificar: "))
    encontrado = False
    for comida in comidas:
        if comida["id"] == id_comida:
            comida["descripcion"] = input("Ingrese la nueva descripción: ")
            comida["precio"] = float(input("Ingrese el nuevo precio: "))
            comida["ingredientes"] = input("Ingrese los nuevos ingredientes (separados por coma): ").split(",")
            comida["tiempo"] = int(input("Ingrese el nuevo tiempo de elaboración en minutos: "))
            comida["calorias"] = int(input("Ingrese las nuevas calorías: "))
            comida["vegana"] = input("¿Es vegana? (Si/No): ").lower() == "si"
            agregarPasos=input("desea agregar lista de pasos? si o no")
            if (agregarPasos=="si"):
                num_pasos = int(input("Ingrese el número de pasos de elaboración: "))
                pasos = []
                for i in range(num_pasos):
                 paso = input(f"Ingrese el paso {i+1}: ")
                 pasos.append(paso)
                 comida["pasos"] = pasos
            print("Los pasos de elaboración se han agregado correctamente.")
            print("Comida modificada con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró una comida con ese ID.")

def borrar_comida(comidas):
    id_comida = int(input("Ingrese el ID de la comida a borrar: "))
    encontrado = False
    for comida in comidas:
        if comida["id"] == id_comida:
            comidas.remove(comida)
            print("Comida borrada con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró una comida con ese ID.")

def buscar_por_ingrediente(comidas):
    ingrediente = input("Ingrese el ingrediente a buscar: ")
    resultados = []
    for comida in comidas:
        ingredientes = comida["ingredientes"]
        coincidencia = [i for i in ingredientes if ingrediente in i]
        if coincidencia:
            resultados.append(comida)
    if len(resultados) == 0:
        print("No se encontraron comidas con ese ingrediente.")
    else:
        print("Resultados de búsqueda:")
        mostrar_comidas(resultados)


def buscar_por_precio(comidas):
    precio=int(input("ingrese el precio a buscar: "))
    resultados = []
    for comida in comidas:
        if precio >= comida["precio"]:
            resultados.append(comida)
    if len(resultados) == 0:
        print("No se encontraron precios.")
    else:
        print("Resultados de búsqueda:")
        mostrar_comidas(resultados)

def buscar_por_calorias(comidas):
    caloria=int(input("ingrese las calorias a buscar: "))
    resultados = []
    for comida in comidas:
        if caloria >= comida["calorias"]:
            resultados.append(comida)
    if len(resultados) == 0:
        print("No se encontraron comidas con esas calorias.")
    else:
        print("Resultados de búsqueda:")
        mostrar_comidas(resultados)

def buscar_veganas(comidas):
    veganismo=True
    resultados = []
    for comida in comidas:
        if veganismo==comida["vegana"]:
            resultados.append(comida)
    if len(resultados) == 0:
        print("No se encontraron productos veganos.")
    else:
        print("Resultados de búsqueda:")
        mostrar_comidas(resultados)

while True:
    print("-------- MENÚ DE OPCIONES ---------")
    print("1. Mostrar comidas existentes")
    print("2. Agregar una nueva comida")
    print("3. Modificar los datos de una comida existente")
    print("4. Borrar una comida seleccionada")
    print("5. buscar comida")
    print("0. salir")

    opcion = input("Ingrese la opción deseada:\n ")

    if opcion == "1":
        mostrar_comidas(comidas)
    elif opcion == "2":
        agregar_comida(comidas)
    elif opcion == "3":
        modificar_comida(comidas)
    elif opcion == "4":
        borrar_comida(comidas)
    elif opcion == "5":
        opcion=int(input("ingrese\n1-buscar por ingrediente\n2-buscar por precio\n3-buscar por caloria\n4-mostrar productos veganos"))
        if(opcion==1):
            buscar_por_ingrediente(comidas)
        elif(opcion==2):
            buscar_por_precio(comidas)
        elif(opcion==3):
            buscar_por_calorias(comidas)
        elif(opcion==4):
            buscar_veganas(comidas)
    elif opcion=="0":
        guardar_datos(comidas)
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")