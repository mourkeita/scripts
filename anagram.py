#! /usr/bin/python
# coding: utf8

'''
This program simulates an anagram game.
The user enter a word and the program 
lists all the anagrams
'''

def bye():
	print "End of the program"

class Anagram:
	'''
	This class simulates an anagram
	'''

	def __init__(self, name):
		self.name = name

	def getNom(self):
		return self.name

	def printNom(self):
		print self.name

	def getAnagram(self, name):
		return name

	def printAnagram(self, name):
		print self.getAnagram(name)

	def printAllAnagrams(self, tab):
		for i in range(len(tab)):
			print tab[i]

	def getAnagramNumbers(self, name):
		nameLength = len(name)
		if nameLength < 3:
			print nameLength
		else:
			j = 1
			for i in range(1, nameLength+1):
				i,j = (i,i *j)
			return j			

	def treatment(self, name, callback=bye):
		tab = []
		if len(name) == 0 or len(name) == 1:
			one = self.getAnagram(name)
			tab.append(one)
			self.printAnagram(name)
		else:
			tab.append(name)
			word_len = len(name)
			anagrams = self.getAnagramNumbers(name)
			
			for i in range(word_len):
				if i + 1 < word_len:
					temp = name[i]
					name = name.replace(name[i], name[i+1])
					name = name.replace(name[i+1], temp)
					print "Nouveau nom : %s" % name
				tab.append(name)

		self.printAllAnagrams(tab)
			

if __name__ == '__main__':
	word = Anagram('abcde')
	name =word.getNom()
	word.treatment(name)
