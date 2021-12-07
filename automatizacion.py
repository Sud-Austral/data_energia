import requests
import json
import pandas as pd

def url():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"
return get_url

def proceso():
    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones.xlsx", index = False)

if __name__ == '__main__':
    proceso();