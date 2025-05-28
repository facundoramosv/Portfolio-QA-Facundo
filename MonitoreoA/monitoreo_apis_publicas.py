import requests
from datetime import datetime
import time

apis = {
    "Rick and Morty": "https://rickandmortyapi.com/api/character",
    "Cat Facts": "https://catfact.ninja/fact",
    "API Inexistente": "https://api.inventada123456.com/data",
    "OpenWeather sin API Key": "https://api.openweathermap.org/data/2.5/weather?q=London"
}

def chequear_api(nombre, url):
    try:
        inicio = time.time()
        response = requests.get(url, timeout=5)
        duracion = round((time.time() - inicio) * 1000, 2)

        if response.status_code == 200:
            return f"✅ {nombre} está activa - Tiempo: {duracion}ms"
        else:
            return f"⚠️  {nombre} responde con código {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"❌ {nombre} no está disponible - Error: {str(e)}"

# Crear reporte
hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
reporte = f"📡 REPORTE DE ESTADO DE APIS PÚBLICAS\n🕒 {hora}\n{'='*50}\n"

for nombre, url in apis.items():
    resultado = chequear_api(nombre, url)
    reporte += resultado + "\n"
    print(resultado)

# Guardar reporte
with open("reporte_apis.txt", "w", encoding="utf-8") as archivo:
    archivo.write(reporte)
