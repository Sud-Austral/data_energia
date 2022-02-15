import pandas as pd
import codecs
import json
import requests
import datetime


def descarga():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    decoded_data=codecs.decode(response.content, 'utf-8-sig')
    d = json.loads(decoded_data, strict=False)

    result = d
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    
    clearFloat(df)


def string_to_float(cadena):
    
    try:
        return float(cadena)
    except:
        return None


def clearFloat(df):
    clasificacion = ['Gasolina 93 $/L', 'Gasolina 97 $/L', 'Petróleo Diesel $/L', 'Gasolina 95 $/L', 'GLP Vehicular $/m3', 'GNC $/m3']
    
    for i in clasificacion:

        df[i] = df[i].apply(string_to_float)
     
    clasificacionTabla(df)


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

def clasificacionTabla(df):
    
    clasificacion = ['Gasolina 93 $/L', 'Gasolina 97 $/L', 'Petróleo Diesel $/L', 'Gasolina 95 $/L', 'GLP Vehicular $/m3', 'GNC $/m3']

    for i in clasificacion:

        getTramos(df, i)
    
    createFile(df) 


def createFile(df):

    salida = []

    df = df[df['ID'] != 'pb520101']
    df = df[df['ID'] != 'pb520102']

    for i in range(len(df)):

        filasJSON = json.loads(df.iloc[i].to_json(orient='index', force_ascii=False))

        filasJSON['razon'] = filasJSON['Razón Social']
        filasJSON['calle'] = filasJSON['Calle']
        filasJSON['numero'] = filasJSON['Número']
        filasJSON['comuna'] = filasJSON['Comuna']
        filasJSON['region'] = filasJSON['Región']
        filasJSON['horario'] = filasJSON['Horario de Atención']
        filasJSON['distribucion'] = filasJSON['Distribuidor']
        filasJSON['logo'] = filasJSON['Distribuidor Logo SVG']
        filasJSON['G93'] = filasJSON['Gasolina 93 $/L']
        filasJSON['G97'] = filasJSON['Gasolina 97 $/L']
        filasJSON['petroleo'] = filasJSON['Petróleo Diesel $/L']
        filasJSON['G95'] = filasJSON['Gasolina 95 $/L']
        filasJSON['GLP'] = filasJSON['GLP Vehicular $/m3']
        filasJSON['GNC'] = filasJSON['GNC $/m3']
        filasJSON['class93'] = filasJSON['ClasificacionGasolina 93 $/L']
        filasJSON['class95'] = filasJSON['ClasificacionGasolina 95 $/L']
        filasJSON['class97'] = filasJSON['ClasificacionGasolina 97 $/L']
        filasJSON['classGLP'] = filasJSON['ClasificacionGLP Vehicular $/m3']
        filasJSON['classGNC'] = filasJSON['ClasificacionGNC $/m3']
        filasJSON['classD'] = filasJSON['ClasificacionPetróleo Diesel $/L']

        del filasJSON['Razón Social']
        del filasJSON['Calle']
        del filasJSON['Número']
        del filasJSON['Comuna']
        del filasJSON['Región']
        del filasJSON['Horario de Atención']
        del filasJSON['Distribuidor']
        del filasJSON['Distribuidor Logo SVG']
        del filasJSON['Gasolina 93 $/L']
        del filasJSON['Gasolina 97 $/L']
        del filasJSON['Petróleo Diesel $/L']
        del filasJSON['Gasolina 95 $/L']
        del filasJSON['GLP Vehicular $/m3']
        del filasJSON['GNC $/m3']
        del filasJSON['ClasificacionGasolina 93 $/L']
        del filasJSON['ClasificacionGasolina 95 $/L']
        del filasJSON['ClasificacionGasolina 97 $/L']
        del filasJSON['ClasificacionGLP Vehicular $/m3']
        del filasJSON['ClasificacionGNC $/m3']
        del filasJSON['ClasificacionPetróleo Diesel $/L']

        del filasJSON['ID']
        # del filasJSON['ID Comuna']
        del filasJSON['ID Región']
        del filasJSON['Distribuidor Logo']
        del filasJSON['Distribuidor Logo SVG Horizontal']
        del filasJSON['Tienda']
        del filasJSON['Farmacia']
        del filasJSON['Mantención']
        del filasJSON['Autoservicio']
        del filasJSON['Pago Efectivo']
        del filasJSON['Cheque']
        del filasJSON['Tarjetas Bancarias']
        del filasJSON['Tarjeta Grandes Tiendas']


        salida2 = {"type": "Feature","geometry": {"type": "Point","coordinates": [filasJSON['Longitud'], filasJSON['Latitud']]},"properties": filasJSON}
        # print(salida2)

        salida.append(salida2.copy())

    jsonFinal = {"type": "FeatureCollection", "features": salida}

    with open('mapa/chile/combustibles.json', 'w', encoding='utf8') as myfile:
        json.dump(jsonFinal, myfile, ensure_ascii=False)
    
    print("Estaciones de combustible creado correctamente.")
    historico(df)
    
    print("Histórico creado correctamente.")

def historico(df):
    hoy = str(datetime.datetime.today())[0:10]
    df.to_csv('historico/' + str(hoy) + '.csv', index=False)


if __name__ == '__main__':
    descarga()