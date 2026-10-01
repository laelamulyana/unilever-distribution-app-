produk_unilever = [
    ["Lifebuoy","100 ml", "Personal Care", 150, 3500],
    ["Sunsilk Shampoo", "100 ml" ,"Personal Care", 120, 15000],
    ["Pepsodent Pasta Gigi", "15 gram","Personal Care", 100, 12000],
    ["Rinso Deterjen","500 gram" ,"Home Care", 80, 18500],
    ["Molto","100 ml", "Home Care", 60, 22000],
    ["Sunlight","250 ml", "Home Care", 90, 14000],
    ["Bango Kecap Manis","100 ml", "Food & Beverage", 70, 21000],
    ["Royco Kaldu Ayam","20 gram","Food & Beverage", 110, 8500],
    ["Wall's Cornetto", "10 gram", "Food & Beverage", 200, 10000],
    ["Clear Shampoo","100 ml", "Personal Care", 50, 32000],
]
#urutan produk =[nama,ukuran/berat,kategori,stok,harga]
# uruta produk = [0,          1,      2,      3,     4, ]
#urutan produk = [0,              1,       2,      3,     4,    5,              6,    ]
# Data Penjualan (k.Transaksi, outlet, wilayah, produk, ukuran, qty terjual, subtotal)
History_penjualan = [
    ["a123879", "Indomaret Sudirman", "Jakarta", "Lifebuoy","100 ml", 20, 70000],
    ["x234687", "Alfamart Kemang", "Jakarta", "Rinso Deterjen", "500 gram", 10, 185000],
    ["y890755", "Toko Sinar Jaya", "Bandung", "Sunsilk Shampoo","100 ml", 15, 225000],
    ["p098724", "Indomaret Dago", "Bandung", "Bango Kecap Manis","100 ml", 8, 168000],
    ["q279278", "Alfamart Rungkut", "Surabaya", "Wall's Cornetto","10 gram",30, 300000],
    ["w263742", "Toko Makmur", "Surabaya", "Pepsodent Pasta Gigi","15 gram", 12, 144000],
    ["k982753", "Indomaret Sudirman", "Jakarta", "Molto","100 ml", 5, 110000],
    ["c293728", "Toko Sinar Jaya", "Bandung", "Royco Kaldu Ayam","20 gram", 25, 212500],
    ["k029374", "Alfamart Kemang", "Jakarta", "Sunlight","250 ml", 18, 252000],
    ["m203839", "Toko Makmur", "Surabaya", "Clear Shampoo","100 ml", 6, 192000],
]
#fungsi bantu
def cetak_header_produk():
   print('='*99)
   print(f"{'Index':<7} | {'Nama':<20} | {'Ukuran':<20} | {'Kategori':<15} | {'Stok':<10} | {'Harga':<10}| ")
   print('=' * 99)

def cetak_baris_produk(i):
   print(f"{i:<7} | {produk_unilever[i][0]:<20} | {produk_unilever[i][1]:<20} | {produk_unilever[i][2]:<15} | {produk_unilever[i][3]:<10} | {produk_unilever[i][4]:<10}| ")

def tampilkan_semua_produk():
   cetak_header_produk()
   for i in range(len(produk_unilever)):
      cetak_baris_produk(i)
   print("=" * 99)

def tampilkan_satu_produk(i):
   cetak_header_produk()
   cetak_baris_produk(i)
   print('='*99)

def input_angka(pesan):
   while True:
      nilai = input(pesan)
      if nilai.isdigit():
         return int(nilai)
      print('Input Harus Angka Bulat Positif')

#main menu

