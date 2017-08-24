'''Longest Common String'''
import os
import string
class lcs(object):
	def __init__(self,path):
		self.path=path
		self.b=[]
	def length(self,fname):               #to calculate length of file
		file1=open(fname)
		f1=file1.read()
		s=len(f1)
		
		return s

	def conlist(self,fname1):              #to convert file into list of words eliminating special characters
		
		file1=open(fname1)
		f1=file1.read()
		f1=f1.lower()
		f1=f1.replace("\n"," ")  
		                   
		#f1=[word.strip(string.punctuation)for word in l1]     #remove the special characters
		print f1
		return f1

	def callcs(self):
		a=[];cmax=0
		self.b=[fname for fname in os.listdir(os.getcwd()) if fname.endswith('.txt')]   #getcwd()=Return a string representing the current working directory
		for fname1 in self.b:             #open the files in directory
			m=[]
			s=self.length(fname1)
			l1=self.conlist(fname1)
			
			for fname2 in self.b:         #take individual files from directory to compare with the first file
				t=self.length(fname2)
				if(fname1==fname2):
					y=0.0
				else:
					l2=self.conlist(fname2)    
					for temp in range(0,len(l1),1):
						j=0
						while(j<len(l2)):
							c=0
							i=temp
							if(l1[i]==l2[j]):
								while((i<len(l1)) and (j<len(l2)) and (l1[i]==l2[j])):
									c+=len(l1[i])
									i+=1
									j+=1
							else:
								j+=1	
							if(c>cmax):
								cmax=c
							
					print cmax						
					y=((cmax*2.0)/(s+t))*100     #s:length of fname1 and t:length of fname2 
					y=round(y,2)
				m.append(y)	
			a.append(m)
		return a
		
	def display(self):
		mat=self.callcs()
		spaces=10*" "
		print spaces,
		for i in self.b:
			print i,
			k=(int(len(spaces)-len(str(i))))
			print k*" ",
		print '\n'
		j=0
		for i in mat:
			#print j	
			#print (self.b[0])
			print (self.b[j]),
			print (int(len(spaces)-len(self.b[j])))*" ",
			for x in i:
				print x,
				print (int(len(spaces)-len(str(x))))*" ",
			print '\n'
			j+=1
path=raw_input()
os.chdir(path)
lcs1=lcs(path)
lcs1.display()
