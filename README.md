**EDIT: 10 Jan 2023**

This code helps to setup mongoDB in ubuntu 20.04 using binary from Mongo official (https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-6.0.3.tgz).

Pointers:

1. Make sure to create the folder to store the log file -- [ **sudo mkdir -p /var/log/mongodb** ]
2. Clone the repo and then **cd** into it.
3. Run the script using command -- [ **sudo /usr/bin/python3 mongo-install.py mongo-install.json** ]


**EDIT: 11 Jan 2023**

1. Config file is added. After installation is complete, you can make changes in the config file as per your requirement and restart the service.
2. This service is being controlled using systemctl commands. For example, **sudo systemctl restart mongodb**



**Suggestions are always welcome, drop me message at manasrawat0007@gmail.com. Keep learning and keep exploring**
