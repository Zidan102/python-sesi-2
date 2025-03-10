useradmin, passadmin = "admin", "admin123"
useruser, passuser = "user", "user123"
userguest = "guest"

inuser = input("Masukan username anda: ")
inpass = input("Masukan Passwordnya(Kosongkan bila anda adalah guest): ")
if inuser == useradmin and inpass == passadmin:
    kategori = "akses admin"
elif inuser == useruser and inpass == passuser:
    kategori = "akses terbatas"
elif inuser == userguest:
    kategori = "akses minimal"
else:
    kategori = "akses ditolak"
print("%s, itu adalah akses yang kamu dapatkan." % (kategori))