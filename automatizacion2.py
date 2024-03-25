import requests as req
import json
import pandas as pd
import sys
import datetime

#BENCINA EN LÍNEA:

def changeToNumber(number):
    try:
        number = number.replace(",",".")
        return float(number)
    except:
        return number

def proceso():
    url = 'https://3b9x.short.gy/xAW5bI'

    file = req.get(url, allow_redirects=True)
    open('data.csv', 'wb').write(file.content)
    df = pd.read_csv("data.csv", sep=";")
    newNames = {'id':'ID', 'fecha_actualizacion':'Última Actualización', 'razon_social':"Razón Social", 
            'calle':"Calle", 'numero':"Número",'id_comuna':'ID Comuna','comuna':"Comuna", 'id_region':'ID Región', 
            'region':'Región', 'horario_atencion':'Horario de Atención','distribuidor':'Distribuidor', 
            'distribuidor_logo':'Distribuidor Logo', 'distribuidor_logo_svg':'Distribuidor Logo SVG',
            'distribuidor_logo_svg_horizontal':'Distribuidor Logo SVG Horizontal', 
            'gasolina_93':'Gasolina 93 $/L', 'gasolina_97':'Gasolina 97 $/L','petroleo_diesel':'Petróleo Diesel $/L', 
            'gasolina_95':'Gasolina 95 $/L', 'glp_vehicular':'GLP Vehicular $/m3', 'gnc':'GNC $/m3',
            'pago_efectivo': 'Pago Efectivo','cheque':'Cheque', 'tarjetas_bancarias':'Tarjetas Bancarias',
           'tarjetas_grandes_tiendas':'Tarjeta Grandes Tiendas', 'tienda':'Tienda', 'farmacia':'Farmacia', 
            'mantencion':'Mantención', 'autoservicio':'Autoservicio', 'latitud':'Latitud', 'longitud':'Longitud'}
    df.rename(columns = newNames , inplace = True)
    df['ClasificacionGasolina 93 $/L'] = "" 
    df['ClasificacionGasolina 97 $/L'] = ""
    df['ClasificacionPetróleo Diesel $/L']= "" 
    df['ClasificacionGasolina 95 $/L']= ""
    df['ClasificacionGLP Vehicular $/m3']= "" 
    df['ClasificacionGNC $/m3']= ""
    hoy = str(str(datetime.datetime.today())[0:10])
    anio = str(str(datetime.datetime.today())[0:4])
    df['Fecha'] = hoy
    df["Latitud"] = df["Latitud"].apply(changeToNumber)
    df["Longitud"] = df["Longitud"].apply(changeToNumber)
    df.to_csv(f"historico/{hoy}.csv" , index=False)
    try:
        ref = pd.read_csv(f"https://raw.githubusercontent.com/Sud-Austral/data_energia/main/historico/historico_combustibles2_{anio}.csv")
        df = pd.concat([df,ref])
    except:
        print("ERROR")
        #ref = pd.read_csv(f"https://raw.githubusercontent.com/Sud-Austral/data_energia/main/historico/historico_combustibles2_.csv")
        #df = pd.concat([df,ref])
    #df.to_csv("avance.csv", index=False)
    df.to_csv("historico/historico_combustibles2.csv" , index=False)
    df.to_csv(f"historico/historico_combustibles_{anio}.csv" , index=False)

    return

def proceso2():
    url = 'https://3b9x.short.gy/lsVb5c'
    file = req.get(url, allow_redirects=True)
    open('data.csv', 'wb').write(file.content)
    df = pd.read_csv("data.csv", sep=";")
    newNames = {'fecha_actualizacion':'fecha_hora_actualizacion','calle':"direccion_calle", 
                'numero':"direccion_numero",'comuna':"nombre_comuna",  
                'region':'nombre_region', 'distribuidor':'distribuidor.nombre', 
                'distribuidor_logo':'distribuidor.logo', 'distribuidor_logo_svg':'distribuidor.logo_svg',
                'distribuidor_logo_svg_horizontal':'distribuidor.logo_horizontal_svg', 
                'kerosene':'precios.kerosene', 'pago_efectivo':'metodos_de_pago.efectivo','cheque':'metodos_de_pago.cheque', 
                'tarjetas_bancarias':'metodos_de_pago.tarjetas bancarias', 
                'tarjetas_grandes_tiendas':'metodos_de_pago.tarjetas grandes tiendas', 'tienda':'servicios.tienda', 
                'farmacia':'servicios.farmacia', 
                'mantencion':'servicios.mantencion', 'autoservicio':'servicios.autoservicio',
                'latitud':'ubicacion.latitud', 'longitud':'ubicacion.longitud'}
    df.rename(columns = newNames , inplace = True)
    df['Clasificacionprecios.kerosene'] = "" 
    hoy = str(str(datetime.datetime.today())[0:10])
    anio = str(str(datetime.datetime.today())[0:4])
    df['fecha'] = hoy
    df["ubicacion.longitud"] = df["ubicacion.longitud"].apply(changeToNumber)
    df["ubicacion.latitud"] = df["ubicacion.latitud"].apply(changeToNumber)
    df.to_csv(f"historico_kerosene/{hoy}.csv" , index=False)
    try:
        ref = pd.read_csv(f"https://raw.githubusercontent.com/Sud-Austral/data_energia/main/historico_kerosene/kerosene_historico_{anio}.csv")
        df = pd.concat([df,ref])
    except:
        print("ERROR")
        #ref = pd.read_csv(f"https://raw.githubusercontent.com/Sud-Austral/data_energia/main/historico_kerosene/kerosene_historico2.csv")
        #df = pd.concat([df,ref])

    #df.to_csv("avance.csv", index=False)
    df.to_csv("historico_kerosene/kerosene_historico2.csv" , index=False)
    df.to_csv(f"historico_kerosene/kerosene_historico_{anio}.csv" , index=False)
    return
    






if __name__ == '__main__':
    proceso()
    proceso2()
    
