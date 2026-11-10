# Ping Pong en Python (Tkinter)

[Español](#español) · [English](#english)

---

## Español

### Índice

- [Descripción](#descripción)
- [Características](#características)
- [Controles](#controles)
- [Requisitos](#requisitos)
- [Cómo ejecutar](#cómo-ejecutar)
- [Generar un ejecutable](#generar-un-ejecutable)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Cómo funciona](#cómo-funciona)
- [Licencia](#licencia)

### Descripción

Juego clásico de **ping pong** escrito en Python con **Tkinter**. Permite jugar dos personas en el mismo teclado o un jugador contra la máquina. Todo el juego se dibuja sobre un `Canvas` de 600 × 400 píxeles, sin dependencias externas más allá de la biblioteca estándar.

### Características

- **Dos modos de juego**: jugador contra jugador o jugador contra la IA.
- **Marcador a 15 puntos**: gana el primero que llegue a `PUNTOS_MAX`.
- **Dificultad progresiva**: la pelota acelera un 20 % cada vez que rebota en una raqueta.
- **IA con velocidad limitada**: la raqueta derecha sigue la pelota como máximo a `VEL_IA` píxeles por ciclo, así que es batible.
- **Reinicio rápido**: al terminar una partida se puede empezar otra desde el menú.
- **Sin instalación de dependencias**: solo Python y Tkinter.

### Controles

| Contexto | Tecla | Acción |
|---|---|---|
| Jugador izquierdo | `W` | Subir la raqueta |
| Jugador izquierdo | `S` | Bajar la raqueta |
| Jugador derecho (modo 2 jugadores) | `↑` | Subir la raqueta |
| Jugador derecho (modo 2 jugadores) | `↓` | Bajar la raqueta |

En el modo contra la IA la raqueta derecha se mueve sola y las flechas no tienen efecto.

### Requisitos

- **Python 3.8 o superior**.
- **Tkinter**, incluido por defecto en Windows y macOS. En Linux puede requerir instalación:

```bash
sudo apt install python3-tk
```

### Cómo ejecutar

```bash
python main.py
```

Se abre la ventana con dos botones: **Jugar contra IA** y **Jugar contra otro jugador**.

### Generar un ejecutable

El repositorio incluye `dist/main.exe` ya compilado. Para regenerarlo:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

### Estructura del proyecto

```text
Ping-pong/
├── main.py          # Todo el juego (lógica, dibujo y eventos)
├── dist/
│   └── main.exe     # Ejecutable para Windows ya compilado
├── LICENSE          # MIT
├── .gitignore
└── README.md
```

### Cómo funciona

- Un bucle con `ventana.after(20, mover_pelota)` actualiza la posición de la pelota cada 20 ms.
- `colision()` comprueba el solapamiento entre el rectángulo de la pelota y el de cada raqueta.
- Al golpear, se invierte `dx` y se multiplican ambas componentes por `1.2`.
- `mover_ia()` calcula el centro de la raqueta y lo desplaza hacia el centro de la pelota sin superar `VEL_IA`.
- Cuando un jugador alcanza 15 puntos, `fin_partida()` detiene el bucle y dibuja el mensaje de victoria.

### Licencia

Este proyecto se distribuye bajo la **licencia MIT**. Consulta [LICENSE](LICENSE).

---

## English

### Table of contents

- [Overview](#overview)
- [Features](#features)
- [Controls](#controls)
- [Requirements](#requirements)
- [How to run](#how-to-run)
- [Building an executable](#building-an-executable)
- [Project structure](#project-structure)
- [How it works](#how-it-works)
- [License](#license)

### Overview

A classic **Pong** game written in Python with **Tkinter**. Two people can play on the same keyboard, or one player can face the computer. The whole game is drawn on a 600 × 400 `Canvas` using only the standard library.

### Features

- **Two game modes**: player vs player or player vs AI.
- **First to 15 points** wins (`PUNTOS_MAX`).
- **Progressive difficulty**: the ball speeds up by 20 % every time it hits a paddle.
- **Capped AI speed**: the right paddle chases the ball at most `VEL_IA` pixels per tick, so it can be beaten.
- **Quick restart**: start a new match from the menu.
- **No third-party dependencies**: just Python and Tkinter.

### Controls

| Context | Key | Action |
|---|---|---|
| Left player | `W` | Move paddle up |
| Left player | `S` | Move paddle down |
| Right player (2-player mode) | `↑` | Move paddle up |
| Right player (2-player mode) | `↓` | Move paddle down |

In AI mode the right paddle moves on its own and the arrow keys do nothing.

### Requirements

- **Python 3.8 or later**.
- **Tkinter**, bundled with Windows and macOS. On Linux it may need to be installed:

```bash
sudo apt install python3-tk
```

### How to run

```bash
python main.py
```

The window shows two buttons: **Play vs AI** and **Play vs another player**.

### Building an executable

The repo ships a prebuilt `dist/main.exe`. To rebuild it:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

### Project structure

```text
Ping-pong/
├── main.py          # Entire game (logic, rendering and events)
├── dist/
│   └── main.exe     # Prebuilt Windows executable
├── LICENSE          # MIT
├── .gitignore
└── README.md
```

### How it works

- A `ventana.after(20, mover_pelota)` loop updates the ball every 20 ms.
- `colision()` checks whether the ball rectangle overlaps each paddle rectangle.
- On a hit, `dx` is inverted and both components are multiplied by `1.2`.
- `mover_ia()` compares paddle and ball centres and moves toward the ball without exceeding `VEL_IA`.
- When a player reaches 15 points, `fin_partida()` stops the loop and draws the victory message.

### License

This project is released under the **MIT License**. See [LICENSE](LICENSE).
