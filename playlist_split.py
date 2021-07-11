from os import listdir
from os.path import isfile, join
import os
import split_one_file
listOfSpeakers = ['1']

for i in listOfSpeakers:
    mypath = './reduced_videos/' + i
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if not os.path.isdir('./reduced_splits/' + i):
        os.mkdir('./reduced_splits/' + i)
    for file in onlyfiles:
        video_name = file.split('.')[0]

        if not os.path.isdir('./reduced_splits/'+i+"/"+video_name):
            os.mkdir('./reduced_splits/'+i+"/"+video_name)

        destination_folder = './reduced_splits/'+i+"/"+video_name+"/"
        src_folder = './reduced_videos/' + i + '/'

        split_one_file.split(src_folder,video_name+".mp4",destination_folder,120)


