import random

#Objetivo de la funcion: Ordenar listas en base a un valor especificó de las mismas
#Parametros de entrada: Listas con los valores de facturacion, unidades vendidas, costos e identificacion de producto
#Parametros de salida: Matriz ordenas con los costos y el identificador
"""
def ordenarLista(matrizResumenes,origen):
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(matrizResumenes)-1):
            if origen == "costos":
                if matrizResumenes[i][0] > matrizResumenes[i+1][0]:
                    aux = matrizResumenes[i][0]
                    matrizResumenes[i][0] = matrizResumenes[i+1][0]
                    matrizResumenes[i+1][0] = aux

                    aux2 = matrizResumenes[i][3]
                    matrizResumenes[i][3] = matrizResumenes[i+1][3]
                    matrizResumenes[i+1][3] = aux2

                    desordenada = True
            else:
                if matrizResumenes[i][0] > matrizResumenes[i+1][0]:
                    aux = matrizResumenes[i][0]
                    matrizResumenes[i][0] = matrizResumenes[i+1][0]
                    matrizResumenes[i+1][0] = aux

                    aux2 = matrizResumenes[i][3]
                    matrizResumenes[i][3] = matrizResumenes[i+1][3]
                    matrizResumenes[i+1][3] = aux2

                    aux3 = matrizResumenes[i][2]
                    matrizResumenes[i][2] = matrizResumenes[i+1][2]
                    matrizResumenes[i+1][2] = aux3

                    desordenada = True

    listaA = [0,0,0]
    listaB = [0,0,0]
    listaC = [0,0,0]
    listaD = [0,0,0]
    listaE = [0,0,0]

    matrizOrdenada = [listaA,listaB,listaC,listaD,listaE]
    if origen == "costos":

        for i in range(len(matrizResumenes)):
            matrizOrdenada[i][0]=matrizResumenes[i][3]
            matrizOrdenada[i][1]=matrizResumenes[i][1]
    else:
        for i in range(len(matrizResumenes)):
            matrizOrdenada[i][0]=matrizResumenes[i][3]
            matrizOrdenada[i][1]=matrizResumenes[i][0]
            matrizOrdenada[i][2]=matrizResumenes[i][2]
    
    return matrizOrdenada"""
def ordenarLista(matrizResumenes):
    desordenada = True
    print(matrizResumenes)
    while desordenada:
        desordenada = False
        for i in range(len(matrizResumenes)-1):
            
                if matrizResumenes[i][0] > matrizResumenes[i+1][0]:
                    aux = matrizResumenes[i][0]
                    matrizResumenes[i][0] = matrizResumenes[i+1][0]
                    matrizResumenes[i+1][0] = aux

                    aux2 = matrizResumenes[i][3]
                    matrizResumenes[i][3] = matrizResumenes[i+1][3]
                    matrizResumenes[i+1][3] = aux2

                    aux3 = matrizResumenes[i][2]
                    matrizResumenes[i][2] = matrizResumenes[i+1][2]
                    matrizResumenes[i+1][2] = aux3

                    desordenada = True
    print(matrizResumenes)
    listaA = [0,0,0]
    listaB = [0,0,0]
    listaC = [0,0,0]
    listaD = [0,0,0]
    listaE = [0,0,0]

    matrizOrdenada = [listaA,listaB,listaC,listaD,listaE]
    for i in range(len(matrizResumenes)):
            matrizOrdenada[i][0]=matrizResumenes[i][3]
            matrizOrdenada[i][1]=matrizResumenes[i][0]
            matrizOrdenada[i][2]=matrizResumenes[i][2]
    
    return matrizOrdenada

#Funcion1 -> Resumen de Ventas

