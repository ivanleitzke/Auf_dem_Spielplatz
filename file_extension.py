# Import the modules
import os
import json

vd_dict = dict()
vd_dict['playable'] = False

vf = "/home/leitzke/git_repo/DataCentric_MigoBox_Python/metallica/greatwar.mp3"

file_extension = os.path.splitext(vf)[1][1:]

if file_extension in ["mp2", "mp3", "aac", "ogg", "flac", "opus", "wav", "aiff"]:
    vd_dict['playable'] = True

print(vd_dict)


print("Arbeit hart. Lerne jeden Tag fleißig")