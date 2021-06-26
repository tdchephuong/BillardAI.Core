import shutil
import datetime
import os
import logging

def copy_file_to_folder(pathFile, dest_path):
    date = datetime.datetime.now().strftime("%m%d%Y_%h%M%s")
    exist = os.path.isfile(pathFile)

    if exist:
        logging.exception("file has exist. : " + pathFile)
        return
        
    shutil.copyfile(pathFile, dest_path)
    print("file has copied to : " + dest_path)

def backup_file(pathFile):
    date = datetime.datetime.now().strftime("%m%d%Y_%h%M%s")

    dest_file = "/content/drive/MyDrive/BillardAI/Models/best_" + date + ".pt"

    exist = os.path.isfile(dest_file)

    if exist:
        os.remove(dest_file)
        print("file has removed : " + "best_" + date + ".pt")
        
    shutil.copyfile(pathFile, dest_file)
    print("file has copied to : " + "best_" + date + ".pt")

def movefile(pathFile):
    date = datetime.datetime.now().strftime("%m%d%Y")
    dest_file = "/content/drive/MyDrive/BillardAI/Models/best_" + date + ".pt"
    exist = os.path.isfile(dest_file)

    if exist:
        os.remove(dest_file)
        print("file has removed : " + "best_" + date + ".pt")
        
    shutil.move(pathFile, dest_file)
    print("file has moved to : " + "best_" + date + ".pt")

    
def zipdir(zipFolder):
    date = datetime.datetime.now().strftime("%m%d%Y")
    output_filename = zipFolder + "label_" + date + ".zip"
    shutil.make_archive(output_filename, 'zip', zipFolder)