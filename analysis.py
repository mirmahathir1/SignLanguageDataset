from os import listdir
from os.path import isfile, join
import os

count = 0

videoname_mapfile = open('./videoname_map.txt', 'w')

for i in range(13):
    mypath = './reduced_videos/' + str(i)
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles:
        print('./reduced_videos/', i, '/', file, ' => ', count, '.mp4')
        # os.rename(r'./reduced_videos/' + str(i) + '/' + file, r'./reduced_videos/' + str(i) + '/' + str(count) + '.mp4')
        count = count + 1

print(count)
