---
tags:
  - metaheuristicas
  - parcial_1
---
# Computación Evolutiva
---
La Computación Evolutiva (EC) ==es un subcampo de la Inteligencia Artificial inspirado en la evolución biológica. Se basa en mecanismos como la selección natural, la mutación y la recombinación para resolver problemas de optimización y búsqueda.==

### Algoritmos genéticos
---
Los Algoritmos Genéticos (GA) ==son una de las técnicas más populares dentro de la computación evolutiva. Fueron desarrollados por John Holland y están basados en la selección natural de Darwin y utilizan una población de soluciones candidatas que evolucionan con operadores genéticos.== 

_Componentes principales:_

- **Individuo/Cromosoma:** Representación de una posible solución al problema.
- **Población**: Conjunto de individuos en una generación.
- **Función de aptitud (fitness)**: Evalúa qué tan buena es una solución.
- **Selección:** Escoge los mejores individuos para reproducirse. Existen diferentes técnicas (elitista, ruleta, torneo, etc.)
- **Cruzamiento (crossover)**: Combina dos soluciones para generar nuevas. Existen diferentes técnicas (de un punto, etc.)
- **Mutación:** Introduce variaciones aleatorias para mantener la diversidad.
- **Iteraciones = generaciones:** El proceso se repite durante varias generaciones hasta alcanzar una solución óptima.

Con estos conceptos, podemos analizar los _pasos del algoritmo_:

1. **Generar población inicial**.
2. **Seleccionar** a los individuos en base al **fitness** y a algún método de selección.
3. **Cruzar** a los individuos seleccionados.
4. **Se muta** a los individuos que resulten del cruzamiento.
5. **Se itera de nuevo** hasta encontrar una solución óptima.

### Estrategias Evolutivas
---
Las Estrategias Evolutivas (ES) ==son otro enfoque dentro de la computación evolutiva, utilizadas principalmente para optimización en espacios continuos. Fueron introducidas en los años 60 por Rechenberg y Schwefel.==

*Características principales:*

- Trabajan con vectores de valores reales en lugar de representaciones discretas.
- Utilizan mutaciones gaussianas en lugar de operadores de cruzamiento complejos.
- Selección basada en "$\mu + \lambda$" (donde $\mu$ son los padres y $\lambda$ los descendientes).
- Muy efectivas en optimización de funciones matemáticas y problemas de control.

### Programación Evolutiva
---
La Programación Evolutiva (EP) ==fue propuesta por Lawrence J. Fogel en los años 60 como una técnica para la predicción y optimización de sistemas.==

*Diferencias clave con los AG y EE:*

- No usa operadores de cruzamiento, solo mutación.
- Se centra más en la evolución de máquinas de estado finito para resolver problemas.
- Suele utilizar mutaciones con distribución de Cauchy o Normal para generar variaciones.

###  Algoritmos de Estimación de la Distribución
---
Los **algoritmos de estimación de la distribución (EDA, por sus siglas en inglés: Estimation of Distribution Algorithms)** son una clase de algoritmos evolutivos que utilizan modelos probabilísticos para guiar la búsqueda de soluciones óptimas. A diferencia de los algoritmos genéticos tradicionales, los EDAs no emplean operadores de cruce y mutación, sino que construyen y actualizan una distribución de probabilidad sobre el espacio de soluciones.

##### Pasos
---
Los EDAs siguen un esquema general que consta de los siguientes pasos:

1. **Inicialización**: Se genera una población inicial de manera aleatoria.
2. **Selección**: Se elige un subconjunto de individuos con mejor desempeño según la función objetivo.
3. **Estimación de la distribución**: Se construye un modelo probabilístico que describe la distribución de los individuos seleccionados.
4. **Muestreo**: Se generan nuevos individuos a partir del modelo probabilístico.
5. **Reemplazo**: La nueva generación sustituye a la anterior y el proceso se repite hasta que se cumpla un criterio de parada.

##### Modelos de Distribución
---
Dependiendo del nivel de complejidad del modelo probabilístico, los EDAs pueden clasificarse en:

- **EDAs univariados**: Asumen independencia entre variables. Ejemplo: **PBIL (Population-Based Incremental Learning)**.
- **EDAs bivariados**: Consideran dependencias entre pares de variables. Ejemplo: **MIMIC (Mutual Information Maximization for Input Clustering)**.
- **EDAs multivariados**: Modelan dependencias complejas mediante redes bayesianas o modelos de Markov. Ejemplo: **BOA (Bayesian Optimization Algorithm)**.

##### Aplicaciones
---
Los EDAs se han aplicado con éxito en diversas áreas, incluyendo:

- **Optimización combinatoria** (problema del viajero, empaquetamiento de objetos, scheduling).
- **Optimización continua** (ajuste de parámetros en redes neuronales, diseño de circuitos).
- **Bioinformática** (alineamiento de secuencias, predicción de estructuras proteicas).
