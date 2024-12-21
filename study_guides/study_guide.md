---
tags:
  - Redes_1
  - parcial3
---
## Redes de Comunicaciones y Cómputo
---
### Redes de Información Masivas 
---
==Una red de información masiva es un conjunto de recursos que transmiten información a una gran cantidad de personas de forma simultánea.==

**La Conexión en Red**, es el proceso de conectar dos o más dispositivos informáticos para permitir la transmisión e intercambio de información y recursos

##### Evolución de las redes
---
La primer red informática en funcionamiento fue creada por el departamento de defensa de los Estados Unidos en la década de 1960, llamada DARPANET.

Un ejemplo actual de una red de información masiva es el Internet, la cual, es una red descentralizada de redes de comunicación.


### Redes de Información Privadas
---
==Una red de información privada es una red segura que solo pueden utilizar ciertos dispositivos o usuarios, y que está aislada de la red pública del internet.==

Se utilizan para conectar equipos dentro de una organización (**Intranet**) o de varias organizaciones (**Extranet**). 

Para que los dispositivos se conecten al internet, es necesario de una puerta de enlace, a través de su ISP

##### Ejemplos
---
**En Casa**. Nosotros somos el administrador de la red, y nos conectamos a través del router

**En una Empresa**. Se conectan diversos equipos, incluso de manera remota por medio de un VPN

##### Ventajas
---
- **Seguridad**
- **Control**
- **Mayor tasa de transferencia entre los dispositivos**
- **Permite compartir recursos**


### Redes conmutadas
---
##### Conmutación de Circuitos virtuales
---
- **Circuitos virtuales conmutados**. Se establece una ruta lógica entre dos máquinas, esta ruta lógica se usará para futuras comunicaciones y se libera después de cada transmisión

- **Circuitos virtuales permanentes**. Es lo mismo que el conmutado, pero los circuitos una vez que se establecen, quedan fijados para futuras comunicaciones.


### Clasificación de Redes de Comunicación por Extensión
---
**PAN (Personal Area Network)**. Es una red diseñada para conectar dispositivos dentro de un área muy pequeña, generalmente de unos pocos metros (como una habitación).

**LAN (Local Area Network)**. Una red que conecta dispositivos en un área local limitada, como una casa, oficina, o campus universitario.

**MAN (Metropolitan Area Network)**. Es una red más extensa que una LAN, diseñada para cubrir una ciudad o un área metropolitana.

**WAN (Wide Area Network)**. Una red que cubre grandes distancias geográficas, conectando múltiples LANs, MANs, o incluso dispositivos individuales en diferentes partes del mundo.

### VLAN
---
==Es una tecnología que nos permite crear redes lógicas independientes dentro de la misma red física.== 

**Dentro de sus beneficios podemos encontrar.**

- _Seguridad._ Nos permite aislar el tráfico entre diferentes VLANs.

- _Segmentación._ De esta manera podemos organizar nuestra red de diferentes formas

- _Flexibilidad._ Nos permite colocar equipos en diferentes subredes de manera rápida

- _Optimización._ Al ser redes más pequeñas, el broadcast solo se hace en partes pequeñas de la red.

- _Mejora eficiencia del personal de TI_. 


### Enrutamiento
---
==El enrutamiento es el proceso de selección de rutas en cualquier red.==

**Elementos de una red de computación**
1. Hosts
2. Nodos de comunicación
3. Rutas de conexión entre nodos

La comunicación entre dos nodos de una red se puede producir a través de muchas rutas, la meta del enrutamiento es seleccionar la mejor ruta.

##### Enrutador
---
==Es un dispositivo de red que conecta los dispositivos de computación y las redes a otras redes.==

Cumple con 3 funciones principales

1. **Determinación de la ruta**
2. **Reenvío de datos**
3. **Balanceador de carga**

##### Cómo funciona?
---
Los datos se mueven en la red en forma de paquetes, los cuales son enviados por el enrutador desde un origen hasta un destino.

Para esto, el enrutador us una tabla de de enrutamiento, la cual le indica el camino óptimo para llegar de punto A a punto B. Y existen 2 tipos de enrutamiento.

##### 1. Enrutamiento Estático
---
==Esto se basa en un administrador de red, quién configura manualmente las rutas de red. Es útil cuando la arquitectura de red permanezca constante.==

Pero puede llevar a congestionamientos, y disminuye la adaptabilidad y flexibilidad de las redes. 

##### 2. Enrutamiento Dinámico
---
==Es un conjunto de reglas que crean, mantienen y actualizan la tabla de enrutamiento dinámico.== Se adapta a la condiciones cambiantes de la red, como el volumen de tráfico, el ancho de banda, entre otros.

