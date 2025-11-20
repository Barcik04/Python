from PIL import Image
import matplotlib.pyplot as plt
import numpy as np



##################################ZAD1############################
obraz = Image.open("obraz.png")
kopia = obraz.copy()

inicjaly = Image.open("inicjaly.bmp")


####################################ZAD2#################################
# def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
#     wynik = obraz.copy()
#
#     w_b, h_b = wynik.size
#     w_i, h_i = inicjaly.size
#
#     kolor_tla = inicjaly.getpixel((0, 0))
#
#     for x in range(w_i):
#         for y in range(h_i):
#             px = inicjaly.getpixel((x, y))
#
#             if px != kolor_tla:
#                 bx = m + x
#                 by = n + y
#
#                 if 0 <= bx < w_b and 0 <= by < h_b:
#                     wynik.putpixel((bx, by), kolor)
#
#     return wynik
#
#
#
# w_b, h_b = obraz.size
# w_i, h_i = inicjaly.size
#
# m = w_b - w_i
# n = h_b - h_i
#
# obraz1 = wstaw_inicjaly(obraz, inicjaly, m, n, (255, 0, 0))
# obraz1.save("obraz1.png")
#
# #########################################b#####################################
# def wstaw_inicjaly_maska(obraz, inicjaly, m, n):
#     wynik = obraz.copy()
#
#     w_b, h_b = wynik.size
#     w_i, h_i = inicjaly.size
#
#     for x in range(w_i):
#         for y in range(h_i):
#             bx = m + x
#             by = n + y
#
#             if bx < w_b and by < h_b:
#                 mask_pixel = inicjaly.getpixel((x, y))
#
#                 if mask_pixel == 0:
#                     r, g, b = wynik.getpixel((bx, by))
#                     wynik.putpixel((bx, by), (255 - r, 255 - g, 255 - b))
#
#     return wynik
#
#
# w_b, h_b = obraz.size
# w_i, h_i = inicjaly.size
#
# m = (w_b - w_i) // 2
# n = (h_b - h_i) // 2
#
# obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, m, n)
# obraz2.save("obraz2.png")
#

######################################ZAD3###################################
# def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
#     wynik = obraz.copy()
#
#     pix = wynik.load()
#     mask = inicjaly.load()
#
#     w_b, h_b = wynik.size
#     w_i, h_i = inicjaly.size
#
#     kolor_tla = mask[0, 0]
#
#     for x in range(w_i):
#         for y in range(h_i):
#             if mask[x, y] != kolor_tla:
#                 bx = m + x
#                 by = n + y
#
#                 if 0 <= bx < w_b and 0 <= by < h_b:
#                     pix[bx, by] = kolor
#
#     return wynik
#
#
# def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n):
#     wynik = obraz.copy()
#
#     pix = wynik.load()
#     mask = inicjaly.load()
#
#     w_b, h_b = wynik.size
#     w_i, h_i = inicjaly.size
#
#     for x in range(w_i):
#         for y in range(h_i):
#             bx = m + x
#             by = n + y
#
#             if 0 <= bx < w_b and 0 <= by < h_b:
#                 if mask[x, y] == 0:
#                     r, g, b = pix[bx, by]
#                     pix[bx, by] = (255 - r, 255 - g, 255 - b)
#
#     return wynik
#
#
# w_b, h_b = obraz.size
# w_i, h_i = inicjaly.size
#
# m1 = w_b - w_i
# n1 = h_b - h_i
# obraz3_1 = wstaw_inicjaly_load(obraz, inicjaly, m1, n1, (255, 0, 0))
#
# m2 = (w_b - w_i) // 2
# n2 = (h_b - h_i) // 2
# obraz3_2 = wstaw_inicjaly_maska_load(obraz, inicjaly, m2, n2)
#
#
# fig, axes = plt.subplots(1, 2, figsize=(10, 5))
#
# axes[0].imshow(obraz3_1)
# axes[0].set_title("zad 3a")
# axes[0].axis("off")
#
# axes[1].imshow(obraz3_2)
# axes[1].set_title("zad 3b")
# axes[1].axis("off")
#
# plt.tight_layout()
# plt.savefig("fig1.png")
#

###########################################ZAD4####################################
#
# def kontrast(obraz, wsp_kontrastu):
#
#     mn = ((255 + wsp_kontrastu) / 255) ** 2
#
#     return obraz.point(
#         lambda i: max(0, min(255, int(128 + (i - 128) * mn)))
#     )
#
#
# wsp_list = [0, 30, 60]
#
# img0 = obraz
# img1 = kontrast(obraz, wsp_list[0])
# img2 = kontrast(obraz, wsp_list[1])
# img3 = kontrast(obraz, wsp_list[2])
#
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
#
# axes[0, 0].imshow(img0)
# axes[0, 0].set_title("oryginał")
# axes[0, 0].axis("off")
#
# axes[0, 1].imshow(img1)
# axes[0, 1].set_title(f"wsp_kontrastu = {wsp_list[0]}")
# axes[0, 1].axis("off")
#
# axes[1, 0].imshow(img2)
# axes[1, 0].set_title(f"wsp_kontrastu = {wsp_list[1]}")
# axes[1, 0].axis("off")
#
# axes[1, 1].imshow(img3)
# axes[1, 1].set_title(f"wsp_kontrastu = {wsp_list[2]}")
# axes[1, 1].axis("off")
#
# plt.tight_layout()
# plt.savefig("fig2.png")


