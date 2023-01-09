#!/usr/bin/python3

import sys
import os
import json
import shutil
import logging

logging.basicConfig(filename='/var/log/mongodb/mongodb.log', format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def load_config (config_file_path):
    config_data = {}
    with open(config_file_path) as config_file:
        config_data = json.load(config_file)
    return config_data

def download_binary(url, mongo_home):
    try:
        shutil.rmtree(mongo_home)
    except:
        pass
    os.makedirs(mongo_home)
    cmd = "sudo apt update -y && sudo apt-get install -y libcurl4 openssl liblzma5 &&  curl -o "+mongo_home+"/mongodb-6.0.3.tgz "+url
    os.system(cmd)
    logging.info("System updated & mongo binary downloaded.")

def mongo_config(mongo_home):
    cmd = "tar -xvf "+mongo_home+"/mongodb-6.0.3.tgz -C "+mongo_home+" && mv "+mongo_home+"/mongodb-linux-x86_64-ubuntu2004-6.0.3 "+mongo_home+"/mongodb && sudo cp -R "+mongo_home+"/mongodb/bin/mongod /usr/local/bin/mongod && sudo chmod +x /usr/local/bin/mongod"
    os.system(cmd)
    logging.info("Mongo binary configured.")

def start_mongo(data_path):
    try:
        shutil.rmtree(data_path)
    except:
        pass
    os.makedirs(data_path)
    cmd = "/usr/local/bin/mongod --dbpath "+data_path
    os.system(cmd)
    logging.info("Mongo started...")

def install_mongo_client(client):
    cmd = "sudo apt-get install -y "+client
    os.system(cmd)
    
config_data = {}
try:
    config_data = load_config(sys.argv[1])
    download_binary(config_data['url'], config_data['mongo_home']) 
    mongo_config(config_data['mongo_home'])
    install_mongo_client(config_data['client_name'])
    start_mongo(config_data['data_path'])
    
except Exception as exp:
    logging.exception("Mongo installation failed.")
