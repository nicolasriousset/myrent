from bs4 import BeautifulSoup
import sys
import os
from os import listdir

def displayHelp():
    print("usage : " + os.path.basename(sys.argv[0]) + " <Kijiji ads folder> <destination CSV file>")

def parseFile(kijijiAd):
    print("Parsing " + kijijiAd)
    f = open(kijijiAd,"r")
    html = f.read()
    
    # Must use the lxml HTML parser even though it has external dependecies, because the default python one is not good enough to parse the Kijiji pages
    # lxml Windows distribution was downloaded from http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
    soup = BeautifulSoup(html, "lxml")
    
    #Extract urls of each classified ad
    categories = soup.body.find_all('span', itemprop="title")
    if len(categories) > 0:
        appartmentType = categories[-1].text;
        
    attrTable = soup.body.find('table', id="attributeTable")
    for attrRow in attrTable.find_all('tr'):
        attrCols = attrRow.find_all('td')
        if (len(attrCols) >= 2):
            attrName = attrCols[0]
            attrVal = attrCols[1]
            print(attrName.text + " = " + attrVal.text) 
    print(appartmentType + ";")
    
    
def analyzeFolder(folder):
    print("Analyzing folder " + folder)
    for f in listdir(folder):
        if os.path.isdir(f):
            analyzeFolder(f)
        else:
            parseFile(os.path.join(folder, f))
    
def main():
    if len(sys.argv) <= 2:
        displayHelp()
        return

    kjijiAdsFolder = sys.argv[1]
    if not os.path.exists(kjijiAdsFolder):
        printf(kjijiAdsFolder + " doesn't exist") 
        displayHelp()
        return
    
    csvFile = sys.argv[2]
    if os.path.exists(csvFile):
        printf(csvFile + " already exists.") 
        displayHelp()
        return

    analyzeFolder(kjijiAdsFolder)
    
if __name__ == "__main__":
    main()
