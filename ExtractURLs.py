import pandas as pd
import ConstantStrings as cs

def obtain_links():
    data = pd.read_excel(open(cs.file_name, 'rb'), sheetname=cs.sheet_name)
    #print data[cs.doc_link]
    return data[cs.doc_title],data[cs.doc_link]