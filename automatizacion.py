import requests
import json
import pandas as pd

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

if __name__ == '__main__':
    proceso();
    proceso2();
    proceso3();
    proceso4();
    proceso5();
    proceso6();
    proceso7();