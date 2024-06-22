"""
def ventasTotales()
def costosTotales()
"""    

def ordenarLista(lista1,lista2,lista3,lista4,lista5):
    matrizResumenes = [lista1,lista2,lista3,lista4,lista5]
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(matrizResumenes)-1):
            if matrizResumenes[i][0] > matrizResumenes[i+1][0]:
                aux = matrizResumenes[i][0]
                matrizResumenes[i][0] = matrizResumenes[i+1][0]
                matrizResumenes[i+1][0] = aux
                desordenada = True
    
    listaA = [0,0]
    listaB = [0,0]
    listaC = [0,0]
    listaD = [0,0]
    listaE = [0,0]


    matrizCostos = [listaA,listaB,listaC,listaD,listaE]

    for i in range(len(matrizResumenes)-1):
        matrizCostos[i][0]=matrizResumenes[i][3]
        matrizCostos[i][1]=matrizResumenes[i][1]
    
    return matrizCostos
        

#Funcion1 -> Resumen de Ventas
"""
- calculo total de la facturacion del mes (asumir 30 dias)
- cuantos articulos totales se vendieron y el costo
"""
def resumenVentas(cocinaM1,cocinaM2,cocinaM3,heladeraM1,heladeraM2,heladeraM3,aireM1,aireM2,aireM3,lavarropasM1,lavarropasM2,lavarropasM3,microondasM1,microondasM2,microondasM3,precioCocina,precioHeladera,precioAire,precioLavarropas,precioMicroondas,unidadesTotal,costoCocina,costoHeladera,costoAire,costoLavarropas,costoMicroondas,almacenamientoTotal):
    # Calculamos el dinero generado por ventas por cada modelo
    total_cocinaM1 = cocinaM1*precioCocina[0]
    total_cocinaM2 = cocinaM2*precioCocina[1]
    total_cocinaM3 = cocinaM3*precioCocina[2]
    total_heladeraM1 = heladeraM1*precioHeladera[0]
    total_heladeraM2 = heladeraM2*precioHeladera[1]
    total_heladeraM3 = heladeraM3*precioHeladera[2]
    total_aireM1 = aireM1*precioAire[0]
    total_aireM2 = aireM2*precioAire[1]
    total_aireM3 = aireM3*precioAire[2]
    total_lavarropasM1 = lavarropasM1*precioLavarropas[0]
    total_lavarropasM2 = lavarropasM2*precioLavarropas[1]
    total_lavarropasM3 = lavarropasM3*precioLavarropas[2]
    total_microondasM1 = microondasM1*precioMicroondas[0]
    total_microondasM2 = microondasM2*precioMicroondas[1]
    total_microondasM3 = microondasM3*precioMicroondas[2]

    ventasTotales = total_cocinaM1+total_cocinaM2+total_cocinaM3+total_heladeraM1+total_heladeraM2+total_heladeraM3+total_aireM1+total_aireM2+total_aireM3+total_lavarropasM1+total_lavarropasM2+total_lavarropasM3+total_microondasM1+total_microondasM2+total_microondasM3
    
    # Calculamos el costo de cada modelo
    costos_cocinaM1 = cocinaM1*costoCocina[0]
    costos_cocinaM2 = cocinaM2*costoCocina[1]
    costos_cocinaM3 = cocinaM3*costoCocina[2]
    costos_heladeraM1 = heladeraM1*costoHeladera[0] 
    costos_heladeraM2 = heladeraM2*costoHeladera[1]
    costos_heladeraM3 = heladeraM3*costoHeladera[2]
    costos_aireM1 = aireM1*costoAire[0]
    costos_aireM2 = aireM2*costoAire[1]
    costos_aireM3 = aireM3*costoAire[2]
    costos_lavarropasM1 = lavarropasM1*costoLavarropas[0]
    costos_lavarropasM2 = lavarropasM1*costoLavarropas[1]
    costos_lavarropasM3 = lavarropasM1*costoLavarropas[2]
    costos_microondasM1 = microondasM1*costoMicroondas[0]
    costos_microondasM2 = microondasM1*costoMicroondas[1]
    costos_microondasM3 = microondasM1*costoMicroondas[2]

    costosTotales = costos_cocinaM1 + costos_cocinaM2 + costos_cocinaM3 + costos_heladeraM1 + costos_heladeraM2 + costos_heladeraM3 + costos_aireM1 + costos_aireM2 + costos_aireM3 + costos_lavarropasM1 + costos_lavarropasM2 + costos_lavarropasM3 + costos_microondasM1 + costos_microondasM2 + costos_microondasM3 + almacenamientoTotal

    # Facturación total del mes:
    facturacion = ventasTotales-costosTotales

    print(f"\nFacturación total del mes: ${facturacion}\nTotal de unidades vendidas: {unidadesTotal}\nCostos totales: {costosTotales}\n")


