import pandas as pd
import codecs
import json

def getTramos(df, variable):
    
    dfAux = df

    dfAux = dfAux[dfAux[variable] < df[variable].std() + df[variable].mean()]
    dfAux = dfAux[dfAux[variable] > df[variable].mean() - df[variable].std()]

    maximo = dfAux[variable].max()
    minimo = dfAux[variable].min()
    
    rango = (maximo - minimo) / 4
    
    def setTramos(x):
        
        if(x >= maximo - rango):
            return 'Alto'
        
        if(x >= maximo - rango * 2 and x < maximo - rango):
            return 'Medio alto'
        
        if(x >= maximo - rango * 3 and x < maximo - rango * 2):
            return 'Medio bajo'
                
        if(x <= maximo - rango * 3):
            return 'Bajo'
        
        return 'Sin valor'
        
    df['Clasificacion' + str(variable)] = df[variable].apply(setTramos)
    
    return

def clear(texto):
    
    finalText = texto.replace("'", "").replace("´", "").replace("´", "").replace("’", "")
    return finalText

def upgradePoints(dfAux):
    
    df = dfAux
    
    salida1 = 'puntos = {"type": "FeatureCollection","features": ['
    salida3 = ']}'

    data = []

    for i,j in df.iterrows():

        lat = df["Latitud"][i]
        lng = df["Longitud"][i]

        RAZON_SOCIAL = clear(str(df["Razón Social"][i]))
        CALLE = clear(str(df["Calle"][i]))
        NUMERO = df["Número"][i]
        COMUNA = clear(str(df["Comuna"][i]))
        REGION = clear(str(df["Región"][i]))
        HORARIO_ATENCION = clear(str(df["Horario de Atención"][i]))
        DISTRIBUIDOR = clear(str(df["Distribuidor"][i]))
        D_LOGO_SVG = df["Distribuidor Logo SVG"][i]
        G93 = df["Gasolina 93 $/L"][i]
        G97 = df["Gasolina 97 $/L"][i]
        PETROLEO = df["Petróleo Diesel $/L"][i]
        G95 = df["Gasolina 95 $/L"][i]
        GLP = df["GLP Vehicular $/m3"][i]
        GNC = df["GNC $/m3"][i]
        class93 = df['ClasificacionGasolina 93 $/L'][i]
        class95 = df['ClasificacionGasolina 95 $/L'][i]
        class97 = df['ClasificacionGasolina 97 $/L'][i]
        classGLP = df['ClasificacionGLP Vehicular $/m3'][i]
        classGNC = df['ClasificacionGNC $/m3'][i]
        classD = df['ClasificacionPetróleo Diesel $/L'][i]

        salida2 = '{"type": "Feature","geometry": {"type": "Point","coordinates": [' + str(lng) + ',' + str(lat) + ']},"properties": {"razon": "' + str(RAZON_SOCIAL) + '", "calle": "' + str(CALLE) + '", "numero": "' + str(NUMERO) + '", "comuna": "' + str(COMUNA) + '", "region": "' + str(REGION) + '", "horario": "' + str(HORARIO_ATENCION) + '", "distribucion": "' + str(DISTRIBUIDOR) + '", "logo": "' + str(D_LOGO_SVG) + '", "G93": "' + str(G93) + '", "G97": "' + str(G97) + '", "petroleo": "' + str(PETROLEO) + '", "G95": "' + str(G95) + '", "GLP": "' + str(GLP) + '", "GNC": "' + str(GNC) + '", "class93": "' + str(class93) + '", "class95": "' + str(class95) + '", "class97": "' + str(class97) + '", "classGLP": "' + str(classGLP) + '", "classGNC": "' + str(classGNC) + '", "classD": "' + str(classD) + '"}}'
        data.append(salida2)

    salida = (salida1 + str(data).replace("'", "").replace("[{", "{").replace("}}]", "}}") + salida3)
    # print(salida)

    with codecs.open('mapa/chile/establecimientos.js', 'w', 'utf-8') as file:
        file.write(salida)
        
    print("Puntos actualizados")


def establecimientos():
    df = pd.read_excel('combustibles_vehicular_estaciones.xlsx')
    
    # df = df.head(50)

    df = df[df['ID'] != 'pb520101']
    df = df[df['ID'] != 'pb520102']

    clasificacion = ['Gasolina 93 $/L', 'Gasolina 97 $/L', 'Petróleo Diesel $/L', 'Gasolina 95 $/L', 'GLP Vehicular $/m3', 'GNC $/m3']

    for i in clasificacion:

        getTramos(df, i)

    upgradePoints(df)


if __name__ == '__main__':
    establecimientos()