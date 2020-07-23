
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiSecrets import *

def authenticateGoogleDrive():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("../memeSaverCreds/mycreds.txt")
    if gauth.credentials is None:

        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:

        gauth.Refresh()
    else:

        gauth.Authorize()

    gauth.SaveCredentialsFile("../memeSaverCreds/mycreds.txt")
    return GoogleDrive(gauth)

def uploadToDrive(filePath):
    drive = authenticateGoogleDrive()
    file = drive.CreateFile()
    file.SetContentFile(filePath)
    file.Upload()
