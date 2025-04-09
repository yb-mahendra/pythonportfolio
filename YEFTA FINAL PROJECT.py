import random

# ---------- Data Awal ----------
data_nasabah = [
     {
        "Nomor": 1,
        "Nama": "Andi Saputra",
        "CIF": "9392645866",
        "Jenis Kredit": "Kredit Modal Kerja",
        "Maksimum Kredit": 250000000,
        "No HP": "081234567891",
        "Alamat": "Jl. Merdeka No.81, Kulon Progo, DIY"
    },
    {
        "Nomor": 2,
        "Nama": "Siti Aminah",
        "CIF": "9096190924",
        "Jenis Kredit": "Kredit Pemilikan Rumah",
        "Maksimum Kredit": 500000000,
        "No HP": "081234567892",
        "Alamat": "Jl. Sudirman No.62, Bantul, DIY"
    },
    {
        "Nomor": 3,
        "Nama": "Budi Hartono",
        "CIF": "9049658877",
        "Jenis Kredit": "Kredit Kendaraan Bermotor",
        "Maksimum Kredit": 150000000,
        "No HP": "081234567893",
        "Alamat": "Jl. Diponegoro No.73, Sleman, DIY"
    },
    {
        "Nomor": 4,
        "Nama": "Dewi Lestari",
        "CIF": "9221764302",
        "Jenis Kredit": "Kredit Modal Kerja",
        "Maksimum Kredit": 100000000,
        "No HP": "081234567894",
        "Alamat": "Jl. Gajah Mada No.45, Gunung Kidul, DIY"
    },
    {
        "Nomor": 5,
        "Nama": "Rudi Gunawan",
        "CIF": "9197694258",
        "Jenis Kredit": "Kredit Pemilikan Rumah",
        "Maksimum Kredit": 750000000,
        "No HP": "081234567895",
        "Alamat": "Jl. Siliwangi No.52, Kota Yogyakarta, DIY"
    },
    {
        "Nomor": 6,
        "Nama": "Lina Marlina",
        "CIF": "9049584891",
        "Jenis Kredit": "Kredit Modal Kerja",
        "Maksimum Kredit": 300000000,
        "No HP": "081234567896",
        "Alamat": "Jl. Ahmad Yani No.69, Sleman, DIY"
    },
    {
        "Nomor": 7,
        "Nama": "Hendra Wijaya",
        "CIF": "9049660818",
        "Jenis Kredit": "Kredit Multiguna",
        "Maksimum Kredit": 200000000,
        "No HP": "081234567897",
        "Alamat": "Jl. Hasanuddin No.74, Kota Yogyakarta, DIY"
    },
]

# ---------- Utility ----------
def generate_cif_unik(data):
    existing_cif = {nasabah["CIF"] for nasabah in data}
    while True:
        angka_acak = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        cif_baru = "94" + angka_acak
        if cif_baru not in existing_cif:
            return cif_baru

def tampilkan_tabel(data):
    if not data:
        print("Tidak ada data untuk ditampilkan.")
        return
    header = f"{'No':<4}{'Nama':<20}{'CIF':<12}{'Jenis Kredit':<25}{'Maks Kredit':<15}{'No HP':<15}{'Alamat'}"
    print(header)
    print("=" * len(header))
    for d in data:
        print(f"{d['Nomor']:<4}{d['Nama']:<20}{d['CIF']:<12}{d['Jenis Kredit']:<25}{d['Maksimum Kredit']:<15}{d['No HP']:<15}{d['Alamat']}")

# ---------- Menu Fungsional ----------
def tampilkan_semua(data):
    print("\n📄 Daftar Nasabah:")
    tampilkan_tabel(data)

def filter_jenis_kredit(data):
    jenis = input("Masukkan jenis kredit (case sensitive): ")
    hasil = [d for d in data if d['Jenis Kredit'] == jenis]
    print(f"\n📑 Hasil filter jenis kredit: {jenis}")
    tampilkan_tabel(hasil)

