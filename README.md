# Ping pong en Python (Tkinter)

¡Bienvenido al clásico juego de **Pong** desarrollado en Python usando **Tkinter**! 🏓

---

## 🎮 Descripción

Este es un proyecto de Pong donde puedes jugar:

* **Contra otro jugador** usando el teclado.
* **Contra la IA**, con dificultad ajustable.

El juego incluye:

* Marcador de puntos (partida a 15 puntos).
* Aceleración de la pelota cada vez que rebota en una raqueta.
* Botón de “Iniciar partida”.
* Mensajes de victoria cuando un jugador llega a 15 puntos.

---

## ⌨ Controles

**Jugador izquierdo:**

* `W` → mover arriba
* `S` → mover abajo

**Jugador derecho (solo si no es IA):**

* `↑` → mover arriba
* `↓` → mover abajo

---

## 🧩 Requisitos

* Python 3.8 o superior
* Tkinter (generalmente viene incluido con Python)

Opcional (para crear `.exe`):

* PyInstaller

---

## ⚡ Cómo ejecutar

1. Clona el repositorio o descarga los archivos:

```bash
git clone <URL_DEL_REPOSITORIO>
cd pong
```

2. Ejecuta el juego con Python:

```bash
python main.py
```

3. Selecciona si quieres jugar contra otro jugador o contra la IA y comienza la partida.

---

## 📦 Crear un `.exe` (opcional)

Si quieres generar un ejecutable para Windows:

```bash
python -m PyInstaller --onefile --windowed main.py
```

El `.exe` se encontrará en la carpeta `dist/`.

---

## 🌟 Estructura recomendada del proyecto

```
PING-PONG/
├─ main.py
├─ assets/        # (opcional, imágenes o sonidos)
├─ README.md
└─ LICENSE       # Licencia MIT
```

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver archivo [LICENSE](LICENSE) para más detalles.

---
