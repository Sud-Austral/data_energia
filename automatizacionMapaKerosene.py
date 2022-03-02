import pandas as pd
import codecs
import json
import requests
import datetime

def descarga():
    api_auth = "o6TXnCxKRtkI4oMY1ayi8MtZRDBYE1GVoezyURQO"
    url = 'https://api.desarrolladores.energiaabierta.cl/calefaccion-en-linea/v1/kerosene.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    decoded_data=codecs.decode(response.content, 'utf-8-sig')
    d = json.loads(decoded_data, strict=False)

    result = d
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    
    clearFloat(df)
    
    return df

def string_to_float(cadena):
    
    try:
        return float(cadena)
    except:
        return None

def clearFloat(df):
    clasificacion = ['precios.kerosene']
    
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
    
    clasificacion = ['precios.kerosene']

    for i in clasificacion:

        getTramos(df, i)
    
    createFile(df)

def createFile(df):

    salida = []

    df = df[df['id'] != 'pb520101']
    df = df[df['id'] != 'pb520102']

    for i in range(len(df)):

        filasJSON = json.loads(df.iloc[i].to_json(orient='index', force_ascii=False))

        filasJSON['razon'] = filasJSON['razon_social']
        filasJSON['calle'] = filasJSON['direccion_calle']
        filasJSON['numero'] = filasJSON['direccion_numero']
        filasJSON['comuna'] = filasJSON['nombre_comuna']
        filasJSON['region'] = filasJSON['nombre_region']
        filasJSON['horario'] = filasJSON['fecha_hora_actualizacion']
        filasJSON['distribucion'] = filasJSON['distribuidor.nombre']
        filasJSON['logo'] = filasJSON['distribuidor.logo']
        filasJSON['kerosene'] = filasJSON['precios.kerosene']

        filasJSON['ID_COM'] = int(filasJSON['id_comuna'])
        
        deleteCols = ['id', 'fecha_hora_actualizacion', 'razon_social', 'direccion_calle','direccion_numero', 'id_comuna', 'nombre_comuna', 'id_region','nombre_region', 'horario_atencion', 'distribuidor.nombre','distribuidor.logo', 'distribuidor.logo_svg','distribuidor.logo_horizontal_svg', 'precios.kerosene','metodos_de_pago.efectivo', 'metodos_de_pago.cheque','metodos_de_pago.tarjetas bancarias','metodos_de_pago.tarjetas grandes tiendas', 'servicios.tienda', 'servicios.farmacia','servicios.mantencion', 'servicios.autoservicio']
        
        for i in deleteCols:
            
            del filasJSON[i]



        salida2 = {"type": "Feature","geometry": {"type": "Point","coordinates": [filasJSON['ubicacion.longitud'], filasJSON['ubicacion.latitud']]},"properties": filasJSON}
        # print(salida2)

        salida.append(salida2.copy())
        
    
    jsonFinal = {"type": "FeatureCollection", "features": salida}

    with open('mapa_kerosene/chile/kerosene.json', 'w', encoding='utf8') as myfile:
        json.dump(jsonFinal, myfile, ensure_ascii=False)
    
    print("Keroseke creado correctamente.")
    historico(df)
    
def historico(df):
    hoy = str(datetime.datetime.today())[0:10]
    df.to_csv('historico_kerosene/' + str(hoy) + '.csv', index=False)
    
    print("Histórico creado correctamente.")

if __name__ == '__main__':
    descarga()