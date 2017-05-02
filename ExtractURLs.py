import pandas as pd
import ConstantStrings as cs
import sys

def obtain_links():
    data = pd.read_csv(open(cs.file_name, 'rb'))
    return data[cs.doc_link]

def check_size(file_name,field):
	data = pd.read_csv(open(file_name, 'rb'),)
	print data
	raw_input()
	print len(set(data[field]))


if __name__ == "__main__":
	f = sys.argv[1]
	c = sys.argv[2]
	check_size(f,c)
