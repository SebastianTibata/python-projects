'''
To do list en consola
'''
tareas = []

def agregartarea(tarea,id):
    tareas.append({"id":id,"Tarea": tarea,"Completado":False})
    print(f"Tarea: {tarea} agregada")
    

def eliminartarea(tarea_eliminar,id):
    if tarea_eliminar < id:
        for i, tarea in enumerate(tareas):
            if tarea["id"] == tarea_eliminar:
                print (f'Tarea: {tarea["id"]} {tarea["Tarea"]} eliminada')
                del tareas[i]
        for i, tarea in enumerate(tareas, start=1):
            tarea["id"] = i
    else:
        print("No existe esa tarea")
        
        
def marcarcompletada(tarea_completar,id):
    for tarea in tareas:
        if tarea["id"] == tarea_completar:
            if tarea["Completado"]:
                print("Tarea ya completada")
                break
            tarea["Completado"]= True
            print (f'Tarea: {tarea["id"]} {tarea["Tarea"]} Completada')
    
def verTareas():
    if len(tareas)!=0:
        for tarea in tareas:
            print(f"{tarea["id"]}. {tarea["Tarea"]}, {"Completado" if tarea["Completado"] else "Pendiente"}")
    else:
        print("No tienes tareas :D")
        
        
def main():
    id= 1
    print("--Bienvenido--")
    while True:
        print("#------------------------------------#")
        print("Seleccione una opción en el menú")
        print("1. Agregar una tarea: ")
        print("2. Eliminar una tarea: ")
        print("3. Marcar una completa: ")
        print("4. Ver todas las tareas:")
        print("5. Salir")
        print("#------------------------------------#")
        print("\n")

        try:
            entrada = int(input("Digite la opcion que quiere usar: "))
            if entrada == 1:
                tarea = input ("Digite la tarea que desea agregar: ")
                agregartarea(tarea,id)
                id+=1
            elif entrada == 2:
                verTareas()
                tarea_eliminar = int(input ("Digite el ID de la tarea que desea eliminar: "))
                eliminartarea(tarea_eliminar,id)
            elif entrada == 3:
                tarea_completar = int(input("Digite el ID de la tarea que desea marcar completada: "))
                marcarcompletada(tarea_completar, id)
            elif entrada == 4:
                verTareas()
            elif entrada == 5:
                break
            else:
                print("No marcó una opcion valida \n")
        except ValueError:
            print("Debe digitar un numero")
        

if __name__ == "__main__":
    main()