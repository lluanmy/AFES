#importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt


# Configuramos el estilo del gráfico
plt.style.use('bmh')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams["xtick.direction"] = "out"
plt.rcParams["ytick.direction"] = "out"


# velocidades simuladas
vx, vy = [], []

#usamos, por ejemplo, los 201 últimos archivos para asegurarnos el estado de equilibrio 
for i in range( 1800,2001):
    nombre_archivos = f'Datos/vxvy{i:04d}.dat'
    datos = np.loadtxt(nombre_archivos)
    vx.extend(datos[:, 0])
    vy.extend(datos[:, 1])

# Módulo de la velocidad
vel = np.sqrt(np.array(vx)**2 + np.array(vy)**2)

plt.figure(figsize=(8, 6))  #tamaño de la figura

# Histograma normalizado
counts, bins, _ = plt.hist(vel, bins=50, density=True,color='teal' ,alpha=0.6, label='Simulación')

v = np.linspace(0, max(vel), 500) # intervalo de velocidades (eje x)
T = 1.523588  # Temperatura media simulada
MB = (v / T) * np.exp(-v**2 / (2*T)) # función de Maxwell-Boltzmann
plt.plot(v, MB, label='Maxwell-Boltzmann',color='crimson')
plt.xlabel(r'$Velocidad\ | v |$', fontsize=14, labelpad=10)
plt.ylabel(r'$Distribución\ de\ probabilidad$', fontsize=14, labelpad=10)
plt.legend(loc='upper right', frameon=True, fontsize=10, fancybox=True, edgecolor='grey', facecolor='white')
plt.grid(False)
plt.show()
