from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")  # wczytywanie obrazu

# print(type(inicjaly.mode))

def rysuj_ramke_w_obrazie(obraz,grub):
    if inicjaly.mode != "1":
       print("Obraz nie jest w trybie 1")
       return obraz
    else:
        tab_obraz = np.asarray(obraz).astype(np.uint8)
        h, w = tab_obraz.shape
        for i in range(h):
            for j in range(grub):
                tab_obraz[i][j] = 0
            for j in range(w - grub, w):
                tab_obraz[i][j] = 0
        for j in range(w):
            for i in range(grub):
                tab_obraz[i][j] = 0
            for i in range(h - grub, h):
                tab_obraz[i][j] = 0
        tab = tab_obraz.astype(bool)
        return Image.fromarray(tab)

def rysuj_ramki(w,h,grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i0 = k * grub + g
            j0 = i0
            for i in range(i0,h-i0):
                for j in range(j0,grub+j0):
                    tab[i][j] = k % 2
                for j in range(w - grub-j0, w-j0):
                    tab[i][j] = k % 2
            for j in range(j0,w-j0):
                for i in range(i0,grub+i0):
                    tab[i][j] = k % 2
                for i in range(h - grub-i0, h-i0):
                    tab[i][j] = k % 2
    return Image.fromarray(tab)




rysuj_ramki(100,180,20).show()
