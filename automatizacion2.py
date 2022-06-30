import requests as req
import json
import pandas as pd
import sys

#BENCINA EN LÍNEA:

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
    ref = pd.read_csv("https://raw.githubusercontent.com/Sud-Austral/data_energia/main/historico/historico_combustibles.csv")
    df = pd.concat([df,ref])
    df.to_csv("avance.csv", index=False)

    return
    






if __name__ == '__main__':
    proceso()
    
