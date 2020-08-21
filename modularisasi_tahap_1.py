"""
program menghitung luas segitiga
luas_segitiga = alas * tinggi / 2
"""
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luas {luas_segitiga}')

alas = 20
tinggi = 4
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luas {luas_segitiga}')


# Menghitung segitiga dengan fungsi
def hitung_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 6
print(f'\nDengan fungsi, Segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luas {hitung_segitiga(alas, tinggi)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_segitiga(20, 4)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_segitiga(8, 4)}')
