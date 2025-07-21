"""
Tidies up all movie names and subtitles in a folder.

Usage:
    python movie.py folder_path

Example:
    How.To.Train.Your.Dragon.2010-SuccessfulCrab.mkv
    ↓
    how to train your dragon.mkv
"""

import sys
import os
import re
import shutil

EXTENSIONS = [".mp4", ".mkv", ".srt", ".avi"]
BASE_DIRECTORY = os.path.abspath(sys.argv[1])

def rename_files(files: str, movie_name: str, folder: str) -> None:
    for file in files:
        for ext in EXTENSIONS:
            if file.endswith(ext):
                name = movie_name.lower() + ext
                os.rename(os.path.join(BASE_DIRECTORY, folder, file), 
                          os.path.join(BASE_DIRECTORY, name))

def get_movie_name(name: str) -> str:    
    pattern = r"\d{4}"
    
    years = re.findall(pattern, name)
    if not years:
        print(f"Skipping folder (no year found): {name}")
        return name.strip()
    
    split_value = years[-1]
    return name.split(split_value)[0].rstrip("(").strip()

def rename(folders: list) -> None:
    for folder in folders:
        movie_name = get_movie_name(folder)
        rename_files(os.listdir(os.path.join(BASE_DIRECTORY, folder)), movie_name, folder)
        shutil.rmtree(os.path.join(BASE_DIRECTORY, folder))

def get_folders() -> list:
    ls = os.listdir(sys.argv[1])
    return [_ for _ in ls if os.path.isdir(os.path.join(BASE_DIRECTORY, _))]

def main():
    if not os.path.isdir(sys.argv[1]):
        sys.exit('check directory and try again!')
    rename(get_folders())

if __name__ == "__main__":
    main()