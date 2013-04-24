import urllib2

def main():
    response = urllib2.urlopen('http://www.kijiji.ca')
    html = response.read()
    outputFile = open("kijiji.ca.html", "w")
    outputFile.write(html)
    outputFile.close()


if __name__ == "__main__":
    main()