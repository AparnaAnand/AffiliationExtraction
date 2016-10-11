import urllib2
import ConstantStrings as cs
from bs4 import BeautifulSoup
import re

def download_files(titles,urls):
    file = open("affiliations.csv", 'w')
    #print urls
    i=1
    for title,link in zip(titles,urls):
        print title,link,"\n"
        html_page=urllib2.urlopen(link)
        content = html_page.read()
        #raw_input()
        #use beautiful soup to obtain pdf link
        soup = BeautifulSoup(html_page,"html.parser")
        #print "SOUP FRAME: ",soup
        p = re.compile("affiliation\":\"(.*?)\"")
        #m = p.search(content)
        file.write(repr(title))
        file.write(",")
        for m in p.finditer(content):
            file.write(m.group(1).replace(',','_'))
            file.write(",")
        #download pdf to local folder
        file.write("\n")
        print "Finished", str(i)
        i+=1
    file.close()
    print("Completed")