##################################b#####################################3
# def zakres(w, h):
#     for i in range(w):
#         for j in range(h):
#             yield i, j
#
# def transformacja_logarytmiczna(obraz):
#     return obraz.point(lambda i: int(255 * np.log(1 + i / 255)))
#
#
# def filtr_liniowy(image, a, b):
#     w, h = image.size
#     pixele = image.load()
#
#     for i, j in zakres(w, h):
#         r, g, b2 = pixele[i, j]
#
#         r = a * r + b
#         g = a * g + b
#         b2 = a * b2 + b
#
#         r = max(0, min(255, r))
#         g = max(0, min(255, g))
#         b2 = max(0, min(255, b2))
#
#         pixele[i, j] = (r, g, b2)
#
#     return image
#
#
# obraz = Image.open("obraz.png")
#
#
# img_orig = obraz.copy()
#
# img_log = transformacja_logarytmiczna(obraz.copy())
#
# img_lin = filtr_liniowy(obraz.copy(), a=2, b=100)
#
#
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
# axes[0].imshow(img_orig)
# axes[0].set_title("oryginał")
# axes[0].axis("off")
#
# axes[1].imshow(img_log)
# axes[1].set_title("transformacja logarytmiczna")
# axes[1].axis("off")
#
# axes[2].imshow(img_lin)
# axes[2].set_title("filtr liniowy (a=2, b=100)")
# axes[2].axis("off")
#
# plt.tight_layout()
# plt.savefig("fig3.png")



###############################################c##################################3
# def transformacja_gamma(obraz, gamma):
#     return obraz.point(
#         lambda i: int(((i / 255) ** (1 / gamma)) * 255)
#     )
#
# gamma_vals = [0.5, 1, 2.5]
#
# img_orig = obraz.copy()
# img_g1 = transformacja_gamma(obraz.copy(), gamma_vals[0])
# img_g2 = transformacja_gamma(obraz.copy(), gamma_vals[1])
# img_g3 = transformacja_gamma(obraz.copy(), gamma_vals[2])
#
# fig, axes = plt.subplots(1, 4, figsize=(20, 5))
#
# axes[0].imshow(img_orig)
# axes[0].set_title("oryginał")
# axes[0].axis("off")
#
# axes[1].imshow(img_g1)
# axes[1].set_title(f"gamma = {gamma_vals[0]}")
# axes[1].axis("off")
#
# axes[2].imshow(img_g2)
# axes[2].set_title(f"gamma = {gamma_vals[1]}")
# axes[2].axis("off")
#
# axes[3].imshow(img_g3)
# axes[3].set_title(f"gamma = {gamma_vals[2]}")
# axes[3].axis("off")
#
# plt.tight_layout()
# plt.savefig("fig4.png")

# Transformacja gamma zmienia jasność pikseli w sposób nieliniowy. W zależności od wartości gamma efekt jest inny:
#
# 1. Gamma < 1 (np. 0.5)
#
# Obraz robi się wyraźnie jaśniejszy.
# Ciemne miejsca zostają mocno rozjaśnione, przez co widać więcej szczegółów w cieniach.
#
# 2. Gamma = 1
#
# Brak zmian — obraz wygląda dokładnie tak samo jak oryginał.
#
# 3. Gamma > 1 (np. 2.5)
#
# Obraz staje się ciemniejszy.
# Cienie robią się jeszcze ciemniejsze, część detali znika, a jasne fragmenty zmieniają się niewiele.



################################################################ZAD5########################################
def transformacja_gamma(obraz, gamma):
    return obraz.point(
        lambda i: int(((i / 255) ** (1 / gamma)) * 255)
    )

def transformacja_gamma_lista(obraz, gamma):
    tabela = [
        int(((i / 255) ** (1 / gamma)) * 255)
        for i in range(256)
    ]

    if obraz.mode == "L":
        return obraz.point(tabela)

    if obraz.mode == "RGB":
        r, g, b = obraz.split()
        r = r.point(tabela)
        g = g.point(tabela)
        b = b.point(tabela)
        return Image.merge("RGB", (r, g, b))

    return transformacja_gamma(obraz, gamma)


gamma = 0.5

img_lambda = transformacja_gamma(obraz.copy(), gamma)
img_lista  = transformacja_gamma_lista(obraz.copy(), gamma)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(obraz)
axes[0].set_title("oryginalny")
axes[0].axis("off")

axes[1].imshow(img_lambda)
axes[1].set_title("gamma 0.5 – lambda (pkt 4c)")
axes[1].axis("off")

axes[2].imshow(img_lista)
axes[2].set_title("gamma 0.5 – lista (pkt 5)")
axes[2].axis("off")

plt.tight_layout()
plt.savefig("fig5.png")

# Obie funkcje (lambda i lista) dają praktycznie identyczny efekt wizualny, ponieważ korzystają z tego samego wzoru gamma.
# Różnica jest tylko w implementacji: wersja z listą korzysta z gotowej tablicy 256 wartości, więc działa szybciej, bo nie wywołuje lambdy dla każdego piksela osobno.
# Przy gamma = 0.5 oba obrazy są wyraźnie rozjaśnione i wyglądają prawie tak samo.



# 6A
# Obraz uzyskany za pomocą numpy różni się od wyniku point(lambda i: i + 100),
# ponieważ tablica uint8 w numpy powoduje overflow — wartości powyżej 255 „zawijają się” modulo 256 i
# zmieniają kolory w nieprzewidywalny sposób. Funkcja point() nie robi overflow,
# tylko przycina wartości do zakresu 0–255,
# więc obraz jest poprawnie rozjaśniony.


# 6B
# def dodaj_100_numpy(obraz):
#     T = np.array(obraz, dtype='int16')
#     T = np.clip(T + 100, 0, 255)
#     return Image.fromarray(T.astype('uint8'), "RGB")