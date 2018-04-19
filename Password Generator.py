#OXY Password Generator
#Khan

import random,os

def password(n):
	upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lower="abcdefghijklmnopqrstuvwxyz"
	numbers="0123456789"
	special="~!@#$%^&*+_-=()[]/., "
	chars=[upper,lower,numbers,special]
	res=""
	for i in range(int(n)):
		res+=random.choice(chars[random.randrange(0,4,1)])
	return res

def main():
	print("Welcome to OXY Password Generator !\n")
	lenght=input("Enter lenght of password :\n")
	print("Generated password is :\n")
	print(password(lenght)+"\n")
main()
os.system("pause")