#Objetivo de la funcion: mostrarle al usuario la facturacion del mes, cuantos articulos se vendieron y cual fue el costo total
#Parametros de entrada: Recibe: Recibe los precios de cada producto, los costos de cada produto y las unidades vendidas
#Parametros de salida: Facturación mensual

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
    costos_lavarropasM2 = lavarropasM2*costoLavarropas[1]
    costos_lavarropasM3 = lavarropasM3*costoLavarropas[2]

    costos_microondasM1 = microondasM1*costoMicroondas[0]
    costos_microondasM2 = microondasM2*costoMicroondas[1]
    costos_microondasM3 = microondasM3*costoMicroondas[2]

    costosTotales = costos_cocinaM1 + costos_cocinaM2 + costos_cocinaM3 + costos_heladeraM1 + costos_heladeraM2 + costos_heladeraM3 + costos_aireM1 + costos_aireM2 + costos_aireM3 + costos_lavarropasM1 + costos_lavarropasM2 + costos_lavarropasM3 + costos_microondasM1 + costos_microondasM2 + costos_microondasM3 + almacenamientoTotal

    # Facturación total del mes:
    facturacion = ventasTotales-costosTotales

    print(f"\nFacturación total del mes: ${facturacion}\nTotal de unidades vendidas: {unidadesTotal}\nCostos totales: ${costosTotales}\n")


#Funcion2 -> facturacion por producto

#Objetivo de la funcion: mostrarle al usuario la facturacion de todos los productos y el costo de los productos
#Parametros de entrada: Recibe los precios de cada producto, los costos de cada produto y las unidades vendidas
#Parametros de salida: Facturación de cada producto y modelo

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
    costos_lavarropasM2 = lavarropasM2*costoLavarropas[1]
    costos_lavarropasM3 = lavarropasM3*costoLavarropas[2]

    costosLavarropas = costos_lavarropasM1 + costos_lavarropasM2 + costos_lavarropasM3

    costos_microondasM1 = microondasM1*costoMicroondas[0]
    costos_microondasM2 = microondasM2*costoMicroondas[1]
    costos_microondasM3 = microondasM3*costoMicroondas[2]

    costosMicroondas = costos_microondasM1 + costos_microondasM2 + costos_microondasM3

    # Calculamos la facturación por tipo de producto
    facturacionCocinas = ventasCocina-costosCocinas
    facturacionHeladeras = ventasHeladera-costosHeladeras
    facturacionAires = ventasAire-costosAires
    facturacionLavarropas = ventasLavarropas-costosLavarropas
    facturacionMicroondas = ventasMicroondas-costosMicroondas

    # Armamos una lista para cada tipo de producto, que contenga la facturación, costos totales y la cantidad de unidades vendidas.
    resumenCocinas = [facturacionCocinas,costosCocinas,unidadesCocina,"Cocinas: $"]
    resumenHeladeras = [facturacionHeladeras,costosHeladeras,unidadesHeladera,"Heladeras: $"]
    resumenAires = [facturacionAires,costosAires,unidadesAire,"Aires acondicionados: $"]
    resumenLavarropas = [facturacionLavarropas,costosLavarropas,unidadesLavarropas,"Lavarropas: $"]
    resumenMicroondas = [facturacionMicroondas,costosMicroondas,unidadesMicroondas,"Microondas: $"]

    matrizResumenes=(resumenCocinas,resumenHeladeras,resumenAires,resumenLavarropas,resumenMicroondas)
    costosOrdenados=ordenarLista(matrizResumenes)

    print(f"\nTotal de Facturación:\nCocinas: ${facturacionCocinas}\nUnidades: {unidadesCocina}\n\nHeladeras: ${facturacionHeladeras}\nUnidades: {unidadesHeladera}\n\nAires Acondicionados: ${facturacionAires}\nUnidades: {unidadesAire}\n\nLavarropas: ${facturacionLavarropas}\nUnidades: {unidadesLavarropas}\n\nMicroondas: ${facturacionMicroondas}\nUnidades: {unidadesMicroondas}")
    print(f"\nCostos ordenados por facturación:\n\n{costosOrdenados[0][0]}{costosOrdenados[0][1]}\n{costosOrdenados[1][0]}{costosOrdenados[1][1]}\n{costosOrdenados[2][0]}{costosOrdenados[2][1]}\n{costosOrdenados[3][0]}{costosOrdenados[3][1]}\n{costosOrdenados[4][0]}{costosOrdenados[4][1]}\n") 


