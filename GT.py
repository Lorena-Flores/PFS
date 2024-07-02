import os 
from termcolor import colored # Importa la función colored para imprimir el texto con color

class Tarea:
    # Define la clase Tarea para representar una tarea con su descripción y estado
   def __init__(self, descripcion, completada=False):
       # Inicializa una nueva tarea con su descripcion y estado (por defecto Pendiente)
       self.descripcion = descripcion
       self.completada = completada

class GestorTareas:
    # Define la clase GestorTareas para manejar una lista de tareas
   def __init__(self):
       # Inicializa el gestor de tareas con una lista vacía de tareas
       self.tareas = []

   def agregar_tarea(self, descripcion):
       # Agrega una nueva tarea a la lista
       self.tareas.append(Tarea(descripcion))

   def mostrar_tareas(self):
       # Muestra todas las tareas de la lista
       os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
       # Se imprime el encabezado y el título de la lista de tareas
       print(colored("\n\n********* LISTA DE TAREAS PENDIENTES *********", "cyan"))
       print(colored("\n*** Realizada por: Lorena Flores Fernández ***", "cyan"))
       print(colored("\n**********************************************\n", "cyan"))
       print(colored("\n* * * * * * * * MENÚ PRINCIPAL * * * * * * * *\n", "blue"))
       # Imprime las columnas de la tabla de tareas
       print(colored("{:<5} {:<20} {:<15}".format("ID", "Nombre de la tarea", "Estado"), "blue"))
       print(colored("-" * 45, "blue"))  # Línea de separación
       # Itera sobre todas las tareas y las imprime con su estado
       for i, tarea in enumerate(self.tareas, start=1):
           estado = colored("Completada", "green") if tarea.completada else colored("Pendiente", "red")
           print(colored("{:<5} {:<20} {:<15}".format(i, tarea.descripcion, estado), "blue"))
           # Imprime un mensaje si todas las tareas están completadas
       if all(tarea.completada for tarea in self.tareas):
           print(colored("\nZorionak! Has completado todas las tareas de tu lista.", "magenta"))

   def validar_posicion(self, posicion):
       # Valida si la posición introducida es válida para acceder a una tarea en la lista
       return 0 <= posicion < len(self.tareas)

   def marcar_completada(self, posicion):
       # Marca una tarea como completada en la lista de tareas
       if self.validar_posicion(posicion): # Verifica si la posición es válida
           self.tareas[posicion].completada = True
       else:
           print(colored("\nPosición inválida.", "red")) # Imprime un mensaje de error si la posición es inválida

   def eliminar_tarea(self, posicion):
       # Elimina una tarea de la lista
       if self.validar_posicion(posicion): # Verifica si la posición es válida
           del self.tareas[posicion] # Elimina la tarea en la posición indicada
       else:
           print(colored("\nPosición inválida.", "red")) # Imprime un mensaje de error si la posición es inválida

def mostrar_menu():
   # Muestra el encabezado y el menú principal
   os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
   print(colored("\n\n********* LISTA DE TAREAS PENDIENTES *********", "cyan"))
   print(colored("\n*** Realizada por: Lorena Flores Fernández ***", "cyan"))
   print(colored("\n**********************************************\n", "cyan"))
   print(colored("\n* * * * * * * * MENÚ PRINCIPAL * * * * * * * *\n", "blue"))
   print(colored("[1] Agregar una nueva tarea.", "blue"))
   print(colored("[2] Marcar una tarea como completada.", "blue"))
   print(colored("[3] Mostrar todas las tareas.", "blue"))
   print(colored("[4] Eliminar una tarea.", "blue"))
   print(colored("[5] Salir de la lista de tareas.", "blue"))
   print(colored("\n* * * * * * * * * * * * * * * * * * * * * * * *\n", "blue"))

gestor = GestorTareas() # Crea una instancia del GestorTareas

while True: # Bucle while para mostrar el menú y recibir instrucciones por parte del usuario
   mostrar_menu() # Muestra el menú principal
   opcion = input(colored("\nSelecciona una opción del MENÚ PRINCIPAL: ", "blue")) # Solicita una opción al usuario

   if opcion == "1": # Si la opción es agregar una nueva tarea
       descripcion = input(colored("\nIntroduce la tarea a realizar: ", "blue")) # Solicita la descripción de la tarea
       gestor.agregar_tarea(descripcion) # Agrega la tarea al GestorTareas
   elif opcion == "2": # Si la opción es marcar una tarea como completada
       gestor.mostrar_tareas() # Muestra todas las tareas
       if gestor.tareas:
           while True:
               try:
                   posicion = int(input(colored("\nIntroduce el ID de la tarea a marcar como completada: ", "blue"))) - 1
                   if gestor.validar_posicion(posicion): # Verifica si la posición es válida
                       gestor.marcar_completada(posicion) # Marca la tarea como completada
                       break
                   else:
                       print(colored("\nOpción inválida. Por favor, introduce un ID válido.", "red"))
                       # Imprime un mensaje de error en rojo cuando la opción introducida no es válida
               except ValueError:
                   # Imprime un mensaje de error en rojo cuando la opción introducida no es válida
                   print(colored("\nOpción inválida. Por favor, introduce un ID válido.", "red"))
   elif opcion == "3": # Si la opción es mostrar todas las tareas
       gestor.mostrar_tareas()
       input(colored("\nPresiona Enter para volver al MENÚ PRINCIPAL ...", "blue"))  # Espera a que el usuario presione Enter
   elif opcion == "4": # Si la opción es eliminar una tarea
       if gestor.tareas:
           while True:
               try:
                   posicion = int(input(colored("\nPor favor, introduce el ID de la tarea a eliminar: ", "blue"))) - 1
                   # Solicita al usuario que introduzca el ID de la tarea a eliminar
                   if gestor.validar_posicion(posicion): # Verifica si la opción es válida
                       gestor.eliminar_tarea(posicion) # Elimina la tarea
                       break
                   else:
                       print(colored("\nOpción inválida. Por favor, introduce un ID válido.", "red"))
                       # Imprime un mensaje de error en rojo cuando la opción introducida no es válida
               except ValueError:
                   print(colored("\nOpción inválida. Por favor, introduce un ID válido.", "red"))
   elif opcion == "5": # Si la opción es salir de la lista de tareas, imprime un mensaje de despedida
       print(colored("\nAgur Lorena! Vuelve cuando tengas más tareas pendientes.", "magenta"))
       break
   else:
       print(colored("\nOpción inválida. Por favor, selecciona una opción válida del MENÚ PRINCIPAL.", "red"))