from Kutya import Kutya

kutya1 = Kutya("Üstökös", "kan", "foxi keverék", 25, 11)
kutya2 = Kutya("Max", "kan", "corgi keverék", 20, 18)
kutya3 = Kutya("Vauli", "szuka", "tacskó keverék", 17, 8)
kutya = [kutya1, kutya2, kutya3]

i = 0
while i < len(kutya):
    aktualkuty = kutya[i]
    aktualkuty.tevekenyseg()
    i += 1


