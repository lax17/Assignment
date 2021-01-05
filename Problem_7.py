
from datetime import datetime
import os
for file in os.listdir("../Assignment"):
    if file.endswith(".log"):
        with open("logsfile.log", "a") as logwritefile:
            with open(file,"r") as logreadfile:
                for line in logreadfile:
                    data = line.strip("\n") + " " + str(datetime.now())
                    logwritefile.write(data)
                    logwritefile.write("\n")