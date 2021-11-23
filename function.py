def display_contact(daftar_contact) :
    for contact in daftar_contact :
        print("=" * 20)
        print(f"Nama : {contact['nama']}")
        print(f"Email : {contact['email']}")
        print(f"Telepon : {contact['telepon']}")
        print(f"No. HP : {contact['no']}")

def new_contact() :
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon : ")
    no = input("No. HP : ")
    contact = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon,
        "no" : no
    }
    return contact

def cari_contact(daftar_contact) :
    cari_nama = input("Nama yang akan dicari : ")
    for contact in daftar_contact :
        nama = contact["nama"]
        if nama.lower().find(cari_nama.lower()) != -1 :
            print("=" * 20)
            print(f"Nama : {contact['nama']}")
            print(f"Email : {contact['email']}")
            print(f"Telepon : {contact['telepon']}")
            print(f"No. HP : {contact['no']}")

def delete_contact(daftar_contact) :
    nama = input("Nama yang akan di hapus : ")
    index = -1
    for i in range(0, len(daftar_contact)) :
        contact = daftar_contact[i]
        if nama == contact["nama"] :
            index = i
            break
    if index == -1 :
        print("Data yang anda minta tidak ditemukan")
    else :
        del daftar_contact[index]
        print("Anda telah berhasil menghapus data contact")