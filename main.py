import argparse
import os
import shutil
from google.colab import drive


def initialize(source):
    # mount drive folder
    drive.mount('/content/drive')
    print("Drive has mounted.")
    # unzip dataset
    if not os.path.isfile(source):
        print("the source file not exist !!!")
        return

    shutil.unpack_archive(source, "/content/Dataset")
    print("File has Unzipped into directory [Dataset]." + source)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, help='/content/drive/MyDrive/BillardAI/<file>.zip, the zip file google drive')
    opt = parser.parse_args()
    print(opt)
    initialize(**vars(opt))

