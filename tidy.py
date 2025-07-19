'''
    tidies up all episode and subtitle names.

    usage: python tidy.py folder_path

    requirements: absolute path to the folder
    limitations: does not handle relative path and files
    example:  The.Bear.S04E03.1080p.WEB.H264-SuccessfulCrab.mkv ---------> 403.mkv
'''

import re
import sys
import os

def rename(files, dir):
    name_pattern = r'[sS]\d{2}[eE]\d{2}'
    extension_pattern = r'\.[^.\\/:*?"<>|\r\n]+$'
    renamed = False

    for file in files:
        extension = re.search(extension_pattern, file)
        filename = re.search(name_pattern, file)
        if (filename is not None and extension is not None and extension.group() != '.part'):
            filename = filename.group()
            filename = re.sub(r'[A-Za-z]', "", filename).lstrip('0') + extension.group()
            renamed = True
        else:
            filename = file
        os.rename(dir + file, dir + filename)
    print("renamed all episodes and their subtitles, if any!" if renamed else "nothing to rename!")

def main():
    if os.path.isdir(sys.argv[1]):
        dir = sys.argv[1].rstrip('/') + '/'
    else:
        sys.exit('check directory and try again!')
        
    rename(os.listdir(dir), dir)

if __name__ == "__main__":
    main()