#### Protocolos de Enrutamiento
---
==Son un conjunto de reglas que especifican cómo los enrutadores identifican paquetes y reenvían paquetes.==

Y se pueden clasificar en 2

##### 1. Protocolos de puerta de enlace interior
---
Evalúan el sistema y toman decisiones de enrutamiento en función de algunas métricas, como por ejemplo

- Recuento de saltos
- Retraso o tiempo necesario para enviar de A a B
- Ancho de banda

**Algunos ejemplos...**

1. _RIP._ Se basa en los recuentos de saltos para determinar la ruta más corta
2. _OSPF._ Open Shortest Path First, recopila información de todos los demás enrutadores del sistema para identificar rutas más cortas.

##### 2. Protocolos de puerta de enlace exterior
---
==Sirven para gestionar de mejor manera la transferencia de información entre dos sistemas autónomos.==

El único protocolo de este tipo es **BGP (Border Gateway Protocol)**

Como el internet es una gran colección de sistemas autónomos, cada uno de estos sistemas tiene un ASN que obtiene al registrarse en al Autoridad de números asignados de Internet.

De esta manera BGP hace un seguimiento de los ASN más cercanos para calcular rutas óptimas.

#### Algoritmos de Enrutamiento
---
==Son programas de software que implementan diferentes protocolos de enrutamiento, funcionan mediante la asignación de un número de costo a cada enlace.==

Cada enrutador intenta enviar el paquete de datos al siguiente mejor enlace con el costo más bajo.

**Ejemplos de algoritmos.**

- Enrutamiento vector distancia
- Enrutamiento por estado de enlace

#### Enrutamiento en la nube
---
==Administra dinámicamente las conexiones entre dos redes de nube virtual.== Al ser un entorno virtual, un enrutador en la nube, es un software que virtualiza las funciones de un enrutador, facilitando sus funciones.


## Aspectos Funcionales para Redes de Cómputo
---
### Aspectos Funcionales para Redes de Cómputo
---
##### Historia (ARPANET)
---
ARPA (Agencia de Proyectos de Investigación Avanzada), fue una iniciativa del departamento de defensa de los Estados Unidos. ==Tuvo como objetivo la creación de una red de computadoras capaz de comunicar usuarios en distintas computadoras==.

La versión inicial de ARPANET contaba con 4 ubicaciones principales

- La Universidad de California
- Standford
- La universidad de California en Santa Bárbara
- La universidad de Utah

==Esta primer red es considerada como el inicio del Internet.==

Se puede decir que la idea surgió de _J. Licklider_. El objetivo era desarrollar una red que funcionara independientemente de la localización de las ordenadores o de los sistemas utilizados.

##### Componentes de ARPANET
---
- **Packet Switching**. La conmutación de paquetes funciona de un modo diferente a la conmutación de circuitos que se conoce a partid de la red telefónica. ARPANET sentó las bases de la _neutralidad de red_

- **IMP (Interface Message Processor)**. Eran máquinas pequeñas encargadas de la interoperabilidad de la red, es similar a lo que hacen los routers hoy en día

- **Nodos**. Son todos aquellos puntos de conexión que manejan información en una conectividad en red.

- **RFC (Request for comments)**. Son una serie de documentos públicos donde se describen y definen: protocolos, conceptos, métodos y programas de internet. Sentó la base para la creación de diferentes protocolos y procedimientos. Son una serie de documentos públicos donde se describen y definen: protocolos, conceptos, métodos y programas de internet. Sentó la base para la creación de diferentes protocolos y procedimientos.

- **Protocol 1822**. Protocolo que permitía la comunicación entre IMPs. Este exigía dos áreas por paquete, la información y los headers

- **NCP (Network Control Program)**. Este protocolo se utilizaba en la capa intermedia, la de transporte. Se usaba para establecer comunicaciones entre dos hosts.


### Software de Comunicaciones
---
##### Gateways
---
==Es un nodo de red que conecta dos reces con diferentes protocolos de transmisión, sirven como entrada y salida de una red.==

De esta manera, se simplifica la conectividad a Internet en un solo dispositivo.

**Gateway vs. Router**.

Las puertas de enlace se utiliza para unir dos redes diferentes (redes con protocolos primarios diferentes), mientras que el router solo une dos redes que tengan los mismos protocolos.

##### Proxies
---
==Es un servidor que actúa como intermediario entre un usuario y el internet.== Es muy útil, ya que cuenta con una caché que le sirve a todos los usuarios que usen dicho proxy. 

