#!/usr/bin/env python
# coding: utf-8

# In[11]:


def hitung_fpb(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def hitung_kpk(x, y):
    if x == 0 or y == 0:
        return 0
    kpk = max(x, y)
    while True:
        if kpk % x == 0 and kpk % y == 0:
            return kpk
        kpk += 1

def menu():
    print("Pilihan menu:")
    print("1. Menghitung FPB")
    print("2. Menghitung KPK")
    print("3. Selesai")

def main():
    while True:
        menu()
        try:
            pilihan = int(input("Masukkan pilihan Anda: "))
        except ValueError:
            print("Input tidak valid, silakan masukkan bilangan bulat.")
            continue

        if pilihan == 1:
            try:
                x = int(input("Masukkan bilangan pertama: "))
                y = int(input("Masukkan bilangan kedua: "))
            except ValueError:
                print("Input tidak valid, silakan masukkan bilangan bulat.")
                continue
            fpb = hitung_fpb(x, y)
            print("FPB dari", x, "dan", y, "adalah", fpb)

        elif pilihan == 2:
            try:
                x = int(input("Masukkan bilangan pertama: "))
                y = int(input("Masukkan bilangan kedua: "))
            except ValueError:
                print("Input tidak valid, silakan masukkan bilangan bulat.")
                continue
            kpk = hitung_kpk(x, y)
            print("KPK dari", x, "dan", y, "adalah", kpk)

        elif pilihan == 3:
            break

        else: 
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == '__main__':
    main()


# In[ ]:




