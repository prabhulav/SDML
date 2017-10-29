# SEQ-02 Reads the incidents.csv and creates a new file (incident_trim.csv) with Incident #, Description, Priority

what= input('Enter T if it is test:')

if what.upper() =='T':
	document_text=open('../SDMLdata/dummy.csv','r')
else:
	document_text=open('../SDMLdata/incidents.csv','r',encoding='latin-1')

out = open('../SDMLdata/incident_trim.csv', 'w')

first_row = document_text.readline().rstrip('\n').split(',')
x=0

header_data = dict()
for i in first_row:
	header_data[i]=x
	x=x+1

#print(header_data)
out.write('Priority' + ',' + 'CallID' + ',' + 'CallDesc' + '\n')

row = document_text.readline()
while row!='' and row!='\n':
    #print(row)
    row_split = row.rstrip('\n').split(',')
    out.write(row_split[header_data['Priority']] + ',' + row_split[header_data['CallID']] + ',' + row_split[header_data['CallDesc']] + '\n')
    row = document_text.readline()

out.close()