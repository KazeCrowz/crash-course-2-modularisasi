# from geometri.segitiga import hitung_luas_segitiga
# import geometri.segitiga as gs
from Geometry.persegipanjang import hitung_persegipanjang, info as info_persegipanjang
from Geometry.segitiga import hitung_segitiga, info as info_segitiga

print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_segitiga(10, 3)}')

print(info_persegipanjang())
print(f'hitung_persegipanjang {hitung_persegipanjang(20, 10)}')
