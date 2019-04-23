from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
import pygame, sys
import os

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
def display(image):
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        screen.fill((255,255,255))
        b1=pygame.image.load(image)
        screen.blit(b1, (0,0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    sleep(3)
            pygame.display.flip()
def killgphoto2Process():
        p=subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out,err = p.communicate()
        for line in out.splitlines():
            if b'gvfsd.gphoto2' in line:
                pid=int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)
shot_date= datetime.now().strftime("%Y-%m-%d")
shot_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiShots"
clearCommand = ["--folder", "/store-00020001/DCIM/100CANON", 
                "-R", "--delete-all-files"]
triggerCommand= ["--trigger-capture"]
downloadCommand=["--get-all-files"]
folder_name=shot_date +picID
save_location = "/home/pi/Desktop/gphoto2/images/"+folder_name
def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("Failed to make a new directory")
    os.chdir(save_location)
def captureImages():
    gp(triggerCommand)
    sleep(3)
    gp(downloadCommand)
    gp(clearCommand)
def renameFiles(ID):
    for filename in os.listdir("."):
        global file1
        in len(filename) < 13:
            if filename.endswith(".JPG"):
                file1 = shot_time+ID+".JPG"
                os.rename(filename, (file1))
                print("renamed the JPG"
                return file1                
def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client1_secret.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    while True:
        createSaveFolder()
        captureImages()
        renameFiles(picID)
        #display(file1)
        sleep(5)
        file_metadata={'name':file1}
        media = MediaFileUpload('/home/pi/Desktop/gphoto2/images/2019-04-17PiShots/file1', 
                                mimetype = 'image/jpeg')
        file=service.files().create(body=file_metadata, media_body=media,
                                    fields='id').execute()
        #print('file ID: %s' % file.get('id'))
killgphoto2Process()
gp(clearCommand)
#if _name_=='_main_':
main()