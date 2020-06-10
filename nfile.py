import requests,os

os.system("clear")
print("made by ")
os.system("figlet Tricker")
k = input("enter file name : ")
os.system("touch "+k)
r = input("enter url : ")
l = requests.get(r)
with open(k, "wb") as p:
	p.write(l.content)