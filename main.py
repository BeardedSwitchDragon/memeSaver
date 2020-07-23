from getRTs import *
from googleDrive import *
import os
import os.path

def run(): 
    mediaPaths = saveTweet()
    for path in mediaPaths:
        
        uploadToDrive(path)


run()

