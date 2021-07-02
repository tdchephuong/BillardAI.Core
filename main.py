import argparse
import os
import shutil
from google.colab import drive
from ultils.ultils import mkdir, log_error, log_message

def initialize(source):
    # mount drive folder
    drive.mount('/content/drive')
    log_message("Drive has mounted.")

    # make dir Videos
    mkdir('/content/Videos')

    # unzip dataset
    if not os.path.isfile(source):
        log_error("the source file not exist !!!")
        return

    shutil.unpack_archive(source, "/content/Dataset")
    log_message("File has Unzipped into directory [Dataset]." + source)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, help='/content/drive/MyDrive/BillardAI/<file>.zip, the zip file google drive')
    opt = parser.parse_args()
    print(opt)
    initialize(**vars(opt))

