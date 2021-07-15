laporan_minuman = [
    {
        'nama': 'kopi',
        'harga': '11000',
        'terjual': '10',
        'modal_satuan': '6000',
    },
    {
        'nama': 'teh_ES',
        'harga': '6000',
        'terjual': '12',
        'modal_satuan': '3500',
    },
    {
        'nama': 'jus',
        'harga': '10000',
        'terjual': '7',
        'modal_satuan': '6000',
    },
] # tidak ada yg perlu dibuah dsn

# isi list makanan dan untuk nama, harga, terjual, modal satuan bebas tetapi diinput melalui terminal (cukup 2 makanan)
laporan_makanan = [] # format makanan samad dengan minuman
"""
format makanan
{
        'nama': '',
        'harga': '',
        'terjual': '',
        'modal_satuan': ,
}
"""

penjualan = {
    'minuman': laporan_minuman,
    'makanan': laporan_makanan,
    'summary': {
        'total_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':''
        },
        'keuntungan_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':'',
        },
        'special_case':'total_semua_penjualan+total_semua_keuntungan_penjualan+special_value+10000' # juga tidak ada yg perlu diubah dsn
    }
}

# lakukan programn didalam fungsi ini
def main():
    global minuman, makanan, penjualan
    special_value = 1910952006 # ex: special_value = 2011512010
    print("Semangat Upgrading, Machine Learning Semangat")
    
    laporanmakanan = dict()
    for a in range(2) :
        nama_makanan = input("Nama Makanan : ")
        harga_makanan = int(input("Harga Makanan : "))
        makanan_terjual = int(input("Jumlah Makanan : "))
        modal_makanan = int(input("Modal Makanan : "))
        laporanmakanan = {'nama':nama_makanan, 'harga':harga_makanan, 'terjual':makanan_terjual, 'modal_satuan':modal_makanan}
        laporan_makanan.append(laporanmakanan)

    
    penjualan['summary']['total_penjualan']['makanan'] = penjualan['makanan'][0]['terjual'] + penjualan['makanan'][1]['terjual']
    penjualan['summary']['total_penjualan']['minuman'] = int(penjualan['minuman'][0]['terjual']) + int(penjualan['minuman'][1]['terjual']) + int(penjualan['minuman'][2]['terjual'])
    penjualan['summary']['total_penjualan']['semua'] = int(penjualan['summary']['total_penjualan']['makanan']) + int(penjualan['summary']['total_penjualan']['minuman'])
    total_semua_penjualan = penjualan['summary']['total_penjualan']['semua'] # juga tidak ada yg perlu diubah dsn
    print("Total penjualan makanan dan minuman : ", total_semua_penjualan)

    penjualan['summary']['keuntungan_penjualan']['makanan'] = (penjualan['makanan'][0]['terjual']*(penjualan['makanan'][0]['harga']-penjualan['makanan'][0]['modal_satuan'])) + \
         (penjualan['makanan'][1]['terjual']*(penjualan['makanan'][1]['harga']-penjualan['makanan'][1]['modal_satuan']))
    penjualan['summary']['keuntungan_penjualan']['minuman'] = int(penjualan['minuman'][0]['terjual'])*(int(penjualan['minuman'][0]['harga']) - \
        int(penjualan['minuman'][0]['modal_satuan'])) + int(penjualan['minuman'][1]['terjual'])*(int(penjualan['minuman'][1]
                                                     ['harga'])-int(penjualan['minuman'][1]['modal_satuan'])) + int(penjualan['minuman'][2]['terjual'])*(int(penjualan['minuman'][2]
                                                     ['harga'])-int(penjualan['minuman'][2]['modal_satuan']))
    penjualan['summary']['keuntungan_penjualan']['semua'] = int(penjualan['summary']['keuntungan_penjualan']['makanan'] + penjualan['summary']['keuntungan_penjualan']['minuman'])
    total_semua_keuntungan_penjualan = penjualan['summary']['keuntungan_penjualan']['semua'] # juga tidak ada yg perlu diubah dsn
    print("Total Keuntungan penjualan : ", total_semua_keuntungan_penjualan)

    penjualan['summary']['special_case'] = total_semua_penjualan + total_semua_keuntungan_penjualan + special_value + 10000
    special_case = penjualan['summary']['special_case'] # perlu sedikit penambahan
    print("Special Case : ", special_case)
    
   
    penjualan['summary']['keuntungan_penjualan']['semua'] = int(penjualan['summary']['keuntungan_penjualan']['makanan']) + \
        int(penjualan['summary']['keuntungan_penjualan']['minuman'])
    print('laporan penjualan makanan')
    print(penjualan['makanan'])
    print('laporan penjualan minuman')
    print(penjualan['minuman'])

    
if __name__ == "__main__":
    main()
