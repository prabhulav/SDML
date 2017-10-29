#SEQ-03 (optional) This program reads incidents.csv and remvoes unwanted fields.

import re
import string
what= input('Enter T if it is test:')

if what.upper() =='T':
	document_text=open('../SDMLdata/dummy.csv','r')
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
	calldes_split= row1[header_data['CallDesc']].split()
	for z in calldes_split:
		if wc.get(z) is not None:
			wc[z]+=1
		else:
			wc[z]=1
	row=document_text.readline()

for rcd in wc:
	out.write(rcd+','+str(wc[rcd])+'\n')


out.close()
document_text.close()