'''bag of words'''

import os
import string
'''function to calculate eucledian norm of vector of files'''
def listsum(dic): 
	k=0
	for x in dic.keys():
		k+=dic[x]**2
	return k
'''function to calculate word frequency of the files'''
def wordfreq(l1):
	dic={}
	for i in range(len(l1)):
		c=0
		for j in range(len(l1)):
			if(l1[i]==l1[j]):
				c+=1
		dic[l1[i]]=c
	return dic

dic1={};dic2={};s=0
a=[]

b=[fname for fname in os.listdir(os.getcwd()) if fname.endswith('.txt')]

for fname1 in b:#open the files in directory
	z=[]
	file1=open(fname1)
	f1=file1.read()
	f1=f1.lower()
	f1=f1.replace("\n"," ")
	l1=f1.split(" ")  #convert the given file int list of words
	l1=[word.strip(string.punctuation)for word in l1]  #remove the special characters

#for i in fname:
	for fname2 in b:#take individual files from directory to compare
		if(fname1==fname2):
			z.append("null")
		else:
			f2=open(fname2)
			f2=f2.read()
			f2=f2.lower()
			f2=f2.replace("\n"," ")
			l2=f2.split(" ")
			l2=[word.strip(string.punctuation)for word in l2]

			dic1=wordfreq(l1)#calculate word frequency of file 1
			if '' in dic1:
				del dic1['']
			dic2=wordfreq(l2)#calclulate word frequency of file 2
			
			if '' in dic2:
				del dic2['']
			s=0

	#To claculate dot product of the values of common words in both files.
			for x in dic1.keys():

				for y in dic2.keys():
					if(x==y):
						s+=dic1[x]*dic2[y]

			l1sum=0;l2sum=0
			l1sum=listsum(dic1) #to calculate eucledian norm of vector of file1
			l2sum=listsum(dic2)	#to calculate eucledian norm of vector of file2

			m=(l1sum**0.5)*(l2sum**0.5)

			#calculate percent of plagiarism
			percent=(s*100.0/m)
			percent=round(percent,4)
			z.append(percent)
	a.append(z)
for i in a:
	print i

