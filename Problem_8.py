
import os
import uuid

FILE_SIZE = 2097152 # in bytes equals to 2MB
CONTENT_TO_LOG = input("Enter the content to log :")
CURRENT_FILE = "logsfile.log"  # this file is more than 2mb to test

if os.path.getsize(CURRENT_FILE) >= FILE_SIZE:
    CURRENT_FILE = uuid.uuid4().hex + ".log"
    with open(CURRENT_FILE ,"a") as file:
        file.write(CONTENT_TO_LOG)
else:
    with open(CURRENT_FILE, "a") as file:
        file.write(CONTENT_TO_LOG)





