# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import os
from os import listdir
import RealEstate
import string

def displayHelp():
    print("usage : " + os.path.basename(sys.argv[0]) + " <Kijiji ads folder> <destination CSV file>")

def parseFile(kijijiAd):
    print("Parsing " + kijijiAd)
    f = open(kijijiAd,"r")
    html = f.read()
    
    # Must use the lxml HTML parser even though it has external dependecies, because the default python one is not good enough to parse the Kijiji pages
    # lxml Windows distribution was downloaded from http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
    soup = BeautifulSoup(html, "lxml")
    
    asset = RealEstate.Asset() 
    categories = soup.body.find_all('span', itemprop="title")
    if len(categories) > 0:
        asset.type = asset.parseType(categories[-1].text)
        
    attrTable = soup.body.find('table', id="attributeTable")
    if not attrTable is None: # V1 Kijiji ad formatting
        for attrRow in attrTable.find_all('tr'):
            attrCols = attrRow.find_all('td')
            if (len(attrCols) >= 2):
                asset.parseAttribute(attrCols[0].text, attrCols[1].text)
    else : # V2 Kijiji ad formatting
        descriptionSpan = soup.body.find('span', itemprop="description")
        if  not descriptionSpan is None:
            asset.description =  string.join(descriptionSpan.text.split())
        attrTable = soup.body.find('table', { 'class', 'ad-attributes'})
        if attrTable is None:
            return None
        for attrRow in attrTable.find_all('tr'):
            th = attrRow.find('th')
            td = attrRow.find('td')
            if not th is None and not td is None: 
                asset.parseAttribute(attrRow.find('th').text, attrRow.find('td').text)


    print(asset)
    return asset
    
def analyzeFolder(folder, csvFile):
    print("Analyzing folder " + folder)
    for basename in listdir(folder):
        fullname = os.path.join(folder, basename)
        if os.path.isdir(fullname):
            analyzeFolder(fullname, csvFile)
        elif os.path.splitext(fullname)[-1].lower() == ".html":
            asset = parseFile(fullname)
            if not asset is None:
                csvFile.write(asset.__repr__())
    
def main():
    if len(sys.argv) <= 2:
        displayHelp()
        return

    kjijiAdsFolder = sys.argv[1]
    if not os.path.exists(kjijiAdsFolder):
        print(kjijiAdsFolder + " doesn't exist") 
        displayHelp()
        return
    
    csvFileName = sys.argv[2]
#     if os.path.exists(csvFileName):
#         print(csvFileName + " already exists.") 
#         displayHelp()
#         return

    csvFile = open(csvFileName, "w");
    sampleAsset = RealEstate.Asset()
    sampleAsset.type = "TYPE"
    sampleAsset.rent = "RENT"
    sampleAsset.rentedBy = "RENTED BY"
    sampleAsset.address = "ADDRESS"
    sampleAsset.dateListed = "DATE LISTED"
    sampleAsset.furnished = "FURNISHED"
    sampleAsset.bathrooms = "BATHROOMS"
    sampleAsset.petFriendly = "PET FRIENDLY"
    sampleAsset.lastEdited = "LAST EDITED"
    sampleAsset.location = "LOCATION"
    sampleAsset.description = "DESCRIPTION"
    csvFile.write(sampleAsset.__repr__())
    
    analyzeFolder(kjijiAdsFolder, csvFile)
    
if __name__ == "__main__":
    main()