#Funcion2 -> facturacion por producto
"""
- total de facturación por tipo de producto, la cantidad de productos y costo ordenado por facturación
- lista ordenada por facturación
"""
def facturacionTipoProducto(cocinaM1,cocinaM2,cocinaM3,heladeraM1,heladeraM2,heladeraM3,aireM1,aireM2,aireM3,lavarropasM1,lavarropasM2,lavarropasM3,microondasM1,microondasM2,microondasM3,precioCocina,precioHeladera,precioAire,precioLavarropas,precioMicroondas,costoCocina,costoHeladera,costoAire,costoLavarropas,costoMicroondas,unidadesCocina,unidadesHeladera,unidadesAire,unidadesLavarropas,unidadesMicroondas):
    # Calculamos las ventas por producto
    total_cocinaM1 = cocinaM1*precioCocina[0]
    total_cocinaM2 = cocinaM2*precioCocina[1]
    total_cocinaM3 = cocinaM3*precioCocina[2]

    ventasCocina = total_cocinaM1+total_cocinaM2+total_cocinaM3

    total_heladeraM1 = heladeraM1*precioHeladera[0]
    total_heladeraM2 = heladeraM2*precioHeladera[1]
    total_heladeraM3 = heladeraM3*precioHeladera[2]

    ventasHeladera = total_heladeraM1+total_heladeraM2+total_heladeraM3

    total_aireM1 = aireM1*precioAire[0]
    total_aireM2 = aireM2*precioAire[1]
    total_aireM3 = aireM3*precioAire[2]

    ventasAire = total_aireM1+total_aireM2+total_aireM3

    total_lavarropasM1 = lavarropasM1*precioLavarropas[0]
    total_lavarropasM2 = lavarropasM2*precioLavarropas[1]
    total_lavarropasM3 = lavarropasM3*precioLavarropas[2]

    ventasLavarropas = total_lavarropasM1+total_lavarropasM2+total_lavarropasM3

    total_microondasM1 = microondasM1*precioMicroondas[0]
    total_microondasM2 = microondasM2*precioMicroondas[1]
    total_microondasM3 = microondasM3*precioMicroondas[2]

    ventasMicroondas = total_microondasM1+total_microondasM2+total_microondasM3

    # Calculamos los costos por producto
    costos_cocinaM1 = cocinaM1*costoCocina[0]
    costos_cocinaM2 = cocinaM2*costoCocina[1]
    costos_cocinaM3 = cocinaM3*costoCocina[2]

    costosCocinas = costos_cocinaM1 + costos_cocinaM2 + costos_cocinaM3

    costos_heladeraM1 = heladeraM1*costoHeladera[0] 
    costos_heladeraM2 = heladeraM2*costoHeladera[1]
    costos_heladeraM3 = heladeraM3*costoHeladera[2]

    costosHeladeras = costos_heladeraM1 + costos_heladeraM2 + costos_heladeraM3

    costos_aireM1 = aireM1*costoAire[0]
    costos_aireM2 = aireM2*costoAire[1]
    costos_aireM3 = aireM3*costoAire[2]

    costosAires = costos_aireM1 + costos_aireM2 + costos_aireM3

    costos_lavarropasM1 = lavarropasM1*costoLavarropas[0]
    costos_lavarropasM2 = lavarropasM1*costoLavarropas[1]
    costos_lavarropasM3 = lavarropasM1*costoLavarropas[2]

    costosLavarropas = costos_lavarropasM1 + costos_lavarropasM2 + costos_lavarropasM3

    costos_microondasM1 = microondasM1*costoMicroondas[0]
    costos_microondasM2 = microondasM1*costoMicroondas[1]
    costos_microondasM3 = microondasM1*costoMicroondas[2]

    costosMicroondas = costos_microondasM1 + costos_microondasM2 + costos_microondasM3

    # Calculamos la facturación por tipo de producto
    facturacionCocinas = ventasCocina-costosCocinas
    facturacionHeladeras = ventasHeladera-costosHeladeras
    facturacionAires = ventasAire-costosAires
    facturacionLavarropas = ventasLavarropas-costosLavarropas
    facturacionMicroondas = ventasMicroondas-costosMicroondas

    # Armamos una lista para cada tipo de producto, que contenga la facturación, costos totales y la cantidad de unidades vendidas.
    resumenCocinas = [facturacionCocinas,costosCocinas,unidadesCocina,"Cocinas:"]
    resumenHeladeras = [facturacionHeladeras,costosHeladeras,unidadesHeladera,"Heladeras:"]
    resumenAires = [facturacionAires,costosAires,unidadesAire,"Aires acondicionados:"]
    resumenLavarropas = [facturacionLavarropas,costosLavarropas,unidadesLavarropas,"lavarropas"]
    resumenMicroondas = [facturacionMicroondas,costosMicroondas,unidadesMicroondas,"microondas"]

    costosOrdenados=ordenarLista(resumenCocinas,resumenHeladeras,resumenAires,resumenLavarropas,resumenMicroondas)

    print(f"Costos ordenados por facturación:\n{costosOrdenados[0][0]}{costosOrdenados[0][1]}") 
    """
    ADIJAEDLSEFGKLAHGFIUAHGKAJRAWLERWELF
    LKFHAERHURHSEKJFNAKLJFKFBKEBF
    
    """

