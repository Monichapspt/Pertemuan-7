# Program Manajemen Kontak
import function

# List of dictionary
daftar_contact = []
daftar_contact.append({
    "nama" : "Monicha",
    "email" : "Monicha@gmail.com",
    "telepon" : "021-537351635",
    "no" : "081245764875"
})

# Menu Program
while True :
    print(" ")
    print("=" * 20)
    print("Daftar Menu")
    print("1. Daftar Contact")
    print("2. Tambah Contact")
    print("3. Cari Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("=" * 20)

    Menu = input("Silahkan Pilih Menu : ")
    print(" ")

    if Menu == "1" :
        function.display_contact(daftar_contact)
    elif Menu == "2" :
        contact = function.new_contact()
        daftar_contact.append(contact)
    elif Menu == "3" :
        function.cari_contact(daftar_contact)
    elif Menu == "4" :
        function.delete_contact(daftar_contact)
    elif Menu == "5" :
        break
    else :
        print("Maaf, menu tidak tersedia")

print("Terima kasih. Program telah keluar")