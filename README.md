**EDIT: 10 Jan 2023**

This code helps to setup mongoDB in ubuntu 20.04 using binary (https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-6.0.3.tgz) 

Pointers:

1. Make sure to create the folder to store the log file -- [ sudo mkdir -p /var/log/mongodb && sudo chmod +x /var/log/mongodb ]
2. Run the script using command -- [ sudo /usr/bin/python3 mongo-install.py mongo-install.json ]


NOTE: This script still needs a lot of code addition which will be done in future. For now, it gives you mongodb server up and running. If you want to have a customized config file, you need to write your own config file.




**EDIT: 11 Jan 2023**

Config file is added. After installation is complete, you can make changes in the config file as per your requirement.



**Suggestions are always welcome, drop me message at manasrawat0007@gmail.com. Keep learning and keep exploring**
