import tkinter as tk
from tkinter import Text
import logging
import threading
from fcshot_estandar import Bot


# Función para mostrar el registro
def mostrar_registro():
    registro_window = tk.Toplevel()
    registro_window.title("Registro")
    registro_window.geometry("1000x800")
    text_widget = tk.Text(registro_window)
    # Cambiar el tamaño del widget Text (ancho y alto)
    text_widget.config(width=1000, height=800)  # Personaliza el ancho y alto según tus preferencias
    text_widget.pack()

    def actualizar_contenido():
        try:
            with open('archivo_de_log.log', 'r') as file:
                log_content = file.read()
            text_widget.delete(1.0, tk.END)  # Limpia el contenido anterior
            text_widget.insert(tk.END, log_content)
            text_widget.see(tk.END)  # Desplaza automáticamente hacia abajo
            registro_window.after(5000, actualizar_contenido)  # Actualiza cada 5000 ms (5 segundos)
        except FileNotFoundError:
            text_widget.insert(tk.END, "Archivo de log no encontrado.")

    actualizar_contenido()
def obtener_valores_y_llamar_funcion():
    # Obtener los valores de las entradas
    val1 = entrada_valor1.get()
    val2 = entrada_valor2.get()
    val3 = entrada_valor3.get()
    val4 = entrada_valor4.get()

    # Llamar a la función de la clase con los valores
    bot.snipefc(val1, val2, val3, val4)

# Función para iniciar el proceso y mostrar el registro
def iniciar_proceso_y_mostrar_registro():
    t1 = threading.Thread(target=obtener_valores_y_llamar_funcion)
    t1.start()
    mostrar_registro()

# Crear una instancia de la clase
bot = Bot()

ventana = tk.Tk()
ventana.title("Interfaz Gráfica")
ventana.geometry("800x600")

# Crear una variable de cadena para almacenar la selección
seleccion = tk.StringVar(ventana)



# Crear entradas
nombre_jugador = tk.Label(ventana, text="Nombre Jugador:")
entrada_valor1 = tk.Entry(ventana)
precio_inicial = tk.Label(ventana, text="Precio inicial:")
entrada_valor2 = tk.Entry(ventana)
precio_final = tk.Label(ventana, text="Precio final:")
entrada_valor3 = tk.Entry(ventana)
intervalo = tk.Label(ventana, text="Intervalo:")
entrada_valor4 = tk.Entry(ventana)

# Crear botón para obtener valores y llamar a la función
boton_llamar_funcion = tk.Button(ventana, text="Buscar Jugador", command=iniciar_proceso_y_mostrar_registro)

nombre_jugador.pack()
entrada_valor1.pack()
precio_inicial.pack()
entrada_valor2.pack()
precio_final.pack()
entrada_valor3.pack()
intervalo.pack()
entrada_valor4.pack()
boton_llamar_funcion.pack()

ventana.mainloop()