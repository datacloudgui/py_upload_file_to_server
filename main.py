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
    for row in csv_reader:
        print(f'Fecha {row[0]}, código: {row[1]}, posición: {row[2]}, temperatura: {row[3]}, humedad: {row[4]}, status: {row[5]}.')

        #Exclude row  that contain data sended OK to the server.
        if str(row[5]).strip() != "201":
            print("Voy a enviar: " + row[1])

            post_headers = {'Content-type': 'application/json'}
            load_json = {
                "dispositivo": "Raspberry4 - sennova - post-test",
                "codigo": str(row[1]),
                "ubicacion": str(row[2]),
                "temperatura":str(row[3]),
                "humedad": str(row[4])
            }
            jsonData = json.dumps(load_json)
            postresponse = requests.post(url_logistic, data=jsonData, headers=post_headers)
            print(f"El código de respuesta del servidor es: {postresponse.status_code}")

            if postresponse.status_code != 201:
                print(f"Error en el servidor al enviar: {row[1]}, intente nuevamente")
            else:
                print(f"Enviado: {row[1]}.")
                line_count += 1

    print(f'Enviados {line_count} registros.')