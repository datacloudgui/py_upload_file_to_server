#CSV file and argument library
import argparse
import csv

#### API dependencies
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument("file", help="The name of the file to upload, including .csv")
args = parser.parse_args()

#URL to send data
url_logistic = ''

with open(args.file) as csv_file:
    print(f'Abriendo el archivo.')
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for column in csv_reader:
        print(f'Fecha {column[0]}, código: {column[1]}, posición: {column[2]}, temperatura: {column[3]}, humedad: {column[4]}, status: {column[5]}.')

        #Exclude column  that contain data sended OK to the server.
        if str(column[5]).strip() != "201":
            print("Voy a enviar: " + column[1])

            post_headers = {'Content-type': 'application/json'}
            load_json = {
                "dispositivo": "Raspberry4 - sennova - post-test",
                "codigo": str(column[1]),
                "ubicacion": str(column[2]),
                "temperatura":str(column[3]),
                "humedad": str(column[4])
            }
            jsonData = json.dumps(load_json)
            postresponse = requests.post(url_logistic, data=jsonData, headers=post_headers)
            print(f"El código de respuesta del servidor es: {postresponse.status_code}")

            if postresponse.status_code != 201:
                print(f"Error en el servidor al enviar: {column[1]}, intente nuevamente")
            else:
                print(f"Enviado: {column[1]}.")
                line_count += 1

    print(f'Enviados {line_count} registros.')