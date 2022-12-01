import nltk
import re
from metaphone import doublemetaphone
from polyglot.text import Text, Word
import configparser
from nltk import chunk



def DeletePunctuation(sentence:str):
	return re.sub(r'[^\w\s]', '', sentence)


def GetStrFromTree(tree:nltk.tree.Tree):
	retval = str()
	for i in tree:
		if isinstance(i, nltk.tree.Tree):
			retval = retval + GetStrFromTree(i)
		else:
			retval = retval + str(i[0]) +" "
	return retval

def GetCollocations(tree:nltk.tree.Tree):
	
	for i in tree:
		if isinstance(i, nltk.tree.Tree):
			if (len (i.leaves()) == 1):
				continue
			print(GetStrFromTree(i))
			continue
		else:
			#print(i[0])
			continue





class MorphAnalyzer:
	def __init__(self,lang=None):
		self.lang = lang
		

	def GetMorphemInfo(self, text:str,lang=None)->dict: # возвращает словарь со всеми словами и их разбором по морфемам
		if lang:
			self.lang =lang
		
		if not self.lang:
			raise Exception('укажите язык для анализа ')\
				.with_traceback(traceback_obj)

		text = DeletePunctuation(text)
		text = text.split()
		retval = dict()
		for i in text:
			retval[i] = Word(i, language=self.lang).morphemes
		
		return retval

	def GetSpeechPartsStupid(self,text:str): #возвращает список кортежей слово-> часть речи 
		return nltk.pos_tag(nltk.word_tokenize(text))

	def GetSpeechParts(self,text:str)->dict: #возвращает словарь слово-> часть речи 
		retval = dict()
		text = DeletePunctuation(text)
		text = nltk.word_tokenize(text)
		tags = nltk.pos_tag(text)
		for i in range(len(text)):
			retval[text[i]] = tags[i][1] # берёт тэг с частью речи

		return retval


class SyntaxAnalyzer:
	def __init__(self,pattern:str= None):
		self.pattern = pattern

	


	def GetSentenceTree(self,sentence:str,pattern:str=None)->nltk.tree.Tree:

		tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
		if pattern:
			self.pattern = pattern

		if not self.pattern:
			return chunk.ne_chunk(tagged)

		Parser = nltk.RegexpParser(self.pattern) 
		return Parser.parse(tagged)

	def GetTextTrees(self,text:str,pattern:str=None)->list:
		sentences = nltk.tokenize.sent_tokenize(text)
		trees = []
		for i in sentences:
			trees.append(self.GetSentenceTree(sentence=i,pattern=pattern))
		return trees





		
		


		
class PhoneticAnalysys:
	

	def GetPhoneticAnalysys(self,text:str)->dict:
		retval = dict()
		for i in nltk.tokenize.sent_tokenize(text):
			for j in nltk.word_tokenize(i):
				retval[j] = doublemetaphone(j)		
	
		return retval

