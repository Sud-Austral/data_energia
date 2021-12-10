import requests
import json
import pandas as pd
import sys

def proceso():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones.xlsx", index = False)

def proceso2():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/diesel.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_diesel.xlsx", index = False)

def proceso3():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gasolina93.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gasolina93.xlsx", index = False)

def proceso4():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gasolina95.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gasolina95.xlsx", index = False)

def proceso5():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gasolina97.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gasolina97.xlsx", index = False)

def proceso6():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/glp.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_glp.xlsx", index = False)

def proceso7():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gnc.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gnc.xlsx", index = False)

def proceso8():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/emisiones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gnc.xlsx", index = False)

def proceso9():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/convencional.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_convencional.xlsx", index = False)

def proceso10():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/enoperacion.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_enoperacion.xlsx", index = False)

def proceso11():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/enpruebas.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_enpruebas.xlsx", index = False)

def proceso12():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/ernc.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_ernc.xlsx", index = False)

def proceso13():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/sistemas.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_sistemas.xlsx", index = False)


def proceso14():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/brent.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_brent.xlsx", index = False)

def proceso15():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/dolar.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_dolar.xlsx", index = False)

def proceso16():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/euro.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_euro.xlsx", index = False)

def proceso17():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/henryhub.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_henryhub.xlsx", index = False)

def proceso18():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/uf.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_uf.xlsx", index = False)

def proceso19():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/utm.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_utm.xlsx", index = False)

def proceso20():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/wti.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_wti.xlsx", index = False)

if __name__ == '__main__':
    try:
        proceso();
    except:
        try:
            proceso();
        except:
            error = sys.exc_info()[1]
            print(error)
        
    try:
        proceso2();
    except:
        try:
            proceso2
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso3();
    except:
        try:
            proceso3
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso4();
    except:
        try:
            proceso4
        except:
            error = sys.exc_info()[1]
            print(error)
    try:
        proceso5();
    except:
        try:
            proceso5
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso6();
    except:
        try:
            proceso6
        except:
            error = sys.exc_info()[1]
            print(error)
            
    try:
        proceso7();
    except:
        try:
            proceso7
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso8();
    except:
        try:
            proceso8
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso9();
    except:
        try:
            proceso9
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso10();
    except:
        try:
            proceso10
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso11();
    except:
        try:
            proceso11
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso12();
    except:
        try:
            proceso12
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso13();
    except:
        try:
            proceso13
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso14();
    except:
        try:
            proceso14
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso15();
    except:
        try:
            proceso15
        except:
            error = sys.exc_info()[1]
            print(error) 
    
    try:
        proceso16();
    except:
        try:
            proceso16
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso17();
    except:
        try:
            proceso17
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso18();
    except:
        try:
            proceso18
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso18();
    except:
        try:
            proceso18
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso19();
    except:
        try:
            proceso19
        except:
            error = sys.exc_info()[1]
            print(error)