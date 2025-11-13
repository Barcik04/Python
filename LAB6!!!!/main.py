import plt
from PIL import Image, ImageChops
import numpy as np


###################################ZAD6########################################
# def ocen_czy_identyczne(obraz1, obraz2):
#
#     if obraz1.mode != obraz2.mode:
#         return f"obrazy nie są identyczne mają różne tryby: {obraz1.mode} - {obraz2.mode}"
#
#     if obraz1.size != obraz2.size:
#         return f"obrazy nie są identyczne mają różne rozmiary: {obraz1.size} - {obraz2.size}"
#
#     diff = ImageChops.difference(obraz1, obraz2)
#     if not diff.getbbox():
#         return "obrazy identyczne"
#
#     return "obrazy nie są identyczne, bo piksele różnią się"
#
#
# im1 = Image.open("beksinski.png")
# im2 = Image.open("beksinski1.png")
# im3 = Image.open("beksinski2.png")
# im4 = Image.open("beksinski3.png")
#
#
# print(ocen_czy_identyczne(im1, im2))
# print(ocen_czy_identyczne(im1, im3))
# print(ocen_czy_identyczne(im1, im4))


###############################################ZAD7###################################################
#beksinski.png to jest moj "im"
#
# def pokaz_roznice(obraz):
#     width, height = obraz.size
#     wynik = Image.new(obraz.mode, (width, height))
#
#     extrema = obraz.getextrema()
#
#
#
#
#     (min_r, max_r), (min_g, max_g), (min_b, max_b) = extrema
#
#     max_r = max_r or 1
#     max_g = max_g or 1
#     max_b = max_b or 1
#
#     for x in range(width):
#         for y in range(height):
#             r, g, b = obraz.getpixel((x, y))
#
#             new_r = int((r / max_r) * 255)
#             new_g = int((g / max_g) * 255)
#             new_b = int((b / max_b) * 255)
#
#             wynik.putpixel((x, y), (new_r, new_g, new_b))
#
#     return wynik
#
#
#
# ###b
#
# im = Image.open("im.jpg")
# im_jpg3 = Image.open("im_jpg3.jpg")
#
# diff = ImageChops.difference(im, im_jpg3)
#
# # diff.show()
# # diff.save("diff.png")
#
# ###c
#
# obraz_po_funkcji = pokaz_roznice(diff)
# # obraz_po_funkcji.show()
#
# plt.figure(figsize=(10, 8))
#
# plt.subplot(2, 2, 1)
# plt.title("im")
# plt.imshow(im)
# plt.axis("off")
#
# plt.subplot(2, 2, 2)
# plt.title("im_jpg3")
# plt.imshow(im_jpg3)
# plt.axis("off")
#
# plt.subplot(2, 2, 3)
# plt.title("diff")
# plt.imshow(diff)
# plt.axis("off")
#
# plt.subplot(2, 2, 4)
# plt.title("obraz_po_funkcji")
# plt.imshow(obraz_po_funkcji)
# plt.axis("off")
#
# plt.tight_layout()
# plt.savefig("fig2.png")
# plt.show()

#################################################ZAD8################################################


# def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
#     wynik = obraz_bazowy.copy()
#
#     w_b, h_b = wynik.size
#     w_i, h_i = obraz_wstawiany.size
#
#     for x in range(w_i):
#         for y in range(h_i):
#             bx = m + x
#             by = n + y
#
#             if 0 <= bx < w_b and 0 <= by < h_b:
#
#                 if obraz_wstawiany.getpixel((x, y)) == 0:
#                     wynik.putpixel((bx, by), kolor)
#
#     return wynik
#
#
#
# inicjaly = Image.open("inicjaly.bmp")
# im = Image.open("im.jpg")
#
# w_b, h_b = im.size
# w_i, h_i = inicjaly.size
#
# obraz = wstaw_inicjaly(im, inicjaly, w_b - w_i, 0, (0, 255, 0))
#
# obraz = wstaw_inicjaly(obraz, inicjaly, 0, h_b - h_i, (255, 0, 0))
#
# obraz = wstaw_inicjaly(obraz, inicjaly, w_b - w_i // 2, h_b // 2 - h_i // 2, (0, 0, 255))
#
# obraz.save("obraz_inicjaly.png")

#########################################ZAD9#################################################
def odkoduj(obraz1, obraz2):
    t1 = np.asarray(obraz1)
    t2 = np.asarray(obraz2)

    h, w, d = t1.shape

    t_wynik = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            if not np.array_equal(t1[i, j], t2[i, j]):
                t_wynik[i, j] = 255
            else:
                t_wynik[i, j] = 0

    return Image.fromarray(t_wynik, mode="L")

jesien = Image.open("jesien.jpg")
zakodowany1 = Image.open("zakodowany1.bmp")

kod2 = odkoduj(jesien, zakodowany1)
kod2.save("kod2.bmp")
