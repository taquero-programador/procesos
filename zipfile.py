#!/usr/bin/env python3

import os
import zipfile
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")

def zip():
    """
    El proceso valida que exista el directorio 'input' y que no esté vacio,
    para cifrar el archivo(s) y el resultado lo guarda en 'output'.
    """

    ent = "input"
    local_path = os.getcwd()
    res_out = os.path.join(local_path, "output")
    file_zip = f"file_{today}.zip"

    if os.path.exists(ent):
        if len(os.listdir(os.path.join(local_path, ent))) > 0:
            os.chdir(os.path.join(local_path, ent))
            with zipfile.ZipFile(os.path.join(res_out, file_zip), "a") as ziper:
                for i in os.listdir():
                    ziper.write(i)
                    print("Archivo zipeado!")
        else:
            print(os.listdir(os.path.join(local_path, "input")))
            print(f'Directorio {"ent"} está vacio!')

zip()
