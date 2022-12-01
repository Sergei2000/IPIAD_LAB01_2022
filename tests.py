import Analyzer
from Analyzer import *
import configparser

new = """

When Australia’s richest woman Gina Rinehart threw a financial lifeline to Netball Australia, she triggered a debate about sponsorships and the role of social and political issues in the sporting sphere. Then she walked away.

Rinehart’s bombshell decision to withdraw a 14 million Australian dollar ($8.9 million) sponsorship deal for the Diamonds, Australia’s national netball team, caught the players off-guard and struck a blow to the future of Netball Australia – a sporting body mired in debt.

The drama engulfing the Diamonds is not new, but experts say disputes could become more common as athletes and fans take a stronger stance on the source of sponsorship money.
"""

m = MorphAnalyzer(lang="en")
print("MORPHOLOGICAL:")
print(m.GetSpeechPartsStupid(new))
print(m.GetMorphemInfo(new))

another_config = configparser.ConfigParser()
another_config.read('simple.conf')
m = SyntaxAnalyzer(pattern=another_config["Syntax"]["rule"])
sentence = """When Australia’s richest woman Gina Rinehart threw a financial lifeline to Netball Australia, she triggered a debate about sponsorships and the role of social and political issues in the sporting sphere."""
print("SYNTAX:")
print(m.GetTextTrees(new))

print("PHONETICS:")
m = PhoneticAnalysys()
print(m.GetPhoneticAnalysys(sentence))

print("COLLOCATIONS :")
sentences = nltk.tokenize.sent_tokenize(new)
m =SyntaxAnalyzer(pattern=another_config["Syntax"]["rule"])
m.GetSentenceTree(sentences[3]).draw()
GetCollocations(m.GetSentenceTree(sentences[3]))
	