Este tipo de servidores también brindan seguridad y un mejor control.

**Proxy vs. VPN**.

Un Proxy funciona como agente entre un usuario e Internet, pero no cifran los datos, mientras que un servidor VPN encripta y enruta todo el tráfico de internet a través de un servidor remoto

##### Firewall
---
==El firewall es un sistema de seguridad de red que impide el acceso no autorizado a una red, este inspecciona el tráfico entrante y saliente mediante un conjunto de reglas de seguridad para identificar y bloquear amenazas.==

**Un firewall puede ser...** hardware físico, software, SaaS, o en la nube

Un firewall puede entrar en alguna de las **siguientes clasificaciones**

1. **Según lo que protegen**
	1. *Basados en red*. protegen redes enteras, suelen ser de hardware
	2. *Basados en host*. protegen dispositivos individuales
	
2. **Por método de filtrado**
	1. *Filtrado de paquetes*. examina paquetes aislados y sin contexto
	2. *Inspección de estado*. examinan el tráfico, y relacionan paquetes entre si
	3. *Puerta de enlace*. monitorean el protocolo TCP entre paquetes de clientes o servidores confiables
	4. *Proxy*. Inspeccionan los paquetes en la capa de aplicación
	5. *De próxima generación*. Son mutlicapa para integrar capacidades de firewalls empresariales con IPS y control de aplicaciones 
	6. *Virtuales*. son firewalls para entornos virtuales
	7. *Nativos de la nube*. brindan funciones de escalamiento automatizado.

**Uso de firewalls**

- *Defensa contra amenazas*
- *Funciones de registro y auditoría*
- *Filtrado de tráfico*
- *Control y bloqueo de acceso*
- *Acceso remoto seguro*


### Hardware de Comunicaciones
---
###### Esquema de Cableado
---
==Es un sistema de cables que permite transportar información de manera segura y eficiente dentro de una LAN.== Existen distintos tipos de cableados como por ejemplo...

- *Cableado vertical*. También llamado troncal, conecta los diferentes cuartos de servicio
- *Cableado horizontal*. Conecta las estaciones de trabajo con la red

Los siguientes aspectos se tienen que considerar al instalar un cableado estructurado

- Diseñar un esquema de cableado que permita futuras expansiones
- Seguir los estándares de cableado para asegurar la compatibilidad y el rendimiento óptimo

###### Tarjetas de Red
---
==Son aparatos que se encargan de preparar, transferir y controlar la información o datos que envían a los otros equipos que están conectados a una misma red.==

###### Repetidor
---
==Es un dispositivo que refuerza las señales, amplificándolas o regenerándolas.==

###### Transductores
---
==Son dispositivos que convierten las señales de un tipo a otro, permitiendo la comunicación y transmisión de datos de manera eficiente.== 
###### Firewall
---
==Es un dispositivo de seguridad de red que supervisa y controla el tráfico de red entrante y saliente para evitar accesos no autorizados.==

Lo logran, al inspeccionar paquetes entrantes y salientes, y deciden si los permiten o los bloquean en base de una serie de reglas.

###### Modem
---
==Es un dispositivo de entrada y salida, el cual conecta distintos equipos computacionales entre sí a través de una conexión entrante en una de Ethernet.== Los hay de dos tipos

1. Interno. Integrado en el equipo como una tarjeta
2. Externo. Fuera del equipo computacional

###### Codec
---
==Es un dispositivo capaz de convertir una señal analógica a una digital para transmitirla sobre una red de datos, su función consiste en transformar las señales digitales de audio y video en un formato que puede reproducirse.==

Antes eran de hardware, pero en la actualidad se usan casi únicamente de software. 

Los hay con pérdida y sin pérdida. Algunos ejemplos... MPEG, MKV, Apple ProRes

###### Puertos
---
==Son las interfaces que utilizan las aplicaciones para conectarse con otros elementos.== Los hay de dos tipos

1. de Hardware. son los puertos físicos
2. de Software. son los puertos lógicos

###### Bridges
---
==Conecta y filtra el tráfico entre dos o más segmentos de red, y opera en la capa dos del modelo OSI.== Por lo que a diferencia de un router que enrutan direcciones IP (capa 3), un puente lo hace con direcciones MAC (capa 2)

###### Switch
---
==Es un dispositivo que permite conectar varias computadoras entre si, este es un dispositivo de capa 2, por lo que usa las direcciones MAC. Aunque también los hay de capa 3 (para funcionar con direcciones IP).==


