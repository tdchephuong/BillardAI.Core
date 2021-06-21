import shutil
import datetime
import os

def movefile(pathFile):
    date = datetime.datetime.now().strftime("%m%d%Y")
    dest_file = "/content/drive/MyDrive/BillardAI/Models/best_" + date + ".pt"
    exist = os.path.isfile(dest_file)

    if exist:
        os.remove(dest_file)
        print("file has removed : " + "best_" + date + ".pt")
        
    shutil.move(pathFile, dest_file)