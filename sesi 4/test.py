sentence = '''Tim Hukum KPK meminta penundaan sidang praperadilan jilid II Sekjen PDIP Hasto Kristiyanto terkait penetapan status tersangka. Kuasa hukum Hasto berharap penundaan itu bukan akal-akalan KPK untuk menyelesaikan berkas perkara.'''

sentence_2 = '''Tentu kita harapkan bahwa ini bukan akal-akalan ya, agar supaya KPK bisa menyelesaikan berkas perkara. Kemudian, mereka melimpahkan berkas perkara itu sehingga nanti seolah-olah permohonan praperadilan ini akan diputus dengan cara mengatakan bahwa ini sudah, apa ya, karena berkas perkaranya sudah digugurkan mengingat berkas perkara, perkara pokok, sudah dilimpahkan ke pengadilan," kata kuasa hukum Hasto, Maqdir Ismail, usai sidang di Pengadilan Negeri Jakarta Selatan'''

s1 = sentence.split(" ")
s2 = sentence_2.split(" ")
#print(s1[0:6])
#print(s2[0:6])
short_s1 = " ".join(s1[0:6])
short_s2 = " ".join(s2[0:6])
print(short_s1)
print(short_s2)