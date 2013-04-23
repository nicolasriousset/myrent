import urllib2

response = urllib2.urlopen('http://montreal.kijiji.ca/f-immobilier-appartements-condos-W0QQCatIdZ37')
html = response.read()

f = open("KijijiApprts.html", "w")
f.write(html)
f.close()
print "Done. Data saved into " + f.name