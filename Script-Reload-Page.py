import keyboard
import time
import webbrowser

def refrescar_pagina():

    webbrowser.open_new_tab('html://..')

    # Espera 10 segundos
    time.sleep(10)

    # Cierra la pestaña actual
    keyboard.press_and_release('ctrl+w')

# Configura la tecla para pausar la recarga
tecla_pausa = 'p'

# Variable para pausar/despausar la recarga
pausado = False

# Bucle principal
while True:
    # Refresca la página si no está pausado
    if not pausado:
        refrescar_pagina()

    # Espera 1 segundo antes de verificar la tecla de pausa nuevamente
    time.sleep(1)

    # Verifica si la tecla de pausa ha sido presionada
    if keyboard.is_pressed(tecla_pausa):
        pausado = not pausado
        time.sleep(1)  # Espera 1 segundo para evitar múltiples activaciones por una sola pulsación