#Crear un proyecto  que permita  gestionar (administrar calificaciones); colocar  un menu  de opciones para agregar, borrar,  modificar, consultar, buscar y vaciar calificaciones 
#Notas: 
#1.-utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar listas para almacenar el nombre de un alumno y 3 calificaciones
import calificaciones

def main():
    opcion=True
    while opcion:
        calificaciones.borra_pantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
                case "1":
                    calificaciones.agregar_Calificaciones()
                    calificaciones.esperarTecla()
                case "2":
                    calificaciones.mostrar_calificaciones()
                    calificaciones.esperarTecla() 
                case "3":
                    calificaciones.calcular_promedios()   
                    calificaciones.esperarTecla()
                case "4":
                    calificaciones.agregarCaracteristicaCalificacion() 
                    calificaciones.esperarTecla()
                case "5": 
                    calificaciones.modificarCaracteristcaCalificacion()
                    calificaciones.esperarTecla()
                case "6": 
                    calificaciones.borrarCaracteristicaCalificacion()
                    calificaciones.esperarTecla()
                case "7":
                    opcion=False    
                    print("Terminaste la ejecucion del SW")
                    calificaciones.esperarTecla()
                    print("/n\tTerminaste la ejecucion del SW")
                case _:
                    opcion=True 
                    input("Opción invalida vuelva a intentarlo ... por favor")

if __name__=="__main__":
    main()
