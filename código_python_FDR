# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import os
import tarfile 

# Configuramos el estilo del gráfico
plt.style.use('bmh')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams["xtick.direction"] = "out"
plt.rcParams["ytick.direction"] = "out"

# Descomprimimos el archivo que contiene las posiciones de las partículas
with tarfile.open('nu02.tar.gz', 'r:gz') as tar_ref:
    tar_ref.extractall('datos_posicion')

# Listar y seleccionar archivos
archivos = sorted([f for f in os.listdir('datos_posicion') if f.startswith('xy') and f.endswith('.dat')])
# Seleccionamos el 10% final de los archivos para asegurar que el sistema está en equilibrio
archivos_seleccionados = archivos[int(0.9 * len(archivos)):]  # Último 10%

# Parámetros del sistema
R = 1  # Radio de las partículas
nu = 0.2  # Factor de empaquetamiento
N = 484  # Número de partículas
L = np.sqrt((N * np.pi * R**2) / nu)  # Longitud del sistema (cuadrado)
A = L**2  # Área total

# Definimos los intervalos radiales
num_intervalos = 75 # un número mayor (por ejemplo, 100) mejora la resolución pero incrementa las fluctuaciones (mayor ruido)
r_max = L / 2 # condición periódica (evita contar distancias mayores que el sistema)
delta_r = r_max / num_intervalos 
intervalos = np.linspace(0, r_max, num_intervalos + 1)
r_vals = 0.5 * (intervalos[:-1] + intervalos[1:])  # Centros de los intervalos

# Precalculamos el denominador para normalización de g(r)
normalizar = np.zeros(num_intervalos)
intervalos_validos = r_vals > 0
normalizar[intervalos_validos] = 2 * np.pi * r_vals[intervalos_validos] * delta_r

# Inicializamos un acumulador de g(r)
g_r_acumulado = np.zeros(num_intervalos)
num_archivos = 0

# Calcular g(r) con condiciones de contorno periódicas 
def calcular_g_r(posiciones): 
    
    h_n = np.zeros(num_intervalos)

    for i in range(N):
        for j in range(i + 1, N):
            # Diferencias con condiciones periódicas
            dx = posiciones[i, 0] - posiciones[j, 0]
            dy = posiciones[i, 1] - posiciones[j, 1]
            dx -= L * np.round(dx / L)  #convección de mínima imagen (algoritmo)
            dy -= L * np.round(dy / L)  #convección de mínima imagen (algoritmo)
            r_ij = np.sqrt(dx**2 + dy**2) # distancia euclídea

            # Asignamos al intervalo correspondiente
            intervalo_idx = int(r_ij / delta_r)
            if intervalo_idx < num_intervalos:
                h_n[intervalo_idx] += 2  # Contamos (i, j) y (j, i)

    # Normalizamos g(r), evitando división por cero
    g_r = np.zeros(num_intervalos)
    g_r[intervalos_validos] = (A / N**2) * (h_n[intervalos_validos] / normalizar[intervalos_validos])
    return g_r

# Procesamos cada archivo
for archivo in archivos_seleccionados:
    archivo_path = os.path.join('datos_posicion', archivo)
    posiciones = np.loadtxt(archivo_path)
    g_r = calcular_g_r(posiciones)
    g_r_acumulado += g_r
    num_archivos += 1

# Promediamos sobre los archivos
g_r_promedio = g_r_acumulado / num_archivos

# Graficamos g(r)
plt.figure(figsize=(10,6))
plt.plot(r_vals, g_r_promedio, color='crimson', lw=1, label=r"$g(r)$")
plt.xlabel(r"$r\ (u)$ ", fontsize=14, labelpad=10)
plt.ylabel(r"$\left\langle\ g(r)\ \right\rangle$", fontsize=14, labelpad=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title(r"$Función\ de\ Distribución\ Radial\ Promedio$", fontsize=16, pad=20)
plt.legend(loc='upper right', frameon=True, fontsize=10, fancybox=True, edgecolor='grey', facecolor='white')
plt.grid(False)
plt.show()
