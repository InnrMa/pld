import os
import requests

from pld_api_calls import LrcLibApiCall

music_directory = "/home/betten/Music"

def get_directory():
    print(os.getcwd())
    for directory in os.walk(music_directory):
        for file in directory[2]:
            print(file)

get_directory()

api_call: LrcLibApiCall = LrcLibApiCall()

r = api_call.get_lyrics(["Borislav+Slavov"])

print(r)