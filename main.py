import nltk
import re


new = """

When Australia’s richest woman Gina Rinehart threw a financial lifeline to Netball Australia, she triggered a debate about sponsorships and the role of social and political issues in the sporting sphere. Then she walked away.

Rinehart’s bombshell decision to withdraw a 14 million Australian dollar ($8.9 million) sponsorship deal for the Diamonds, Australia’s national netball team, caught the players off-guard and struck a blow to the future of Netball Australia – a sporting body mired in debt.

The drama engulfing the Diamonds is not new, but experts say disputes could become more common as athletes and fans take a stronger stance on the source of sponsorship money.
"""


def DeletePunctuation(sentence:str):
	return re.sub(r'[^\w\s]', '', sentence)



sentence = """When Australia’s richest woman Gina Rinehart threw a financial lifeline to Netball Australia, she triggered a debate about sponsorships and the role of social and political issues in the sporting sphere."""
tokens = nltk.word_tokenize(sentence)
pattern = """NP: {<DT>?<JJ>*<NN>}
VBD: {<VBD>}
IN: {<IN>}
VP: {<ADJ_SIM><V_PRS>}
VP: {<ADJ_INO><V.*>}
VP: {<V_PRS><N_SING><V_SUB>}
NP: {<N_SING><ADJ.*><N_SING>}
NP: {<N.*><PRO>}
VP: {<N_SING><V_.*>}
VP: {<V.*>+}
NP: {<ADJ.*>?<N.*>+ <ADJ.*>?}
DNP: {<DET><NP>}
PP: {<ADJ_CMPR><P>}
PP: {<ADJ_SIM><P>}
PP: {<P><N_SING>}
PP: {<P>*}
DDNP: {<NP><DNP>}
NPP: {<PP><NP>+}
"""

tagged = nltk.pos_tag(tokens)
NPChunker = nltk.RegexpParser(pattern)
result = NPChunker.parse(tagged)


print ("SYNTACS: ", result)


print(nltk.pos_tag(nltk.word_tokenize(sentence))) 


from metaphone import doublemetaphone

print("PHONETICS:")
for i in DeletePunctuation(sentence).split():
	print(i,"->",doublemetaphone(i))

from polyglot.text import Text, Word
#from polyglot.downloader import downloader
#downloader.download("morph2.en")
print()
print("MORPHOLOGICAL:")
words = DeletePunctuation(sentence)
words = words.split()
for w in words:
  w = Word(w, language="en")
  print("{:<30}->{}".format(w, w.morphemes))

print("COLLOCATIONS: ")
for i in result:
	print(i)
	
