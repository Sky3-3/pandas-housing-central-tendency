import numpy as np
import pandas as pd
from scipy import stats

# --- 1. Ingesta de Datos Inmobiliarios por Distritos ---
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

# --- 2. Desarrollo de Cálculos Analíticos (Métricas del Modelo) ---
# Cálculo de Medias Aritméticas (Promedios)
brooklyn_mean = np.average(brooklyn_price)
manhattan_mean = np.average(manhattan_price)
queens_mean = np.average(queens_price)

# Cálculo de Medianas (Punto de corte central del 50%)
brooklyn_median = np.median(brooklyn_price)
manhattan_median = np.median(manhattan_price)
queens_median = np.median(queens_price)

# Cálculo de Modas (Valores con mayor frecuencia absoluta de repetición)
brooklyn_mode = stats.mode(brooklyn_price)
manhattan_mode = stats.mode(manhattan_price)
queens_mode = stats.mode(queens_price)

# --- 3. Reporte de Control de Resultados en Consola ---
print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
print("The mean price in Queens is " + str(round(queens_mean, 2)))

print("\nThe median price in Brooklyn is " + str(brooklyn_median))
print("The median price in Manhattan is " + str(manhattan_median))
print("The median price in Queens is " + str(queens_median))

print("\nThe mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " (Frecuencia: " + str(brooklyn_mode[1][0]) + ")")
print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " (Frecuencia: " + str(manhattan_mode[1][0]) + ")")
print("The mode price in Queens is " + str(queens_mode[0][0]) + " (Frecuencia: " + str(queens_mode[1][0]) + ")")

```
