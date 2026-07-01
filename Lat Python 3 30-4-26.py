print(' ~•------------------------------•~')
print(' | Lat 3 30/4/26 | Mini Menu Game |\n ---- ChatGPT Idea')
print(' ~•------------------------------•~')
print(''' === MINI MENU GAME ===

 1. Lihat daftar buah
 2. Tebak angka genap
 3. Keluar''')
while True:
        try:
        	Z1=int(input('\n ( 1 / 2 / 3 )\n\n ?..... '))
        	break
        except:
        		print('\n Tolong Masukan Angka, Bukan Huruf')
        
while Z1 not in [1,2,3]:
	print('\n Tolong jawab yang benar')
	while True:
		try:
			Z1=int(input('\n ( 1 / 2 / 3 )\n\n ?..... '))
			break
		except:
			print('\n Tolong Masukan Angka, Bukan Huruf')
if Z1 == 1:
	print(' ~•------------------------------•~')
	print(' Daftar Buah:\n ')
	A=['Apel','Mangga','Jeruk']
	for i in range(len(A)):
		print('',i+1,'.',A[i])
	print(' ~•------------------------------•~')
elif Z1 == 2:
	import random
	B= random.choice([2,4,6,8,10])
	print(' ~•------------------------------•~')
	while True:
		try:
			C=int(input(' Apa tebakanmu?   '))
			break
		except:
			print('\n Tolong Masukan Angka, Bukan Huruf')
		
	while B!=C:
		print(' \n Salah, coba lagi')
		print(' ~•------------------------------•~')
		while True:
			try:
				C=int(input(' Apa tebakanmu?   '))
				break
			except:
				print('\n Tolong Masukan Angka, Bukan Huruf')
				
	print(' \n Selamat, anda benar')
	print(' ~•------------------------------•~')

elif Z1 == 3:
	print('\n Program selesai. Terima kasih!')
	print(' ~•------------------------------•~\n Tugas 1 Hari yang Diselesaikan 3 Hari 🤫😂')
	print(' ~•------------------------------•~')

# Tugas Besar: Mini Menu Game

# Menu utama:
# 1. Lihat daftar buah
# 2. Tebak angka genap
# 3. Keluar

# Menu 1:
# Gunakan list buah = ["Apel", "Mangga", "Jeruk"]
# Tampilkan:
# 1. Apel
# 2. Mangga
# 3. Jeruk

# Menu 2:
# Program memilih angka acak genap dari:
# 2, 4, 6, 8, 10

# User menebak angka sampai benar
# Jika salah:
# "Salah, coba lagi"

# Jika benar:
# "Selamat, anda benar"

# Menu 3:
# Tampilkan:
# "Program selesai. Terima kasih!"

# Validasi input:
# Jika user input selain 1 / 2 / 3
# tampilkan:
# "Tolong jawab yang benar!"
# lalu ulang input