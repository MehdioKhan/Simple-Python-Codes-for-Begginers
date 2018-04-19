import os
class Cesar:
	dic={'0':'A','1':'B','2':'C','3':'D','4':'E','5':'F','6':'G','7':'H','8':'I',\
	'9':'J','10':'K','11':'L','12':'M','13':'N','14':'O','15':'P','16':'Q',\
	'17':'R','18':'S','19':'T','20':'U','21':'V','22':'W','23':'X','24':'Y','25':'Z'}
	def getKey(self,value):
		for k,v in self.dic.items():
			if v==value: return int(k)

	def encrypt(self,message,key):
		message=message.upper()
		result=''
		for c in message:
			if c.isalpha():
				result+=self.dic[str((self.getKey(c)+key)%25)]
			elif c==' ':
				result+=c
		return result
	def decrypt(self,message,key):
		message=message.upper()
		result=''
		for c in message:
			if c.isalpha():
				result+=self.dic[str((self.getKey(c)-key)%25)]
			else:
				result+=c
		return result
def main():
	c=Cesar()
	print("Welcome to Cesar Cipher text encrypter and decrypt.\
		\nuse following options for your operation")
	ch=input("1.Encrypt\n2.Decrypt\n")
	if ch=='1' or ch=='e' or ch.lower()=='encrypt':
		message=input("Enter your message to encrypt :")
		while True:
			key=input("Enter key ( from 0 to 25 ) :")
			if key.isdigit() and 0<=int(key) and int(key)<=25:
				key=int(key)
				break
		print("Encrypted message is :",c.encrypt(message,key))

	elif ch=='2' or ch=='d' or ch.lower()=='decrypt':
		message=input("Enter your message to decrypt :")
		while True:
			key=input("Enter key ( from 0 to 25 ) :")
			if key.isdigit() and 0<=int(key) and int(key)<=25:
				key=int(key)
				break
		print("Decrypted message is :",c.decrypt(message,key))
	else:
		print("Wrong choise!")
main()
os.system("pause")