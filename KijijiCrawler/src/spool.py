'''
Created on 2014-04-02

@author: nriousset
'''
import os
import shutil

def getSpoolSubfolder(destinationFolder, adPath):
    filename = os.path.basename(adPath)
    id = os.path.splitext(filename)[0];
    #ensure we have exactly 10 digits in the id. 
    #Truncate if required, fill with zeroes else
    idLen = 10
    id = id[-idLen:]
    id = id.zfill(idLen);
    return os.path.join(destinationFolder, id[0:2], id[2:6]);

def moveAdsToSpool(rootFolder):
    for basename in os.listdir(rootFolder):
        fullname = os.path.join(rootFolder, basename)
        if os.path.isfile(fullname):
            destinationFolder = getSpoolSubfolder(rootFolder, fullname)
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            print("Moving " + fullname + " to " + destinationFolder)
            shutil.move(fullname, destinationFolder)
                    
if __name__ == '__main__':
    moveAdsToSpool(".\data")
