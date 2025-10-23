import numpy as np
from PIL import Image


###############################ZAD5#############################
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
# r = rysuj_pasy_pionowe_szare(300, 200, 10, 0)
# g = rysuj_pasy_pionowe_szare(300, 200, 18, 50)
# b = rysuj_pasy_pionowe_szare(300, 200, 26, 100)
#
# r_tab = np.asarray(r)
# g_tab = np.asarray(g)
# b_tab = np.asarray(b)
#
# rgb = np.dstack((r_tab, g_tab, b_tab))
# obraz = Image.fromarray(rgb, mode='RGB')
# obraz.save("obraz6.png")
# obraz.show()


#############################ZAD6###############################
def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)


def rysuj_po_skosie_szare(w, h, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a * i + b * j) % 256
    return Image.fromarray(tab)


im_skos = rysuj_po_skosie_szare(100, 100, -20, 20)
im_skos.show()


r = rysuj_pasy_pionowe_szare(300, 200, 10, 0)
g = rysuj_pasy_pionowe_szare(300, 200, 18, 50)
b = rysuj_pasy_pionowe_szare(300, 200, 26, 100)

r_tab = np.asarray(r)
g_tab = np.asarray(g)
b_tab = np.asarray(b)
rgb = np.dstack((r_tab, g_tab, b_tab))


alpha = np.asarray(rysuj_po_skosie_szare(300, 200, 4, 11))

rgba = np.dstack((rgb, alpha))
obraz = Image.fromarray(rgba, mode='RGBA')

obraz.save("obraz7.png")
obraz.show()


##########################ZAD7####################
# masz już obraz RGB z pkt.5 w zmiennej `obraz`
cmyk = obraz.convert("CMYK")      # konwersja w Pillow
cmyk.save("obraz8.tiff")          # zapis w CMYK (TIFF)


obraz = obraz.convert("RGB")
r, g, b = obraz.split()
c, m, y, k = cmyk.split()

r.save("r.png")
c.save("c.png")
# Porównując r i c roznica jest taka że c jest odwrotnoscia r (bialy, czarny)
#b) aby zaproponaowac formalny sprawdzenie tego, można zrobic analizę pikselową