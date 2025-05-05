# importamos las librerías necesarias
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os

# Configuramos el estilo del gráfico
plt.style.use('bmh')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams["xtick.direction"] = "out"
plt.rcParams["ytick.direction"] = "out"


# Parámetros del sistema
nt = 2000       # número de pasos (frames)
LX, LY = 10, 10 # tamaño de la caja
carpeta = 'Datos'  # ruta a los archivos .dat

# Configuramos figura y ejes
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel(r'$L_x$', fontsize=14, labelpad=10)
ax.set_ylabel(r'$L_y$', fontsize=14, labelpad=10)
ax.set_aspect('equal')
ax.grid(False)
particulas, = ax.plot([], [], 'o', color='gray', markersize=65)  # tupla con un solo elemento (inicialización del gráfico)

def get_filename(i): # Devuelve el nombre de archivo 
    return os.path.join(carpeta, f"xy{i:04d}.dat")

def init(): # función de inicialización de la animación
    particulas.set_data([], [])
    return particulas,

def update(frame): # función que se actualiza para cada frame 
    nombre = get_filename(frame)   # nombre del archivo actual
    data = np.loadtxt(nombre) # Carga las coordenadas x, y
    x, y = data[:, 0], data[:, 1] # Separa columnas
    particulas.set_data(x, y) # Actualiza la posición de las partículas
    return particulas,

ani = animation.FuncAnimation(fig, update, frames=nt, init_func=init,   #animación
                              interval=15, blit=True)

ani.save("imagenes/simulacion.mp4", writer='ffmpeg', fps=30) # guardamos la animación
plt.show()
