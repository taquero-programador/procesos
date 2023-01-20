#!/usr/bin/env python3

import os
import pyminizip
import zipfile
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")
zip_file = os.path.join(os.getcwd(),"output",f"zipout_{today}.zip")
unzip_file = os.path.join(os.getcwd(), "output")
password = f"B4nr3g10!{today}"

def zip_pass():

    local_path = os.path.join(os.getcwd(), "input")
    os.chdir(local_path)
    files = [i for i in os.listdir()]
    pyminizip.compress(files[0], None, zip_file, password, 5)

# zip_pass()

def unzip():

    os.chdir(os.path.join(os.getcwd(), "input"))
    for i in os.listdir():
        if i.endswith(".zip"):
            print(i)
            unzip = os.path.join(os.getcwd(), i)
            pyminizip.uncompress(unzip, password, unzip_file, 0)

unzip()
