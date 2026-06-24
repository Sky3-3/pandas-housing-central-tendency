# Proyecto Python: Análisis de Tendencia Central y Costo de Vida Inmobiliario con Pandas

Este repositorio contiene un proyecto práctico desarrollado en Python utilizando las librerías **Pandas**, **NumPy** y **SciPy** enfocado en el cálculo e interpretación de medidas de tendencia central aplicadas al mercado de alquileres de viviendas en la ciudad de Nueva York. El script carga conjuntos de datos independientes para departamentos de una habitación distribuidos en tres distritos (*boroughs*) de la metrópoli (Brooklyn, Manhattan y Queens), automatizando la extracción de métricas base para realizar análisis comparativos directos de costo de vida y asimetría de distribuciones financieras.

---

## Código Python del Proyecto

El programa realiza la ingesta de las bases de datos de alquileres por regiones y calcula los estadísticos de centralización poblacionales:

```python
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

---

## Reporte Estadístico e Interpretación del Mercado

Al contrastar de forma paralela los resultados numéricos obtenidos por el motor de cálculo, se extrae el siguiente cuadro resumen analítico de las tarifas de Nueva York:

### 1. Cuadro Comparativo de Tendencia Central (Precios en USD)

| Distrito Evaluado (*Borough*) | Precio Promedio (Media) | Precio Central (Mediana) | Precio Común (Moda) | Conclusión del Perfil Económico |
| --- | --- | --- | --- | --- |
| **Manhattan** | 3993.48 USD | 3800.00 USD | 3500.00 USD | Región con el costo de vida e inmobiliario más elevado del análisis. |
| **Brooklyn** | 3327.40 USD | 3000.00 USD | 2500.00 USD | Costo intermedio; mercado altamente demandado con valores estables. |
| **Queens** | 2346.25 USD | 2200.00 USD | 1750.00 USD | Zona más accesible económicamente de las tres muestras auditadas. |

### 2. Diagnóstico de Asimetría Financiera

En los tres distritos analizados se cumple una relación matemática estricta respecto al orden de las métricas:

$$\text{Media} > \text{Mediana} > \text{Moda}$$

En ciencia de datos, cuando el promedio es mayor que la mediana, denota una distribución con **sesgo positivo (asimetría hacia la derecha)**. Esto significa que la gran mayoría de los departamentos se agrupan en valores relativamente bajos o estándar, pero existe una cantidad minoritaria de departamentos de lujo con alquileres extremadamente caros que empujan artificialmente la media hacia arriba. Por lo tanto, la **mediana** es la métrica más confiable para evaluar el costo de vida real, ya que no se ve afectada por esos valores atípicos (*outliers*).

---

## Conceptos Técnicos Aplicados

* **Media Aritmética frente a Robustez**: La media (`np.average()`) es sensible a los extremos. En el sector inmobiliario, propiedades de alto valor sesgan el promedio, haciendo necesario contrastarlo con otros estadísticos.
* **Mediana como Punto de Partición**: El valor central (`np.median()`) divide la muestra ordenada exactamente en dos mitades iguales. Garantiza que el 50% de los alquileres se ubiquen por debajo de esa tarifa, sirviendo como indicador robusto de tendencia.
* **Función `stats.mode()**`: Módulo inferencial que identifica el elemento que más veces se repite en una serie. Retorna un objeto compuesto que contiene tanto el valor de la moda (`mode[0]`) como el conteo absoluto de sus ocurrencias (`count[1]`).

