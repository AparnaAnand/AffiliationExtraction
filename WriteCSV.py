import urllib2
import re
import ConstantStrings as cs

def download_files(urls):
    file = open(cs.output_file, 'w')
    no_file = open(cs.file_no_author,"w")
    i=1
    file.write("Page ID,Author,Affiliation\n")
    for link in urls[:]:
        print link,"\n"
        html_page=urllib2.urlopen(link)
        match_id = re.search("arnumber=(\d+)$",link)
        if match_id == None:
            match_id = re.search("fileName=(\d+)", link)
        id_num = match_id.group(1)
        content = html_page.read()
        p = re.compile("name\":\"(.*?)\",\"affiliation\":\"(.*?)\"")
        flag = 0
        for m in p.finditer(content):
            flag = 1
            file.write(str(id_num))
            file.write(",")
            file.write(m.group(1).replace(',', '_'))
            file.write(",")
            file.write(m.group(2).replace(',','_'))
            file.write("\n")
        if flag ==0:
            print "nothing here.."
            no_file.write(str(id_num))
            no_file.write("\n")
        print "Finished", str(i)
        i+=1
    file.close()
    no_file.close()
    print("Completed")