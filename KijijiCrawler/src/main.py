import urllib2
import re
import os
from bs4 import BeautifulSoup

def downloadAd(adUrl, destinationFolder):
    print(adUrl)
    fields = adUrl.split("-")
    filename = os.path.join(destinationFolder, fields[-1] + ".html")
    
    if os.path.exists(filename):
        return # ad already downloaded, ignore
    
    response = urllib2.urlopen(adUrl)
    html = response.read()

    
    file = open(filename, "w")
    file.write(html) 
    file.close()
    
def downloadAdsFromResultsPage(resultsPageUrl, destinationFolder):
    response = urllib2.urlopen(resultsPageUrl)
    html = response.read()
    
    # Must use the lxml HTML parser even though it has external dependecies, because the default python one is not good enough to parse the Kijiji pages
    # lxml Windows distribution was downloaded from http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
    soup = BeautifulSoup(html, "lxml") 

    #Extract urls of each classified ad
    for row in soup.body.find_all(id=re.compile('resultRow.*')):
        downloadAd(row.a.get('href'), destinationFolder)
        
    #find url to the next page of ads
    nextPageTag = soup.body.find('a', text=re.compile('Suivant.*'))
    if nextPageTag is None:
        return None
    
    return nextPageTag.get('href')
    
    
def main():
    destinationFolder = "data"
    if not os.path.exists(destinationFolder): 
        os.makedirs(destinationFolder)
    
    nextResultsPage = 'http://montreal.kijiji.ca/f-immobilier-appartements-condos-W0QQCatIdZ37';
    while nextResultsPage != None:
        nextResultsPage = downloadAdsFromResultsPage(nextResultsPage, destinationFolder)
    
if __name__ == "__main__":
    main()
