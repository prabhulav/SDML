#SEQ-03 (optional) This program reads incidents.csv and remvoes unwanted fields.

import re
import string
from nltk import PorterStemmer

what=input('Enter T if it is test:')

if what.upper() =='T':
	document_text=open('../SDMLdata/dummy_3.csv','r')
else:
	document_text=open('../SDMLdata/incident_trim.csv','r',encoding='latin-1')

out=open('../SDMLdata/word_count.csv','w')

first_row = document_text.readline().rstrip('\n').split(',')
x=0

header_data = dict()
for i in first_row:
	header_data[i]=x
	x=x+1

#print(header_data)
row = document_text.readline()
wc=dict()
while row!='':
	row1 = row.rstrip('\n').split(',')
	#print (row1[header_data['CallID']])
	calldes_split= row1[header_data['CallDesc']].lower().replace(';',' ')\
		.replace('.',' ').replace(':',' ').replace('"',' ').replace('#',' ').\
		replace('{',' ').replace('}',' ').replace('!',' ').replace('~',' ').\
		replace('|',' ').replace("'",' ').replace("*",' ').split()
	for z in calldes_split:
		#Stem
		stemmed_word=PorterStemmer().stem(z)
		if wc.get(stemmed_word) is not None:
			wc[stemmed_word]+=1
		else:
			wc[stemmed_word]=1
	row=document_text.readline()

for rcd in wc:
	if len(rcd)>1 and wc[rcd]>1 and len(rcd)<=20:
		out.write(rcd+','+str(wc[rcd])+'\n')

out.close()
document_text.close()