#Funcion3
"""
- listado completo detallado del total de cada producto y cada modelo con su cantidad y total facturado (ordenado por total facturado)
"""

#Funcion4
"""
- poder seleccionar un tipo de producto y que se detallen la facturación de cada uno de los modelos de ese tipo.
"""

import random

# Variables que representan el stock de cada tipo de producto.
stock_cocina = random.randint(1,2000)
stock_heladera = random.randint(1,2000)
stock_aire = random.randint(1,2000)
stock_lavarropas = random.randint(1,2000)
stock_microondas = random.randint(1,2000)

stock_total = stock_cocina+stock_heladera+stock_aire+stock_lavarropas+stock_microondas

# Variables que representan la cantidad total de unidades vendidas por tipo de producto.
cocina = random.randint(1,stock_cocina)
heladera = random.randint(1,stock_heladera)
aire = random.randint(1,stock_aire)
lavarropas = random.randint(1,stock_lavarropas)
microondas = random.randint(1,stock_microondas)

unidades_total = cocina+heladera+aire+lavarropas+microondas

# En caso de que las ventas no superen el 25% del stock total, se generan nuevamente los datos.
while unidades_total<stock_total*0.25:
    cocina = random.randint(1,stock_cocina)
    heladera = random.randint(1,stock_heladera)
    aire = random.randint(1,stock_aire)
    lavarropas = random.randint(1,stock_lavarropas)
    microondas = random.randint(1,stock_microondas)

    unidades_total = cocina+heladera+aire+lavarropas+microondas

# Variables de las cantidades vendidas por modelo.
cocina_m1 = random.randint(1,cocina)
cocina_m2 = random.randint(1,cocina-cocina_m1)
cocina_m3 = cocina-(cocina_m1+cocina_m2)

heladera_m1 = random.randint(1,heladera)
heladera_m2 = random.randint(1,heladera_m1)
heladera_m3 = heladera-(heladera_m1+heladera_m2)

