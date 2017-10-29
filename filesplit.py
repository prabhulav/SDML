### SEQ-01 This prigream reads cases.csv and extract I1-I5 into incidents.csv

# infile=open('filesplit.csv','r')
what= input('Enter T if it is test:')

if what.upper() =='T':
	infile=open('../SDMLdata/dummy.csv','r')
else:
	infile=open('../SDMLdata/cases.csv','r',encoding='latin-1')

out=open('../SDMLdata/incidents.csv','w')
#Read the line one by one 

n=5
priority=dict()
for z in list(range(1,n+1)): 
	priority['I'+str(z)]=0

i =infile.readline()
out.write(i)
while i!='':
	x=i.split(',')
	if x[3] in ('I1','I2','I3','I4','I5'):
		out.write(i)
		priority[x[3]]+=1
	i =infile.readline()

print (priority)

infile.close()
out.close()