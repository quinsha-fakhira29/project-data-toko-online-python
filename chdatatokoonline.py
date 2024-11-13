import os
import random
import string

data = dict ()

while True:
    os.system("cls") # WIN
    # os.system("clear") # max/linux
    print(f"{'DATA TOKO ONLINE':_^30}")
    keyfinal = "".join(random.choice(string.ascii_uppercase)for i in range(3))
    toko_online = input("toko online\t\t:")
    membeli = input (" membeli\t\t:")
    harga = input ("harga\t\t:")

    data[keyfinal] = {
        'toko_online' :toko_online,
        'membeli' :membeli,
        'harga ' :harga
    }

    opsi = input(" input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-"*30)
print(f"key\t toko_online\membeli\harga")
print("-"*30)
for key,value in data.items():
    print (f"{key} \t {value.get('toko_onlinekey')} \t {value.get('membelikey')} \t {value.get('hargakey')}")