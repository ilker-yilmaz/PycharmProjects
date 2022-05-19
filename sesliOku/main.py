from gtts import gTTS
import os
dosya=open("C:/Users/eymen/Desktop/deneme.txt","r",encoding="utf8").read().replace("\n"," ")
dil="tr"
cikti=gTTS(text=str(dosya),lang=dil,slow=False)
cikti.save("C:/Users/eymen/Desktop/deneme.mp3")
os.system("Start deneme.mp3")

