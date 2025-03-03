#hello_template = "Hallo, saya %s, Tinggal di %s"
#print(hello_template % ('Zidan', 'Kota Sukabumi'))
#nama = "riki hardianto"
#print(nama [-9:])
#print(nama [0])
#print(nama [0:4])
#print(nama [5:])
#print(nama [0:4])
#print(len(nama))

pernyataan = 'Riki, Dapa, Pariji, Ikbal, Sei'
word = pernyataan.split(',')
print(word)

def clean_word(word):
    return word.strip()
clean_word = list(map(clean_word))
print(clean_word)