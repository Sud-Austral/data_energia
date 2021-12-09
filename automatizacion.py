import requests
import json
import pandas as pd

def url():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones.json/'
    url2 = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/diesel.json'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"
    get_url2 = f"{url}?auth_key={api_auth}&limit=5000"
    return get_url, get_url2

def proceso():
    response = requests.get(url())
    response2 = requests.get(url())
    result = response.json(strict=False)
    result2 = response2.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones.xlsx", index = False)
    df2 = pd.DataFrame(result2["data"])
    df2.columns = result2["headers"]
    df2.to_excel("combustibles_vehicular_estaciones_diesel.xlsx", index = False)

if __name__ == '__main__':
    proceso();