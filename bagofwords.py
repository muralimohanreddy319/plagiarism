'''bag of words'''

import os
import string
'''function to calculate eucledian norm of vector of files'''
class bagofwords(object):
	def __init__(self,path):
		self.path=path
		self.b=[]
	def listsum(self,dic): 
		k=0
		for x in dic.keys():
			k+=dic[x]**2
		return k
	'''function to calculate word frequency of the files'''
	def wordfreq(self,l1):
		dic={}
		for i in range(len(l1)):
			c=0
			for j in range(len(l1)):
				if(l1[i]==l1[j]):
					c+=1
			dic[l1[i]]=c
		return dic

	def dotprod(self,dic1,dic2):      #To claculate dot product of the values of common words in both files.
		s=0
		for x in dic1.keys():
			for y in dic2.keys():
				if(x==y):
					s+=dic1[x]*dic2[y]
		return s

	def conlist(self,fname1):       #to convert file into list of words eliminating special characters
		
		file1=open(fname1)
		f1=file1.read()
		f1=f1.lower()
		f1=f1.replace("\n"," ")
		l1=f1.split(" ")                              #convert the given file int list of words
		l1=[word.strip(string.punctuation)for word in l1]  #remove the special characters
		return l1
		
	def calbagofwords(self):
		dic1={};dic2={};s=0
		a=[]

		self.b=[fname for fname in os.listdir(os.getcwd()) if fname.endswith('.txt')]

		for fname1 in self.b:         #open the files in directory	
			
			l1=self.conlist(fname1)
			z=[]
			for fname2 in self.b:        #take individual files from directory to compare
				if(fname1==fname2):
					z.append("null")
				else:
					l2=self.conlist(fname2)
					dic1=self.wordfreq(l1)     #calculate word frequency of file 1
					if '' in dic1:
						del dic1['']
					dic2=self.wordfreq(l2)     #calclulate word frequency of file 2
					if '' in dic2:
						del dic2['']
				
					s=self.dotprod(dic1,dic2)   #to calculate dot product of the values of two dictionaries
					

					l1sum=0;l2sum=0
					l1sum=self.listsum(dic1)        #to calculate eucledian norm of vector of file1
					l2sum=self.listsum(dic2)	    #to calculate eucledian norm of vector of file2

					m=(l1sum**0.5)*(l2sum**0.5)

					percent=(s*100.0/m)				#calculate percent of plagiarism
					percent=round(percent,4)
					z.append(percent)
			a.append(z)
		return a
		
	def display(self):							#display the results in form of matrix
		mat=self.calbagofwords()
		#print len(max[self.b])
		spaces=(len(max(self.b))+5)*" "
		print spaces,
		#print (spaces)*" ",
		for i in self.b:
			print i,
			k=(int(len(spaces)-len(str(i))))
			print k*" ",
		print '\n'
		j=0
		for i in mat:
			print (self.b[j]),
			print (int(len(spaces)-len(self.b[j])))*" ",
			for x in i:
				print x,
				print (int(len(spaces)-len(str(x))))*" ",
			print '\n'
			j+=1

path=raw_input()
os.chdir(path)
bagofwords1=bagofwords(path)
bagofwords1.display()