#Funcion 3
#Objetivo de la funcion: mostrarle al usuario la facturacion de cada producto y de cada modelo, ademas de las unidades vendidas y los costos
#Parametros de entrada: Recibe: Recibe los precios de cada producto, los costos de cada produto y las unidades vendidas
#Parametros de salida: Facturación de cada modelo de producto

def listadoFacturacion(cocinaM1,cocinaM2,cocinaM3,heladeraM1,heladeraM2,heladeraM3,aireM1,aireM2,aireM3,lavarropasM1,lavarropasM2,lavarropasM3,microondasM1,microondasM2,microondasM3,precioCocina,precioHeladera,precioAire,precioLavarropas,precioMicroondas,costoCocina,costoHeladera,costoAire,costoLavarropas,costoMicroondas):
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
    costos_lavarropasM2 = lavarropasM2*costoLavarropas[1]
    costos_lavarropasM3 = lavarropasM3*costoLavarropas[2]

    costosLavarropas = costos_lavarropasM1 + costos_lavarropasM2 + costos_lavarropasM3

    costos_microondasM1 = microondasM1*costoMicroondas[0]
    costos_microondasM2 = microondasM2*costoMicroondas[1]
    costos_microondasM3 = microondasM3*costoMicroondas[2]

    costosMicroondas = costos_microondasM1 + costos_microondasM2 + costos_microondasM3

    # Calculamos la facturación por tipo de producto
    facturacionCocinas = ventasCocina-costosCocinas
    facturacionHeladeras = ventasHeladera-costosHeladeras
    facturacionAires = ventasAire-costosAires
    facturacionLavarropas = ventasLavarropas-costosLavarropas
    facturacionMicroondas = ventasMicroondas-costosMicroondas


    # Calculamos la facturación por modelo
    facturacionCocinasM1 = total_cocinaM1-costos_cocinaM1
    facturacionCocinasM2 = total_cocinaM2-costos_cocinaM2
    facturacionCocinasM3 = total_cocinaM3-costos_cocinaM3

    facturacionHeladerasM1 = total_heladeraM1-costos_heladeraM1
    facturacionHeladerasM2 = total_heladeraM2-costos_heladeraM2
    facturacionHeladerasM3 = total_heladeraM3-costos_heladeraM3

    facturacionAiresM1 = total_aireM1-costos_aireM1
    facturacionAiresM2 = total_aireM2-costos_aireM2
    facturacionAiresM3 = total_aireM3-costos_aireM3

    facturacionLavarropasM1 = total_lavarropasM1-costos_lavarropasM1
    facturacionLavarropasM2 = total_lavarropasM2-costos_lavarropasM2
    facturacionLavarropasM3 = total_lavarropasM3-costos_lavarropasM3

    facturacionMicroondasM1 = total_microondasM1-costos_microondasM1
    facturacionMicroondasM2 = total_microondasM2-costos_microondasM2
    facturacionMicroondasM3 = total_microondasM3-costos_microondasM3

    # Armamos una lista para cada modelo, que contenga la facturación y el modelo
    
    

    cocinasOrdenadasM1 = [facturacionCocinasM1,facturacionCocinasM1,cocinaM1,"Modelo 1: $"]
    cocinasOrdenadasM2 = [facturacionCocinasM2,facturacionCocinasM2,cocinaM2,"Modelo 2: $"]
    cocinasOrdenadasM3 = [facturacionCocinasM3,facturacionCocinasM3,cocinaM3,"Modelo 3: $"]

    matrizCocinasOrdenadas=[cocinasOrdenadasM1,cocinasOrdenadasM2,cocinasOrdenadasM3]
    cocinasOrdenadas = ordenarLista(matrizCocinasOrdenadas)

    heladerasOrdenadasM1 = [facturacionHeladerasM1,facturacionHeladerasM1,heladeraM1,"Modelo 1: $"]
    heladerasOrdenadasM2 = [facturacionHeladerasM2,facturacionHeladerasM2,heladeraM2,"Modelo 2: $"]
    heladerasOrdenadasM3 = [facturacionHeladerasM3,facturacionHeladerasM3,heladeraM3,"Modelo 3: $"]

    matrizHeladerasOrdenadas=[heladerasOrdenadasM1,heladerasOrdenadasM2,heladerasOrdenadasM3]
    heladerasOrdenadas=ordenarLista(matrizHeladerasOrdenadas)
    
    airesOrdenadosM1 = [facturacionAiresM1,facturacionAiresM1,aireM1,"Modelo 1: $"]
    airesOrdenadosM2 = [facturacionAiresM2,facturacionAiresM2,aireM2,"Modelo 2: $"]
    airesOrdenadosM3 = [facturacionAiresM3,facturacionAiresM3,aireM3,"Modelo 3: $"]

    matrizAiresOrdenados=[airesOrdenadosM1,airesOrdenadosM2,airesOrdenadosM3]
    airesOrdenados=ordenarLista(matrizAiresOrdenados)

    lavarropasOrdenadosM1 = [facturacionLavarropasM1,facturacionLavarropasM1,lavarropasM1,"Modelo 1: $"]
    lavarropasOrdenadosM2 = [facturacionLavarropasM2,facturacionLavarropasM2,lavarropasM2,"Modelo 2: $"]
    lavarropasOrdenadosM3 = [facturacionLavarropasM3,facturacionLavarropasM3,lavarropasM3,"Modelo 3: $"]

    matrizLavarropasOrdenados=[lavarropasOrdenadosM1,lavarropasOrdenadosM2,lavarropasOrdenadosM3]
    lavarropasOrdenados=ordenarLista(matrizLavarropasOrdenados)

    microondasOrdenadosM1 = [facturacionMicroondasM1,facturacionMicroondasM1,microondasM1,"Modelo 1: $"]
    microondasOrdenadosM2 = [facturacionMicroondasM2,facturacionMicroondasM2,microondasM2,"Modelo 2: $"]
    microondasOrdenadosM3 = [facturacionMicroondasM3,facturacionMicroondasM3,microondasM3,"Modelo 3: $"]

    matrizMicroondasOrdenados=[microondasOrdenadosM1,microondasOrdenadosM2,microondasOrdenadosM3]
    microondasOrdenados=ordenarLista(matrizMicroondasOrdenados)

    print(f"\nListado Completo de Facturación:\n(Modelos ordenados de menor a mayor según su facturación)\n\nCocinas: ${facturacionCocinas}\n\n{cocinasOrdenadas[0][0]}{cocinasOrdenadas[0][1]}\nUnidades Vendidas: {cocinasOrdenadas[0][2]}\n\n{cocinasOrdenadas[1][0]}{cocinasOrdenadas[1][1]}\nUnidades Vendidas: {cocinasOrdenadas[1][2]}\n\n{cocinasOrdenadas[2][0]}{cocinasOrdenadas[2][1]}\nUnidades Vendidas: {cocinasOrdenadas[2][2]}\n\nHeladeras: {facturacionHeladeras}\n\n{heladerasOrdenadas[0][0]}{heladerasOrdenadas[0][1]}\nUnidades Vendidas: {heladerasOrdenadas[0][2]}\n\n{heladerasOrdenadas[1][0]}{heladerasOrdenadas[1][1]}\nUnidades Vendidas: {heladerasOrdenadas[1][2]}\n\n{heladerasOrdenadas[2][0]}{heladerasOrdenadas[2][1]}\nUnidades Vendidas: {heladerasOrdenadas[2][2]}\n\nAires Acondicionados: ${facturacionAires}\n\n{airesOrdenados[0][0]}{airesOrdenados[0][1]}\nUnidades Vendidas: {airesOrdenados[0][2]}\n\n{airesOrdenados[1][0]}{airesOrdenados[1][1]}\nUnidades Vendidas: {airesOrdenados[1][2]}\n\n{airesOrdenados[2][0]}{airesOrdenados[2][1]}\nUnidades Vendidas: {airesOrdenados[2][2]}\n\nLavarropas: ${facturacionLavarropas}\n\n{lavarropasOrdenados[0][0]}{lavarropasOrdenados[0][1]}\nUnidades Vendidas: {lavarropasOrdenados[0][2]}\n\n{lavarropasOrdenados[1][0]}{lavarropasOrdenados[1][1]}\nUnidades Vendidas: {lavarropasOrdenados[1][2]}\n\n{lavarropasOrdenados[2][0]}{lavarropasOrdenados[2][1]}\nUnidades Vendidas: {lavarropasOrdenados[2][2]}\n\nMicroondas: ${facturacionMicroondas}\n\n{microondasOrdenados[0][0]}{microondasOrdenados[0][1]}\nUnidades Vendidas: {microondasOrdenados[0][2]}\n\n{microondasOrdenados[1][0]}{microondasOrdenados[1][1]}\nUnidades Vendidas: {microondasOrdenados[1][2]}\n\n{microondasOrdenados[2][0]}{microondasOrdenados[2][1]}\nUnidades Vendidas: {microondasOrdenados[2][2]}\n")

