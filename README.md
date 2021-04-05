# py_upload_file_to_server

Take a comma separated file and send to an URL that receive the data in a JSON format.

The columns of the file are:

date the reading, barcode, position(in warehouse), temperature, humidity, status

Only take the not sended rows (status different of 201)

# Requierements

Python libraries: request, csv, argparse and json

# How to run?

Put your endpoint URL in line 14 (url_logistic)

Run with:

``` python
python3 main.py barcodes-4-4-2021.txt
```