aire_m1 = random.randint(1,aire)
aire_m2 = random.randint(1,aire-aire_m1)
aire_m3 = aire-(aire_m1+aire_m2)

lavarropas_m1 = random.randint(1,lavarropas)
lavarropas_m2 = random.randint(1,lavarropas-lavarropas_m1)
lavarropas_m3 = lavarropas-(lavarropas_m1+lavarropas_m2)

microondas_m1 = random.randint(1,microondas)
microondas_m2 = random.randint(1,microondas-microondas_m1)
microondas_m3 = microondas-(microondas_m1+microondas_m2)

# Listas que representan los precios de cada modelo. (precio_cocina=[m1,m2,m3])
precio_cocina = [50000,60000,80000]
precio_heladera = [135000,140000,145000]
precio_aire = [200000,300000,400000]
precio_lavarropas = [138000,145000,148000]
precio_microondas = [21000,32000,35000]

# Listas que calculan los costos de cada modelo.
costo_cocina = [(100*precio_cocina[0]/150),(100*precio_cocina[1]/150),(100*precio_cocina[2]/150)]
costo_heladera = [(100*precio_heladera[0]/150),(100*precio_heladera[1]/150),(100*precio_heladera[2]/150)]
costo_aire = [(100*precio_aire[0]/150),(100*precio_aire[1]/150),(100*precio_aire[2]/150)]
costo_lavarropas = [(100*precio_lavarropas[0]/150),(100*precio_lavarropas[1]/150),(100*precio_lavarropas[2]/150)]
costo_microondas = [(100*precio_microondas[0]/150),(100*precio_microondas[1]/150),(100*precio_microondas[2]/150)]

# Constantes que representan los costos para almacenar stock.
ALMACENAMIENTO_COCINA = 500000
ALMACENAMIENTO_HELADERA = 850000
ALMACENAMIENTO_AIRE = 650000
ALMACENAMIENTO_LAVARROPAS = 550000
ALMACENAMIENTO_MICROONDAS = 350000

ALMACENAMIENTO_TOTAL = ALMACENAMIENTO_COCINA+ALMACENAMIENTO_HELADERA+ALMACENAMIENTO_AIRE+ALMACENAMIENTO_LAVARROPAS+ALMACENAMIENTO_MICROONDAS

bandera = True

while bandera:
    boton = int(input("Seleccione una de las opciones:\n1.Resumen de Ventas\n2.Facturación por Producto\n3.Listado Detallado de Facturación\n4.Facturación por Modelo de Producto\n5.SALIR\n\n"))
    if boton == 1:
        llamadoResumen=resumenVentas(cocina_m1,cocina_m2,cocina_m3,heladera_m1,heladera_m2,heladera_m3,aire_m1,aire_m2,aire_m3,lavarropas_m1,lavarropas_m2,lavarropas_m3,microondas_m1,microondas_m2,microondas_m3,precio_cocina,precio_heladera,precio_aire,precio_lavarropas,precio_microondas,unidades_total,costo_cocina,costo_heladera,costo_aire,costo_lavarropas,costo_microondas,ALMACENAMIENTO_TOTAL)
    elif boton == 2:
        llamadoFacturacionTipoProducto=facturacionTipoProducto(cocina_m1,cocina_m2,cocina_m3,heladera_m1,heladera_m2,heladera_m3,aire_m1,aire_m2,aire_m3,lavarropas_m1,lavarropas_m2,lavarropas_m3,microondas_m1,microondas_m2,microondas_m3,precio_cocina,precio_heladera,precio_aire,precio_lavarropas,precio_microondas,costo_cocina,costo_heladera,costo_aire,costo_lavarropas,costo_microondas,cocina,heladera,aire,lavarropas,microondas)
    elif boton == 3:
        print()
    elif boton == 4:
        print()
    elif boton == 5:
        bandera = False
    else:
        print("\nLa opción ingresada no existe.")
        boton = int(input("Seleccione una de las opciones:\n1.Resumen de Ventas\n2.Facturación por Producto\n3.Listado Detallado de Facturación\n4.Facturación por Modelo de Producto\n5.SALIR\n"))


