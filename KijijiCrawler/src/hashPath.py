'''
Created on 2014-04-02

@author: nriousset
'''
import os

def getHashDirectory(destinationFolder, adId):
    return os.path.join(destinationFolder, adId)

def moveAdsFromRootToHashPath(rootFolder):
    for fn in os.listdir(rootFolder):
        if os.path.isfile(os.path.join(rootFolder, fn)):
            print getHashDirectory(rootFolder, fn)
                    
if __name__ == '__main__':
    moveAdsFromRootToHashPath(".\data")
