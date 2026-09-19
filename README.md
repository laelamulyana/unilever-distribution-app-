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
#urutan produk = [0,              1,       2,      3,     4,    5,    6,    ]
# Data Penjualan (k.Transaksi, outlet, wilayah, produk, ukuran, qty, subtotal)
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

cart=[]
riwayat_penjualan=[]

def tampilkan_produk():
   print('=' * 99)
   print(f"{'Index':<7} | {'Nama':<20} | {'Ukuran':<20} | {'Kategori':<15} | {'Stok':<10} | {'Harga':<10}| ")
   print('=' * 99)
   for i in range(len(produk_unilever)):
      print(f"{i}\t| {produk_unilever[i][0]:<20} | {produk_unilever[i][1]:<20} | {produk_unilever[i][2]:<15} | {produk_unilever[i][3]:<10} | {produk_unilever[i][4]:<10}| ")
   print("=" * 99)

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
               tampilkan_produk()