#Funcion 4
#Objetivo de la funcion: mostrarle al usuario la facturacion del modelo de producto que selecciono
#Parametros de entrada: Recibe: el producto y modelo que eligio el usuario y la facturacion de cada modelo de cada productos
#Parametros de salida: Facturación del modelo seleccionado

def elegirModeloFacturacion(producto,modelo,cocinaM1,cocinaM2,cocinaM3,heladeraM1,heladeraM2,heladeraM3,aireM1,aireM2,aireM3,lavarropasM1,lavarropasM2,lavarropasM3,microondasM1,microondasM2,microondasM3,precioCocina,precioHeladera,precioAire,precioLavarropas,precioMicroondas,costoCocina,costoHeladera,costoAire,costoLavarropas,costoMicroondas):
    # Calculamos los ingresos por las ventas
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

    # Calculamos los costos por producto
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
    costos_lavarropasM2 = lavarropasM2*costoLavarropas[1]
    costos_lavarropasM3 = lavarropasM3*costoLavarropas[2]

    costos_microondasM1 = microondasM1*costoMicroondas[0]
    costos_microondasM2 = microondasM2*costoMicroondas[1]
    costos_microondasM3 = microondasM3*costoMicroondas[2]

    # Calculamos la facturación por modelo
    facturacionCocinasM1 = total_cocinaM1-costos_cocinaM1
    facturacionCocinasM2 = total_cocinaM2-costos_cocinaM2
    facturacionCocinasM3 = total_cocinaM3-costos_cocinaM3

    facturacionHeladerasM1 = total_heladeraM1-costos_heladeraM1
    facturacionHeladerasM2 = total_heladeraM2-costos_heladeraM2
    facturacionHeladerasM3 = total_heladeraM3-costos_heladeraM3

    facturacionAiresM1 = total_aireM1-costos_aireM1
    facturacionAiresM2 = total_aireM2-costos_aireM2
    facturacionAiresM3 = total_aireM3-costos_aireM3

    facturacionLavarropasM1 = total_lavarropasM1-costos_lavarropasM1
    facturacionLavarropasM2 = total_lavarropasM2-costos_lavarropasM2
    facturacionLavarropasM3 = total_lavarropasM3-costos_lavarropasM3

    facturacionMicroondasM1 = total_microondasM1-costos_microondasM1
    facturacionMicroondasM2 = total_microondasM2-costos_microondasM2
    facturacionMicroondasM3 = total_microondasM3-costos_microondasM3
    
    if producto == 1:
        if modelo == 1:
            print(f"\nFacturación: ${facturacionCocinasM1}\n")
        elif modelo == 2:
            print(f"\nFacturación: ${facturacionCocinasM2}\n")
        else:
            print(f"\nFacturación: ${facturacionCocinasM3}\n")
    elif producto == 2:
        if modelo == 1:
            print(f"\nFacturación: ${facturacionHeladerasM1}\n")
        elif modelo == 2:
            print(f"\nFacturación: ${facturacionHeladerasM2}\n")
        else:
            print(f"\nFacturación: ${facturacionHeladerasM3}\n")
    elif producto == 3:
        if modelo == 1:
            print(f"\nFacturación: ${facturacionAiresM1}\n")
        elif modelo == 2:
            print(f"\nFacturación: ${facturacionAiresM2}\n")
        else:
            print(f"\nFacturación: ${facturacionAiresM3}\n")
    elif producto == 4:
        if modelo == 1:
            print(f"\nFacturación: ${facturacionLavarropasM1}\n")
        elif modelo == 2:
            print(f"\nFacturación: ${facturacionLavarropasM2}\n")
        else:
            print(f"\nFacturación: ${facturacionLavarropasM3}\n")
    else:
        if modelo == 1:
            print(f"\nFacturación: ${facturacionMicroondasM1}\n")
        elif modelo == 2:
            print(f"\nFacturación: ${facturacionMicroondasM2}\n")
        else:
            print(f"\nFacturación: ${facturacionMicroondasM3}\n")


