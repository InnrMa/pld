import os
from mutagen.flac import FLAC

music_directory: str = "/home/betten/Music/Fujii Kaze"
albums: list[list[FLAC]] = []

def is_flac(file_path: str) -> bool:
    """Check if file is a valid FLAC by magic bytes."""
    signature = bytes([0x66, 0x4C, 0x61, 0x43])
    with open(file_path, "rb") as f:
        return f.read(4) == signature

def get_directory():
    print(os.getcwd())
    i: int = 0
    for (root,dirs,files) in os.walk(music_directory):
        print(root)
        print(dirs)
        print(len(files))
        if len(files) == 0:
            continue

        albums.append([])
        for file in files:
            if is_flac(root + "/" + file):
                metadata = FLAC(root + "/" + file)
                print(metadata.pprint())
                albums[i].append(metadata)
        i += 1



        #for file in directory[2]:
        #    print(file)

get_directory()