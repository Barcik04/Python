from PIL import Image
import numpy as np


####################################ZAD1#########################################
# def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
#     t = (h, w)
#     tab = np.ones(t, dtype=np.uint8)
#     ile = int(w / grub)
#     for k in range(ile):
#         for g in range(grub):
#             j = k * grub + g
#             for i in range(h):
#                 tab[i, j] = (k + zmiana_koloru) % 256
#     return Image.fromarray(tab)
#
#
# im_paski = rysuj_pasy_pionowe_szare(100, 246, 1, 5)
# im_paski.show()


# def rysuj_ramke_szare(w, h, grub, kolor_ramki, kolor): #kolor od 0 do 255
#     t = (h, w)
#     tab = np.ones(t, dtype=np.uint8)
#     tab[:] = kolor_ramki  # wypełnienie tablicy szarym kolorem o wartości kolor_ramki
#     tab[grub:h-grub, grub:w-grub] = kolor  # wypełnienie podtablicy kolorem o wartości kolor
#     return Image.fromarray(tab)
#
#
# im_ramka = rysuj_ramke_szare(120, 60, 8, 100, 200)
# im_ramka.show()


#####################################ZAD2###########################################
# def negatyw(obraz):
#     if obraz.mode == '1':
#         tab = np.asarray(obraz)
#         h, w = tab.shape
#         tab_neg = tab.copy()
#         for i in range(h):
#             for j in range(w):
#                 if tab_neg[i, j]:
#                     tab_neg[i, j] = False
#                 else:
#                     tab_neg[i, j] = True
#     elif obraz.mode == 'L':
#         tab = np.asarray(obraz)
#         h, w = tab.shape
#         tab_neg = tab.copy()
#         for i in range(h):
#             for j in range(w):
#                 tab_neg[i, j] = 255 - tab[i, j]
#     else:
#         tab = np.asarray(obraz)
#         h, w, rgb = tab.shape
#         tab_neg = tab.copy()
#         for i in range(h):
#             for j in range(w):
#                 for k in range(rgb):
#                     tab_neg[i,j,k] = 255 - tab[i,j,k]
#
#     return Image.fromarray(tab_neg)
#
# img = Image.open("gwiazdka.bmp")
# img.show()
# img_neg = negatyw(img)
# img_neg.show()


#
# def rysuj_ramki_kolorowe(w, kolor, a, b, c):
#     t = (w, w, 3)
#     tab = np.zeros(t, dtype=np.uint8)
#     kolor_r = kolor[0]
#     kolor_g = kolor[1]
#     kolor_b = kolor[2]
#     z = w
#     for k in range(int(w / 2)):
#         for i in range(k, z - k):
#             for j in range(k, z - k):
#                 tab[i, j] = [kolor_r, kolor_g, kolor_b]
#         kolor_r = (kolor_r - a) % 256
#         kolor_g = (kolor_g - b) % 256
#         kolor_b = (kolor_b - c) % 256
#     return Image.fromarray(tab)
#
#
#
# ramki = rysuj_ramki_kolorowe(200, [20,120,220],4,11,-4)
# ramki.show()
# negatyw(ramki).show()


#
# def rysuj_po_skosie_szare(h,w, a, b):
#     t = (h, w)
#     tab = np.zeros(t, dtype=np.uint8)
#     for i in range(h):
#         for j in range(w):
#             tab[i, j] = (a*i + b*j) % 256
#     return Image.fromarray(tab)
#
#
# im_skos = rysuj_po_skosie_szare(100, 300, 4, 11)
# im_skos.show()
# negatyw(im_skos).show()




###################################ZAD3################################
def koloruj_w_paski(obraz, grub):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)

    for i in range(h):
        #kolor paskow przechodzi po rgb. Na podstawie wyniku i//grub % 3 wybierany jest kolor
        color = [0, 0, 0]
        color[(i // grub) % 3] = 255
        for j in range(w):
            if not t_obraz[i, j]:
                tab[i, j] = color
            else:
                tab[i, j] = [255, 255, 255]
    return Image.fromarray(tab)

gwiazdka = Image.open("gwiazdka.bmp")
obraz3 = koloruj_w_paski(gwiazdka, 3)
obraz3.show()

obraz3.save("gwiazdka_kolor.png")
obraz3.save("gwiazdka_kolor.jpg")
#PNG to format bezstratny — zapisuje dokładnie te same wartości pikseli (kolory, jasność itd.).
#JPG (JPEG) to format stratny — podczas kompresji usuwa część informacji o kolorach, żeby plik był mniejszy.


######################ZAD4################################
###RGB ma zakres do 255 wiec w przypadku 324 wartosc jest zawijana (324%256) = 72
### tak samo dla -24 (-24 % 256) = 232