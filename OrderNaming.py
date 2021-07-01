# Program to rename files into an order to conviniently use them
# in Adobe After Effects. All Files will have a number to them
# at the end. From 1 to ... n

import os

folderPath = r'E:\VLC Snaphots\NO2 Level'
fileNumber = 1

for filename in os.listdir(folderPath):
    os.rename(folderPath+ '\\' +filename,folderPath + '\\' + "NO2Level_"+ str(fileNumber)+".png")
    fileNumber+=1