import tkinter as tk

# --- Configuración inicial ---
ANCHO = 600
ALTO = 400
VEL_PELOTA = 4
VEL_IA = 6  # Velocidad de la IA (más rápida = más difícil)
PUNTOS_MAX = 15

ventana = tk.Tk()
ventana.title("Ping pong")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

# --- Crear objetos ---
pelota = canvas.create_oval(290, 190, 310, 210, fill="white")
raqueta_izq = canvas.create_rectangle(20, 150, 30, 250, fill="white")
raqueta_der = canvas.create_rectangle(570, 150, 580, 250, fill="white")

# Texto marcador
marcador = canvas.create_text(ANCHO/2, 30, text="0 - 0", fill="white", font=("Arial", 20))

# Velocidades iniciales
dx, dy = 0, 0
vel_raqueta = 20

# Puntos
puntos_izq = 0
puntos_der = 0

# Bandera de juego
jugando = False

# ID del texto de ganador
texto_ganador = None

# Control del jugador derecho: True = IA, False = jugador
contra_ia = False

# --- Movimiento de la pelota ---
def mover_pelota():
    global dx, dy, puntos_izq, puntos_der, jugando

    if not jugando:
        return

    canvas.move(pelota, dx, dy)
    x1, y1, x2, y2 = canvas.coords(pelota)

    # Rebote en bordes superior/inferior
    if y1 <= 0 or y2 >= ALTO:
        dy = -dy

    # Rebote en raquetas -> aumenta velocidad
    if colision(pelota, raqueta_izq) or colision(pelota, raqueta_der):
        dx = -dx
        dx *= 1.2
        dy *= 1.2

    # Gol en el lado izquierdo
    if x1 <= 0:
        puntos_der += 1
        actualizar_marcador()
        if puntos_der >= PUNTOS_MAX:
            fin_partida("Jugador Derecho")
            return
        reiniciar_pelota(-VEL_PELOTA)

    # Gol en el lado derecho
    if x2 >= ANCHO:
        puntos_izq += 1
        actualizar_marcador()
        if puntos_izq >= PUNTOS_MAX:
            fin_partida("Jugador Izquierdo")
            return
        reiniciar_pelota(VEL_PELOTA)

    # Movimiento de la IA si está activada
    if contra_ia:
        mover_ia()

    ventana.after(20, mover_pelota)

# --- IA para raqueta derecha ---
def mover_ia():
    x1, y1, x2, y2 = canvas.coords(raqueta_der)
    _, py1, _, py2 = canvas.coords(pelota)
    centro_raqueta = (y1 + y2) / 2
    centro_pelota = (py1 + py2) / 2
    # IA sigue la pelota con velocidad máxima de VEL_IA
    if centro_raqueta < centro_pelota:
        canvas.move(raqueta_der, 0, min(VEL_IA, centro_pelota - centro_raqueta))
    elif centro_raqueta > centro_pelota:
        canvas.move(raqueta_der, 0, -min(VEL_IA, centro_raqueta - centro_pelota))

# --- Colisión pelota-raqueta ---
def colision(bola, raqueta):
    x1, y1, x2, y2 = canvas.coords(bola)
    rx1, ry1, rx2, ry2 = canvas.coords(raqueta)
    return (x1 < rx2 and x2 > rx1 and y1 < ry2 and y2 > ry1)

# --- Movimiento de raquetas ---
def mover_arriba(event, raqueta):
    canvas.move(raqueta, 0, -vel_raqueta)

def mover_abajo(event, raqueta):
    canvas.move(raqueta, 0, vel_raqueta)

# --- Reiniciar pelota ---
def reiniciar_pelota(direccion=VEL_PELOTA):
    global dx, dy
    canvas.coords(pelota, 290, 190, 310, 210)
    dx, dy = direccion, VEL_PELOTA

# --- Actualizar marcador ---
def actualizar_marcador():
    canvas.itemconfig(marcador, text=f"{puntos_izq} - {puntos_der}")

# --- Fin de partida ---
def fin_partida(ganador):
    global jugando, dx, dy, texto_ganador
    jugando = False
    dx, dy = 0, 0
    texto_ganador = canvas.create_text(
        ANCHO/2, ALTO/2, text=f"¡{ganador} gana!",
        fill="yellow", font=("Arial", 24, "bold")
    )

# --- Iniciar partida ---
def iniciar_partida(ia=False):
    global puntos_izq, puntos_der, jugando, texto_ganador, contra_ia
    contra_ia = ia
    if texto_ganador is not None:
        canvas.delete(texto_ganador)
        texto_ganador = None

    puntos_izq = 0
    puntos_der = 0
    actualizar_marcador()
    canvas.coords(pelota, 290, 190, 310, 210)
    jugando = True
    reiniciar_pelota(VEL_PELOTA)
    mover_pelota()

# --- Botones de menú inicial ---
frame_menu = tk.Frame(ventana)
frame_menu.pack(pady=10)

boton_ia = tk.Button(frame_menu, text="Jugar contra IA", command=lambda: iniciar_partida(True))
boton_ia.pack(side="left", padx=10)

boton_jugador = tk.Button(frame_menu, text="Jugar contra otro jugador", command=lambda: iniciar_partida(False))
boton_jugador.pack(side="left", padx=10)

# Controles jugador izquierdo (siempre jugador)
ventana.bind("w", lambda e: mover_arriba(e, raqueta_izq))
ventana.bind("s", lambda e: mover_abajo(e, raqueta_izq))

# Controles jugador derecho solo si NO es IA
def controles_jugador_derecho(event, arriba=True):
    if not contra_ia:
        if arriba:
            mover_arriba(event, raqueta_der)
        else:
            mover_abajo(event, raqueta_der)

ventana.bind("<Up>", lambda e: controles_jugador_derecho(e, True))
ventana.bind("<Down>", lambda e: controles_jugador_derecho(e, False))

ventana.mainloop()
