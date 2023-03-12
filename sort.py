
from pathlib import Path
import shutil
import sys
import re
import os
from normalize import normalise


path = Path(r'/Users/bulavinamariia/Desktop/SOME_SHIT')


extensions = {
    'images': ['.jpeg', '.png', '.jpg', '.svg'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'music': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.zip', '.gz', '.tar']
}


def get_path():

    try:
        path = Path(sys.argv[1])

    except IndexError as e:

        print(e)

    return path



def get_not_file_paths(path):

    not_file_paths = [this.path for this in os.scandir(path) if this.is_dir()]
    

    print(not_file_paths)

    return not_file_paths    









def move(path: Path, file, k):

    path_to_k = path.joinpath(k)

    if not path_to_k.exists():

        path_to_k.mkdir()

    file.replace(path_to_k.joinpath(f'{normalise(file.stem)}{file.suffix}'))



def sort(path: Path, extensions):

    for file in path.glob('**/*.*'):

        for k, v in extensions.items():

            if file.suffix.lower() in v:

                move(path, file, k)   



def delete_folders(folder_path):

    not_file_paths = get_not_file_paths(folder_path)

    for p in not_file_paths:

        print(p)

        a = os.listdir(p)

        print(a)

        if not os.listdir(p):
            
            os.rmdir(p)






def main():

    sort(path, extensions)
    delete_folders(path)


if __name__ == '__main__':

    main()