while True:
   Menu=input('''
   Unilever Distribution Apps
   1. Lihat Semua Data Produk
   2. Tambah Data Produk Baru
   3. Update Data Produk
   4. Hapus Data Produk
   5. Input Penjualan ke Outlet
   6. Lihat Riwayat Penjualan
   7. Laporan penjualan
   0.Keluar
   Masukkan Angka yang anda inginkan: ''')
   # 1.menu read
   if Menu == '1':
      while True:
         print('''
            Display Data Menu
            1. Lihat Semua Data
            2. Cari Produk (by Nama)
            3. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')
 
         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
            else:
               tampilkan_semua_produk()
 
         elif sub_menu == '2':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
            else:
               nama_cari = input('Masukkan nama produk yang dicari: ').strip()
               ketemu = False
               for i in range(len(produk_unilever)):
                  if produk_unilever[i][0].lower() == nama_cari.lower():
                     tampilkan_satu_produk(i)
                     ketemu = True
                     break
               if not ketemu:
                  print('Data yang dicari tidak ada.')
         elif sub_menu == '3':
               break   # kembali ke Main Menu
         else:
            print('Pilihan tidak valid!')
   # menu create
   elif Menu=='2':
      while True:
         print('''
            Create Data Menu
            1. Tambah Produk Baru
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            namaproduk = input('Masukkan Nama Produk Baru: ').strip()
            if namaproduk=='':
               print('Nama Produk Tidak Boleh Kosong')
               continue
            # cek duplikat
            double = False
            for i in produk_unilever:
               if i[0].lower() == namaproduk.lower():
                  double = True
                  break
            if double:
               print('Produk sudah ada! Silahkan coba lagi.\n')
               continue   # balik ke Create Menu (sesuai flowchart)
            ukuran = input('Masukkan Ukuran Produk: ')
            mapping_kategori={
               '1':'Personal Care',
               '2':'Home Care',
               '3':'Food & Beverage'
            }
            pilih_kategori = input('''Kategori Produk :
                     1. Personal Care
                     2. Home Care
                     3. Food & Beverage
                     Silahkan Pilih Kategori Produk: ''')
            if pilih_kategori not in mapping_kategori:
                  print('Pilihan kategori tidak valid!\n')
                  continue
            kategori = mapping_kategori[pilih_kategori]
            stok = input_angka('Silahkan Masukkan Stok produk: ')
            harga = input_angka('Silahkan Masukkan Harga Produk: ')
            simpan = input('Simpan data ini? (ya/tidak): ')
            if simpan.lower() == 'ya':
               produk_unilever.append([namaproduk, ukuran, kategori, stok, harga])
               print('Data berhasil disimpan!\n')
               tampilkan_semua_produk()
            else:
               print('Data dibatalkan.\n')
         elif sub_menu == '2':
            break   # kembali ke Main Menu
         else:
            print('Pilihan tidak valid!')
# update menu
   elif Menu=='3':
      while True:
         print('''
            Update Data Menu
            1. Update Produk
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')
 
         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
               continue
            tampilkan_semua_produk()
            #input primary key= index_produk
            index_produk = input_angka('Masukkan Index Produk Yang Ingin Diubah: ')
 # cek data exist (index valid)
            if index_produk < 0 or index_produk >= len(produk_unilever):
               print('Data yang Anda cari tidak ada.\n')
               continue
 # tampilkan data sesuai primary key
            print('Data yang dipilih:')
            tampilkan_satu_produk(index_produk)
            lanjut = input('Lanjutkan update? (ya/tidak): ')
            if lanjut.lower() != 'ya':
               continue   # balik ke Update Menu
            pilih_kolom = input('''Kolom Yang Ingin Diubah :
                              1. Ukuran
                              2. Stok
                              3. Harga
                              Pilih: ''')
            mapping_kolom = {'1': 1, '2': 3, '3': 4}
            if pilih_kolom not in mapping_kolom:
               print('Pilihan kolom tidak valid!\n')
               continue
            index_kolom = mapping_kolom[pilih_kolom]
            
            if index_kolom in (3, 4):
               value = input_angka('Masukkan nilai baru (angka): ')
            else:
               value = input('Masukkan ukuran baru: ').strip()
            konfirmasi = input('Update data ini? (ya/tidak): ')
            if konfirmasi.lower() == 'ya':
               produk_unilever[index_produk][index_kolom] = value
               print('Data berhasil diupdate!\n')
               tampilkan_semua_produk()
            else:
               print('Update dibatalkan.\n')
         elif sub_menu == '2':
               break   # kembali ke Main Menu
         else:
            print('Pilihan tidak valid!')
#  hapus data
   elif Menu=='4':
      while True:
         print('''
            Delete Data Menu
            1. Hapus Produk
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')
         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
               continue
            tampilkan_semua_produk()
            hapus = input_angka('Masukkan Index Produk Yang Ingin Dihapus: ')
         # cek data exist (index valid)
            if hapus < 0 or hapus >= len(produk_unilever):
               print('Data yang Anda cari tidak ada.\n')
               continue
            print('Data yang akan dihapus:')
            tampilkan_satu_produk(hapus)
            konfirmasi = input('Yakin hapus data ini? (ya/tidak): ')
            if konfirmasi.lower() == 'ya':
               del produk_unilever[hapus]
               print('Data berhasil dihapus!\n')
               tampilkan_semua_produk()
            else:
               print('Penghapusan dibatalkan.\n')
         elif sub_menu == '2':
            break   # kembali ke Main Menu
         else:
            print('Pilihan tidak valid!')
   #input penjualan outlet
   elif Menu=='5':
      while True:
         print('''
            Input Data Penjualan Outlet
            1. Input Data Penjualan Outlet
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')
         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
               continue
            #input data
            tampilkan_semua_produk()
            outlet = input('Masukkan Nama Outlet: ')
            wilayah = input('Masukkan Nama Wilayah: ')
            index = input_angka('Masukkan Indeks Produk yang Terjual: ')
            if index < 0 or index >= len(produk_unilever):
               print('Index produk tidak ditemukan.\n')
               continue
            qty = input_angka('Masukkan Jumlah Produk Terjual: ')
            if qty > produk_unilever[index][3]:
               print(f'Maaf Stok Tidak Mencukupi,\nStok Gudang Hanya {produk_unilever[index][3]}')
               continue
            elif qty<=0:
               print('Jumlah Harus lebih dari 0')
            else:
               nama_produk = produk_unilever[index][0]
               ukuran = produk_unilever[index][1]
               harga = produk_unilever[index][4]
               subtotal = qty * harga

               produk_unilever[index][3] -= qty   # kurangi stok

               kode_transaksi = 'TRX' + str(len(History_penjualan) + 1)   # kode simpel: TRX1, TRX2, dst
               History_penjualan.append([kode_transaksi, outlet, wilayah, nama_produk, ukuran, qty, subtotal])

               print(f'\nData Berhasil Ter-input!')
               print(f'Kode Transaksi: {kode_transaksi}')
               print(f'Produk: {nama_produk} | Qty: {qty} | Subtotal: {subtotal}')
         elif sub_menu == '2':
               break   # kembali ke Main Menu
         else:
            print('Pilihan tidak valid!')
# lihat riwayat penjualan
   elif Menu=='6':
      while True:
         print('''
               Riwayat Penjualan
               1. Riwayat Penjualan
               2. Kembali ke Menu Utama
               ''')
         sub_menu = input('Pilih opsi: ')
         if sub_menu == '1':
            if len(History_penjualan)==0:
               print('Belum Ada Riwayat Penjualan')
            else:
               kode_transaksi=input('Masukkan Kode Transaksi: ')
               ketemu=False
               for a in range(len(History_penjualan)):
                  if History_penjualan[a][0]== kode_transaksi:
                     print(f"{a:<7} | {History_penjualan[a][0]:<10} | {History_penjualan[a][1]:<20} | {History_penjualan[a][2]:<15} | {History_penjualan[a][3]:<20} | {History_penjualan[a][5]:<15} | {History_penjualan[a][6]:<12}|")
                     ketemu=True
               if not ketemu:
                  print('Kode transaksi berikut tidak ditemukan!')  
         elif sub_menu == '2':
            break   # kembali ke Main Menu
         else:
            print('Pilihan tidak valid!')        
            #  laporan penjualan        
   elif Menu == '7':
      while True:
         print('''
               Laporan Penjualan
               1. Laporan Penjualan
               2. Kembali ke Menu Utama
               ''')
         sub_menu = input('Pilih opsi: ')
         if sub_menu == '1':
            if len(History_penjualan) == 0:
               print('Belum ada data penjualan.')  
            else:
            # 1. TOTAL PENDAPATAN
               total_pendapatan = 0
               for a in range(len(History_penjualan)):
                  total_pendapatan += History_penjualan[a][6]
            # 2. PRODUK TERLARIS
               qty_per_produk = {}
               for a in range(len(History_penjualan)):
                  namaproduk = History_penjualan[a][3]
                  qty=History_penjualan[a][5]
                  if namaproduk in qty_per_produk:
                     qty_per_produk[namaproduk] += qty
                  else:
                     qty_per_produk[namaproduk] = qty
            
               produk_terlaris = max(qty_per_produk, key=qty_per_produk.get)
               qty_terlaris = qty_per_produk[produk_terlaris]

               # 3. WILAYAH TERBAIK
               total_per_wilayah = {}
               for a in range(len(History_penjualan)):
                  wilayah = History_penjualan[a][2]
                  total = History_penjualan[a][6]
                  if wilayah in total_per_wilayah:
                     total_per_wilayah[wilayah] += total
                  else:
                     total_per_wilayah[wilayah] = total
            
               wilayah_terbaik = max(total_per_wilayah, key=total_per_wilayah.get)
               total_wilayah_terbaik = total_per_wilayah[wilayah_terbaik]

               # 4. JUMLAH TRANSAKSI & RATA-RATA
               jumlah_transaksi = len(History_penjualan)
               rata_rata = total_pendapatan / jumlah_transaksi

               # TAMPILKAN
               print('\n' + '='*60)
               print('LAPORAN PENJUALAN')
               print('='*60)
               print(f'Jumlah Transaksi     : {jumlah_transaksi}')
               print(f'Total Pendapatan     : {total_pendapatan}')
               print(f'Rata-rata Transaksi  : {rata_rata:.0f}')
               print(f'Produk Terlaris      : {produk_terlaris} ({qty_terlaris} unit)')
               print(f'Wilayah Terbaik      : {wilayah_terbaik} (Total: {total_wilayah_terbaik})')
               print('='*60)
               break
         elif sub_menu == '2':
            break   # kembali ke Main Menu
         else:
            print('Pilihan tidak valid!')
   elif Menu=='0':
      print('Terimakasih,Sampai Jumpa!')
      break
   else:
      print('Pilihan yang anda masukkan tidak valid!')   
      print('=' * 99)


def cetak_baris_produk(i):
   print(f"{i:<7} | {produk_unilever[i][0]:<20} | {produk_unilever[i][1]:<20} | {produk_unilever[i][2]:<15} | {produk_unilever[i][3]:<10} | {produk_unilever[i][4]:<10}|")


def tampilkan_produk():
   cetak_header_produk()
   for i in range(len(produk_unilever)):
      cetak_baris_produk(i)
   print('=' * 99)


def tampilkan_satu_produk(i):
   cetak_header_produk()
   cetak_baris_produk(i)
   print('=' * 99)


def input_angka(pesan):
   # minta input sampai user mengetik angka bulat positif (supaya tidak crash)
   while True:
      nilai = input(pesan)
      if nilai.isdigit():
         return int(nilai)
      print('Input harus berupa angka bulat positif!')


# ---------------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------------
while True:
   Menu = input('''
   Unilever Distribution Apps
   1. Lihat Semua Data Produk
   2. Tambah Data Produk Baru
   3. Update Data Produk
   4. Hapus Data Produk
   5. Input Penjualan ke Outlet
   6. Lihat Riwayat Penjualan
   7. Laporan penjualan
   0. Keluar
   Masukkan Angka yang anda inginkan: ''')

   # ===========================================================
   # 1. READ MENU
   # ===========================================================
   if Menu == '1':
      while True:
         print('''
            Display Data Menu
            1. Lihat Semua Data
            2. Cari Produk (by Nama)
            3. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
            else:
               tampilkan_produk()

         elif sub_menu == '2':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
            else:
               nama_cari = input('Masukkan nama produk yang dicari: ').strip()
               ketemu = False
               for i in range(len(produk_unilever)):
                  if produk_unilever[i][0].lower() == nama_cari.lower():
                     tampilkan_satu_produk(i)
                     ketemu = True
                     break
               if not ketemu:
                  print('Data tidak ada.')

         elif sub_menu == '3':
            break   # kembali ke Main Menu

         else:
            print('Pilihan tidak valid!')

   # ===========================================================
   # 2. CREATE MENU
   # ===========================================================
   elif Menu == '2':
      while True:
         print('''
            Create Data Menu
            1. Tambah Produk Baru
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            # input primary key (nama produk)
            namaproduk = input('Masukkan Nama Produk Baru: ').strip()
            if namaproduk == '':
               print('Nama produk tidak boleh kosong!\n')
               continue

            # cek duplikat
            double = False
            for p in produk_unilever:
               if p[0].lower() == namaproduk.lower():
                  double = True
                  break
            if double:
               print('Data sudah ada! Silahkan coba lagi.\n')
               continue   # balik ke Create Menu

            # input data selain primary key
            ukuran = input('Masukkan Ukuran Produk: ').strip()
            pilih_kategori = input('''Kategori Produk :
                     1. Personal Care
                     2. Home Care
                     3. Food & Beverage
                     Silahkan Pilih Kategori Produk: ''')
            daftar_kategori = {'1': 'Personal Care', '2': 'Home Care', '3': 'Food & Beverage'}
            if pilih_kategori not in daftar_kategori:
               print('Kategori tidak valid!\n')
               continue
            kategori = daftar_kategori[pilih_kategori]
            stok = input_angka('Silahkan Masukkan Stok produk: ')
            harga = input_angka('Silahkan Masukkan Harga Produk: ')

            # opsi simpan data
            simpan = input('Simpan data ini? (ya/tidak): ')
            if simpan.lower() == 'ya':
               produk_unilever.append([namaproduk, ukuran, kategori, stok, harga])
               print('Data berhasil disimpan!\n')
               tampilkan_produk()
            else:
               print('Data dibatalkan.\n')
            # selesai -> otomatis kembali ke Create Menu (loop)

         elif sub_menu == '2':
            break   # kembali ke Main Menu

         else:
            print('Pilihan tidak valid!')

   # ===========================================================
   # 3. UPDATE MENU
   # ===========================================================
   elif Menu == '3':
      while True:
         print('''
            Update Data Menu
            1. Update Produk
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
               continue
            tampilkan_produk()

            # input primary key (index produk)
            index_produk = input_angka('Masukkan Index Produk Yang Ingin Diubah: ')
            if index_produk >= len(produk_unilever):
               print('Data yang Anda cari tidak ada.\n')
               continue   # balik ke Update Menu

            # tampilkan data sesuai primary key
            print('Data yang dipilih:')
            tampilkan_satu_produk(index_produk)

            # lanjut update?
            lanjut = input('Lanjutkan update? (ya/tidak): ')
            if lanjut.lower() != 'ya':
               continue   # balik ke Update Menu

            # pilih kolom yang diubah
            pilih_kolom = input('''Kolom Yang Ingin Diubah :
                              1. Ukuran
                              2. Stok
                              3. Harga
                              Pilih: ''')
            mapping_kolom = {'1': 1, '2': 3, '3': 4}
            if pilih_kolom not in mapping_kolom:
               print('Pilihan kolom tidak valid!\n')
               continue
            index_kolom = mapping_kolom[pilih_kolom]

            # input nilai baru
            if index_kolom in (3, 4):
               value = input_angka('Masukkan nilai baru (angka): ')
            else:
               value = input('Masukkan ukuran baru: ').strip()

            # konfirmasi update (berlaku untuk SEMUA kolom)
            konfirmasi = input('Update data ini? (ya/tidak): ')
            if konfirmasi.lower() == 'ya':
               produk_unilever[index_produk][index_kolom] = value
               print('Data berhasil diupdate!\n')
               tampilkan_produk()
            else:
               print('Update dibatalkan.\n')
            # selesai -> otomatis kembali ke Update Menu (loop)

         elif sub_menu == '2':
            break   # kembali ke Main Menu

         else:
            print('Pilihan tidak valid!')

   # ===========================================================
   # 4. DELETE MENU
   # ===========================================================
   elif Menu == '4':
      while True:
         print('''
            Delete Data Menu
            1. Hapus Produk
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
               continue
            tampilkan_produk()

            # input primary key (index produk)
            hapus = input_angka('Masukkan Index Produk Yang Ingin Dihapus: ')
            if hapus >= len(produk_unilever):
               print('Data yang Anda cari tidak ada.\n')
               continue   # balik ke Delete Menu

            # opsi hapus data
            print('Data yang akan dihapus:')
            tampilkan_satu_produk(hapus)
            konfirmasi = input('Yakin hapus data ini? (ya/tidak): ')
            if konfirmasi.lower() == 'ya':
               del produk_unilever[hapus]
               print('Data berhasil dihapus!\n')
               tampilkan_produk()
            else:
               print('Penghapusan dibatalkan.\n')
            # selesai -> otomatis kembali ke Delete Menu (loop)

         elif sub_menu == '2':
            break   # kembali ke Main Menu

         else:
            print('Pilihan tidak valid!')

   # ===========================================================
   # 5. INPUT PENJUALAN OUTLET
   # ===========================================================
   elif Menu == '5':
      while True:
         print('''
            Input Data Penjualan Outlet
            1. Input Data Penjualan Outlet
            2. Kembali ke Menu Utama
            ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            if len(produk_unilever) == 0:
               print('Data tidak ada.')
               continue
            tampilkan_produk()
            outlet = input('Masukkan Nama Outlet: ').strip()
            wilayah = input('Masukkan Nama Wilayah: ').strip()
            if outlet == '' or wilayah == '':
               print('Nama outlet dan wilayah tidak boleh kosong!\n')
               continue
            index = input_angka('Masukkan Indeks Produk yang Terjual: ')
            if index >= len(produk_unilever):
               print('Data yang Anda cari tidak ada.\n')
               continue
            qty = input_angka('Masukkan Jumlah Produk Terjual: ')
            if qty <= 0:
               print('Jumlah harus lebih dari 0!\n')
               continue

            if qty > produk_unilever[index][3]:
               print(f'Maaf Stok Tidak Mencukupi,\nStok Gudang Hanya {produk_unilever[index][3]}')
            else:
               nama_produk = produk_unilever[index][0]
               ukuran = produk_unilever[index][1]
               harga = produk_unilever[index][4]
               subtotal = qty * harga

               produk_unilever[index][3] -= qty   # kurangi stok

               kode_transaksi = 'TRX' + str(len(History_penjualan) + 1)
               History_penjualan.append([kode_transaksi, outlet, wilayah, nama_produk, ukuran, qty, subtotal])

               print('\nData Berhasil Ter-input!')
               print(f'Kode Transaksi: {kode_transaksi}')
               print(f'Produk: {nama_produk} | Qty: {qty} | Subtotal: {subtotal}')

         elif sub_menu == '2':
            break   # kembali ke Main Menu

         else:
            print('Pilihan tidak valid!')

   # ===========================================================
   # 6. RIWAYAT PENJUALAN
   # ===========================================================
   elif Menu == '6':
      while True:
         print('''
               Riwayat Penjualan
               1. Riwayat Penjualan
               2. Kembali ke Menu Utama
               ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            if len(History_penjualan) == 0:
               print('Belum Ada Riwayat Penjualan')
            else:
               kode_transaksi = input('Masukkan Kode Transaksi: ').strip()
               ketemu = False
               for a in range(len(History_penjualan)):
                  if History_penjualan[a][0] == kode_transaksi:
                     if not ketemu:
                        print('Transaksi Ditemukan, Berikut Riwayat Transaksinya')
                        print('=' * 118)
                        print(f"{'Index':<7} | {'Kode':<10} | {'Outlet':<20} | {'Wilayah':<15} | {'Produk':<20} | {'Qty':<15} | {'Subtotal':<12}|")
                        print('=' * 118)
                     print(f"{a:<7} | {History_penjualan[a][0]:<10} | {History_penjualan[a][1]:<20} | {History_penjualan[a][2]:<15} | {History_penjualan[a][3]:<20} | {History_penjualan[a][5]:<15} | {History_penjualan[a][6]:<12}|")
                     ketemu = True
               # dicek SETELAH loop selesai
               if ketemu:
                  print('=' * 118)
               else:
                  print('Kode transaksi berikut tidak ditemukan!')

         elif sub_menu == '2':
            break   # kembali ke Main Menu

         else:
            print('Pilihan tidak valid!')

   # ===========================================================
   # 7. LAPORAN PENJUALAN
   # ===========================================================
   elif Menu == '7':
      while True:
         print('''
               Laporan Penjualan
               1. Lihat Laporan Penjualan
               2. Kembali ke Menu Utama
               ''')
         sub_menu = input('Pilih opsi: ')

         if sub_menu == '1':
            if len(History_penjualan) == 0:
               print('Belum ada data penjualan.')
            else:
               # 1. total pendapatan
               total_pendapatan = 0
               for a in range(len(History_penjualan)):
                  total_pendapatan += History_penjualan[a][6]

               # 2. produk terlaris
               qty_per_produk = {}
               for a in range(len(History_penjualan)):
                  nama = History_penjualan[a][3]
                  qty = History_penjualan[a][5]
                  if nama in qty_per_produk:
                     qty_per_produk[nama] += qty
                  else:
                     qty_per_produk[nama] = qty
               produk_terlaris = max(qty_per_produk, key=qty_per_produk.get)
               qty_terlaris = qty_per_produk[produk_terlaris]

               # 3. wilayah terbaik
               total_per_wilayah = {}
               for a in range(len(History_penjualan)):
                  wil = History_penjualan[a][2]
                  total = History_penjualan[a][6]
                  if wil in total_per_wilayah:
                     total_per_wilayah[wil] += total
                  else:
                     total_per_wilayah[wil] = total
               wilayah_terbaik = max(total_per_wilayah, key=total_per_wilayah.get)
               total_wilayah_terbaik = total_per_wilayah[wilayah_terbaik]

               # 4. jumlah transaksi & rata-rata
               jumlah_transaksi = len(History_penjualan)
               rata_rata = total_pendapatan / jumlah_transaksi

               print('\n' + '=' * 60)
               print('LAPORAN PENJUALAN')
               print('=' * 60)
               print(f'Jumlah Transaksi     : {jumlah_transaksi}')
               print(f'Total Pendapatan     : {total_pendapatan}')
               print(f'Rata-rata Transaksi  : {rata_rata:.0f}')
               print(f'Produk Terlaris      : {produk_terlaris} ({qty_terlaris} unit)')
               print(f'Wilayah Terbaik      : {wilayah_terbaik} (Total: {total_wilayah_terbaik})')
               print('=' * 60)

         elif sub_menu == '2':
            break   # kembali ke Main Menu

         else:
            print('Pilihan tidak valid!')

   # ===========================================================
   # 0. KELUAR
   # ===========================================================
   elif Menu == '0':
      print('Terima kasih, sampai jumpa!')
      break

   # ===========================================================
   # INPUT TIDAK VALID -> notifikasi lalu kembali ke menu utama
   # ===========================================================
   else:
      print('Pilihan yang Anda masukkan tidak valid!')