#PROGRAMA PRINCIPAL

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
heladera_m2 = random.randint(1,heladera-heladera_m1)
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
        llamadoListadoFacturacion=listadoFacturacion(cocina_m1,cocina_m2,cocina_m3,heladera_m1,heladera_m2,heladera_m3,aire_m1,aire_m2,aire_m3,lavarropas_m1,lavarropas_m2,lavarropas_m3,microondas_m1,microondas_m2,microondas_m3,precio_cocina,precio_heladera,precio_aire,precio_lavarropas,precio_microondas,costo_cocina,costo_heladera,costo_aire,costo_lavarropas,costo_microondas)
    elif boton == 4:
        elegirProducto = int(input("\nSeleccione un producto:\n1.Cocina\n2.Heladera\n3.Aire Acondicionado\n4.Lavarropas\n5.Microondas\n\n"))
        while elegirProducto < 1 or elegirProducto > 5:
            print("\nLa opcion ingresada es incorrecta.")
            elegirProducto = int(input("\nSeleccione un producto:\n1.Cocina\n2.Heladera\n3.Aire Acondicionado\n4.Lavarropas\n5.Microondas\n\n"))
        if elegirProducto == 1:
            elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
            while elegirModelo < 1 or elegirModelo > 3:
                print("La opción ingresada es incorrecta.")
                elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
        elif elegirProducto == 2:
            elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
            while elegirModelo < 1 or elegirModelo > 3:
                print("La opción ingresada es incorrecta.")
                elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
        elif elegirProducto == 3:
            elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
            while elegirModelo < 1 or elegirModelo > 3:
                print("La opción ingresada es incorrecta.")
                elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
        elif elegirProducto == 4:
            elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
            while elegirModelo < 1 or elegirModelo > 3:
                print("La opción ingresada es incorrecta.")
                elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
        else:
            elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
            while elegirModelo < 1 or elegirModelo > 3:
                print("La opción ingresada es incorrecta.")
                elegirModelo = int(input("\nSeleccione el modelo:\n1.Modelo 1\n2.Modelo 2\n3.Modelo 3\n\n"))
        elegirFacturacion = elegirModeloFacturacion(elegirProducto,elegirModelo,cocina_m1,cocina_m2,cocina_m3,heladera_m1,heladera_m2,heladera_m3,aire_m1,aire_m2,aire_m3,lavarropas_m1,lavarropas_m2,lavarropas_m3,microondas_m1,microondas_m2,microondas_m3,precio_cocina,precio_heladera,precio_aire,precio_lavarropas,precio_microondas,costo_cocina,costo_heladera,costo_aire,costo_lavarropas,costo_microondas)
    elif boton == 5:
        bandera = False
    else:
        print("\nLa opción ingresada no existe.")
        boton = int(input("Seleccione una de las opciones:\n1.Resumen de Ventas\n2.Facturación por Producto\n3.Listado Detallado de Facturación\n4.Facturación por Modelo de Producto\n5.SALIR\n"))
