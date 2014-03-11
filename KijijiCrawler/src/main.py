import urllib2
import re
import os
from bs4 import BeautifulSoup

def downloadAd(adUrl, destinationFolder):
    print(adUrl)
    adId = re.findall(".*/(.+)\?.*", adUrl)
    if not adId :
        adId = re.findall(".*/(.+)$", adUrl)
    adId = adId[0]
    filename = os.path.join(destinationFolder, adId + ".html")
    
    if os.path.exists(filename):
        print("Already downloaded, skipping")
        return # ad already downloaded, ignore
    
    try:
        print("Downloading to " + filename)
        response = urllib2.urlopen(adUrl)
        html = response.read()
    
        
        destinationFile = open(filename, "w")
        destinationFile.write(html) 
        destinationFile.close()
    except urllib2.URLError as e:
        print("Failed to download from " + adUrl + ":" + e.reason)
    
def downloadAdsFromResultsPage(resultsPageUrl, destinationFolder):
    try:
        response = urllib2.urlopen(resultsPageUrl)
        html = response.read()
        
        # Must use the lxml HTML parser even though it has external dependecies, because the default python one is not good enough to parse the Kijiji pages
        # lxml Windows distribution was downloaded from http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
        soup = BeautifulSoup(html, "lxml") 
    
        #Extract urls of each classified ad
        for row in soup.body.find_all('td', { 'class', 'description'} ):
            downloadAd("http://www.kijiji.ca/" + row.a.get('href'), destinationFolder)
            
        #find url to the next page of ads
        nextPageTag = soup.body.find('a', text=re.compile('Suivant.*'))
        if nextPageTag is None:
            return None
        
        return nextPageTag.get('href')
    except urllib2.URLError as e:
        print("Failed to download from " + resultsPageUrl + ":" + e.reason)
    
def main():
    destinationFolder = "data"
    if not os.path.exists(destinationFolder): 
        os.makedirs(destinationFolder)
    
    nextResultsPage = '/f-immobilier-appartements-condos-W0QQCatIdZ37';
    #nextResultsPage = 'http://montreal.sdfsfsdfsdf.c';
    while nextResultsPage != None:
        nextResultsPage = downloadAdsFromResultsPage("http://montreal.kijiji.ca" + nextResultsPage, destinationFolder)
    
if __name__ == "__main__":
    main()
