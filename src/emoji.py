import random

#Local Libraries
import symbols


angry_mouths =  ["0","益","▂","˛","⌒","△","︿","_","皿","ｪ","n","‿","Ĺ̯","Д","ω","ᆺ","▱๋","∀","^","Ω"," ͟ ͟ʖ","Ｏ","ヘ","ㅂ","言","⌓","人","Q","σ","罒","⌓","⚰","ε","曲","༡̇","ʍ","ム","﹏"]
misc_mouths = ["༬"]

angry_arms = [("凸","凸") , ("┌∩┐","┌∩┐"),("o","o"),("t","t"),("ヽ","ノ"),("ノ","ノ"),("＼","／"),("ヾ","ﾉ"),("┗","┛"),("ﾚ","ﾍ"),("╰","╯"),("╚╚","╝╝"),("」","」")]
angry_fists = [("٩","۶"),("ᕙ","ᕗ"),("ᕦ","ᕤ"),("٩","و"),("ฅ","ฅ"),("໒","७"),("ლ","ლ")]
why_arms = [("щ","щ")]

angry_eyes = [("◣","◢"),("ಠ","ಠ"),("｀","´"),("¬","¬"),("ಥ","ಥ"),("Ŏ","Ŏ"),("눈","눈"),("•᷅","•᷅"),("☀","☀"),("☢","☢"),("ᓀ","ᓂ"),("ಥ","ಥ"),("«○»","«○»"),("ŏ̥̥̥̥","ŏ̥̥̥̥")]
misc_eyes = [("º","º"),("≧","≦"),("￣","￣"),("ಠ","ರೃ"),("⋋","⋌"),("＞","＜"),("ò","ó"),("˃","˂"),("＠","＠"),("⇀","↼"),("◉","◉")]

face_bound = [("(",")"),("༼","༽"),("|","|"),("ʕ","ʔ")]
face_features = ["░","ﾒ","*","｡","╬","๑","＃","ヾ","o","メ",":"," ۜ ","＠"]

class Emoji:
	


	def __init__(self):
		self.emojiStr = ""
		self.emojiStack = [] #Use List as Stack

	def chooseTup(self,emojiset):

		faceTup = self.chooseRandom(emojiset)
		self.emojiStr += faceTup[0]
		self.emojiStack.append(faceTup[1])

	def chooseChar(self,emojiset):
		char = self.chooseRandom(emojiset)
		self.emojiStr += char


	def chooseRandom(self,emojiset):
		return emojiset[random.randrange(0,len(emojiset))]

	def getEmoji(self):
		while(self.emojiStack != []):
			self.emojiStr += (self.emojiStack).pop()

		return self.emojiStr


def main():
	emojimaker = Emoji()
	emojimaker.chooseTup(angry_arms)
	emojimaker.chooseTup(face_bound)
	emojimaker.chooseChar(face_features)
	emojimaker.chooseTup(angry_eyes)
	emojimaker.chooseChar(angry_mouths)

	print(emojimaker.getEmoji())

if __name__ == "__main__":
	main()