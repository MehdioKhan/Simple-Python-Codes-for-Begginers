from os import system as sys
class Morse:
	codeList = {
		"A" : ".-", 
		"B" : "-...", 
		"C" : "-.-.", 
		"D" : "-..", 
		"E" : ".", 
		"F" : "..-.", 
		"G" : "--.", 
		"H" : "....", 
		"I" : "..", 
		"J" : ".---", 
		"K" : "-.-", 
		"L" : ".-..", 
		"M" : "--", 
		"N" : "-.", 
		"O" : "---", 
		"P" : ".--.", 
		"Q" : "--.-", 
		"R" : ".-.", 
		"S" : "...", 
		"T" : "-", 
		"U" : "..-", 
		"V" : "...-", 
		"W" : ".--", 
		"X" : "-..-", 
		"Y" : "-.--", 
		"Z" : "--..", 
		"0" : "-----", 
		"1" : ".----", 
		"2" : "..---", 
		"3" : "...--", 
		"4" : "....-", 
		"5" : ".....", 
		"6" : "-....", 
		"7" : "--...", 
		"8" : "---..", 
		"9" : "----.", 
		"." : ".-.-.-", 
		"," : "--..--"
	}

	def toMorse(self,str):
		result = ""
		for s in str:
			if(s==" "):
				result+=" / "
			else:
				result+=(self.codeList[s]+" ")
		return result
	def toText(self,str):
		result=""
		words=str.split(" / ")
		for w in words:
			chars=w.split(" ")
			for c in chars:
				for key in self.codeList.keys():
					if(self.codeList[key]==c):
						result+=key
			result+=" "
		return result
	def isMessageValid(self,str):
		for s in str:
			if(s!=" " and not s in self.codeList.keys()):
				return False
		return True
	def isMorseValid(self,str):
		words=str.split(" / ")
		for w in words:
			for c in w.split(" "):
				if(c in self.codeList.values()):	result = True
				else:	result = False
		return result
def main():
	print("OXY Morse Translator")
	morse=Morse()
	mode=input("Enter your choice :\n1.Encode 2.Decode :").lower()
	if(mode=='1' or mode=='encode'):
		message=input("Enter your message : ").upper()
		if(morse.isMessageValid(message)):
			print(morse.toMorse(message))
			print("Note: / separates words ")
		else:
			print("Error: Input contains invalid characters")
	elif(mode=='2' or mode=='decode'):
		message=input("Enter your Morse : ")
		if(morse.isMorseValid(message)):
			print(morse.toText(message))
		else:
			print("Error: Input contains invalid Morse")
main()
sys("pause")