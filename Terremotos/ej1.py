import json
import urllib.request

from datetime import datetime

def main():
  url:str = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson'
  data = urllib.request.urlopen(url).read().decode()
  
  dataJson = json.loads(data)

  features : list = dataJson['features']

  cabecera = "{:^12}{:^25}{:50}".format('Magnitud', 'Tiempo', 'Lugar')

  promedio = 0

  separador = '=' *90

  print(separador)
  print(cabecera)

  for feature in features:
    prop = feature['properties']
    date = datetime.fromtimestamp(prop['time']/1000.0) # Convertir milisegundos en segundos
    fila = "{:^12}{:^25}{:50}".format(prop['mag'], date.strftime('%Y-%m-%d %H:%M:%S'), prop['place'])
    
    print(fila)

    promedio += prop['mag']
  
  print(separador)

  print('Magnitud promedio: {:.2f}'.format(promedio / len(features)))

if __name__ == "__main__":
    main()