def filter_maks_kredit(data):
    try:
        batas = int(input("Masukkan batas minimum maksimum kredit: "))
        hasil = [d for d in data if d['Maksimum Kredit'] > batas]
        print(f"\n📑 Hasil filter maksimum kredit di atas {batas}")
        tampilkan_tabel(hasil)
    except ValueError:
        print("Masukkan angka yang valid.")

def tambah_nasabah(data):
    try:
        nama = input("Nama: ")
        jenis_kredit = input("Jenis Kredit: ")
        maks_kredit = int(input("Maksimum Kredit: "))
        no_hp = input("No HP: ")
        alamat = input("Alamat: ")
        cif = generate_cif_unik(data)
        nomor = len(data) + 1

        data.append({
            "Nomor": nomor,
            "Nama": nama,
            "CIF": cif,
            "Jenis Kredit": jenis_kredit,
            "Maksimum Kredit": maks_kredit,
            "No HP": no_hp,
            "Alamat": alamat
        })
        print(f"\n✅ Nasabah ditambahkan. CIF: {cif}")
    except ValueError:
        print("Input tidak valid. Maksimum kredit harus berupa angka.")

def edit_nasabah(data):
    try:
        no = int(input("Masukkan Nomor Urut Nasabah yang ingin diedit: "))
        nasabah = next((d for d in data if d['Nomor'] == no), None)
        if nasabah:
            print(f"🛠️ Edit data untuk: {nasabah['Nama']} (CIF: {nasabah['CIF']})")
            nasabah["Nama"] = input(f"Nama [{nasabah['Nama']}]: ") or nasabah["Nama"]
            nasabah["Jenis Kredit"] = input(f"Jenis Kredit [{nasabah['Jenis Kredit']}]: ") or nasabah["Jenis Kredit"]
            maks = input(f"Maksimum Kredit [{nasabah['Maksimum Kredit']}]: ")
            if maks: nasabah["Maksimum Kredit"] = int(maks)
            nasabah["No HP"] = input(f"No HP [{nasabah['No HP']}]: ") or nasabah["No HP"]
            nasabah["Alamat"] = input(f"Alamat [{nasabah['Alamat']}]: ") or nasabah["Alamat"]
            print("✅ Data berhasil diperbarui.")
        else:
            print("Nomor urut tidak ditemukan.")
    except ValueError:
        print("Masukkan angka yang valid untuk nomor atau maksimum kredit.")

def hapus_nasabah(data):
    try:
        no = int(input("Masukkan Nomor Urut Nasabah yang ingin dihapus: "))
        index = next((i for i, d in enumerate(data) if d["Nomor"] == no), None)
        if index is not None:
            konfirmasi = input(f"Yakin ingin menghapus {data[index]['Nama']}? (y/n): ")
            if konfirmasi.lower() == 'y':
                data.pop(index)
                for idx, d in enumerate(data):  # Re-numbering
                    d["Nomor"] = idx + 1
                print("✅ Data berhasil dihapus.")
            else:
                print("❌ Penghapusan dibatalkan.")
        else:
            print("Nomor urut tidak ditemukan.")
    except ValueError:
        print("Masukkan angka yang valid.")

# ---------- Menu Utama ----------
def menu_interaktif():
    while True:
        print("\n📋 CREDIT MANAGEMENT SYSTEM")
        print("1. Tampilkan Daftar Nasabah")
        print("2. Filter Jenis Kredit")
        print("3. Filter Maksimum Kredit")
        print("4. Tambah Data Nasabah")
        print("5. Edit Data Nasabah")
        print("6. Hapus Data Nasabah")
        print("7. Exit")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            tampilkan_semua(data_nasabah)
        elif pilihan == "2":
            filter_jenis_kredit(data_nasabah)
        elif pilihan == "3":
            filter_maks_kredit(data_nasabah)
        elif pilihan == "4":
            tambah_nasabah(data_nasabah)
        elif pilihan == "5":
            edit_nasabah(data_nasabah)
        elif pilihan == "6":
            hapus_nasabah(data_nasabah)
        elif pilihan == "7":
            print("👋 Terima kasih. Program selesai.")
            break
        else:
            print("⚠️ Pilihan tidak valid. Coba lagi.")

menu_interaktif()

if __name__ == "__main__":
    menu_interaktif()

