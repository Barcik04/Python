
from PIL import Image, ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
import numpy as np



im = Image.open('beksinski.png')

######################ZAD1a####################################
# def statystyki(obraz):
#     s = stat.Stat(obraz)
#     print("extrema ", s.extrema)   # minimalna i maksymalna wartość piksela w każdym kanale (R, G, B)
#     print("count ", s.count)       # liczba pikseli w każdym kanale (powinna być taka sama)
#     print("mean ", s.mean)         # średnia jasność pikseli w kanałach – pokazuje ogólne zabarwienie obrazu
#     print("rms ", s.rms)           # średnia kwadratowa – podobna do mean, ale mocniej reaguje na skrajne wartości
#     print("median ", s.median)     # mediana – połowa pikseli ma wartość mniejszą lub równą tej liczbie
#     print("stddev ", s.stddev)     # odchylenie standardowe – jak bardzo jasność pikseli jest zróżnicowana (kontrast)
#


# statystyki(im)


# def rysuj_histogram_RGB(obraz):
#     hist = obraz.histogram()
#     plt.title("histogram  ")
#     plt.bar(range(256), hist[:256], color='r', alpha=0.5)
#     plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
#     plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
#     plt.show()
# rysuj_histogram_RGB(im)




###########################1b#######################

# hist = im.histogram()
# print("Kanał R, piksele =155:", hist[155])
# print("Kanał G, piksele =155:", hist[155 + 256])
# print("Kanał B, piksele =155:", hist[155 + 2*256])



#############################1c################################
# def zlicz_piksele(obraz, kolor):
#     arr = np.array(obraz)
#     return np.sum(np.all(arr == kolor, axis=2))
#
# wynik = zlicz_piksele(im, [155, 155, 155])
# print("Liczba pikseli o kolorze [155,155,155]:", wynik)




##############################ZAD2a#############################
#
# im.save('beksinski.jpg', 'JPEG')
# im_jpg = Image.open('beksinski.jpg')
#
#
# statystyki(im)
# print("\n\n\n")
# statystyki(im_jpg)
# ###Format PNG zapisuje obraz bezstratnie, każdy piksel jest zachowany dokładnie.
# ###Format JPG używa kompresji stratnej, oznacza to, że:
#         # część informacji o kolorach jest celowo usuwana (dla zmniejszenia rozmiaru pliku),
#         # pojawiają się delikatne różnice w wartościach pikseli,
#         # pojawia się szum i artefakty, szczególnie w jednolitych obszarach i na krawędziach.



##################################ZAD2b###################################
# im.save('beksinski.jpg', 'JPEG')
# im_jpg = Image.open('beksinski.jpg')
#
# diff = ImageChops.difference(im_jpg,im)
# statystyki(diff)
#
# # extrema  [(0, 87), (0, 48), (0, 91)]
# # count  [156816, 156816, 156816]
# # mean  [6.482214825017856, 4.696612590551984, 5.909881644730129]
# # rms  [9.189732576526847, 6.42443896211657, 8.219244273713759]
# # median  [5, 3, 4]
# # stddev  [6.5139907729745445, 4.383519835957174, 5.712204073407946]
# # Statystyki pokazują, że po zapisaniu obrazu w formacie JPG pojawiły się niewielkie różnice w pikselach w porównaniu do oryginału (PNG).
# # Średnie wartości różnicy (mean: 4–6) oraz mediany (3–5) są niskie, co oznacza, że większość zmian jest bardzo mała i praktycznie niewidoczna gołym okiem.
# # Jednak wartości extrema (np. do 87 w kanale R) pokazują, że lokalnie mogą występować większe różnice — typowe dla kompresji JPEG w miejscach z ostrymi krawędziami lub detalami.

#######################################ZAD2c##################################
# im.save('beksinski1.jpg', 'JPEG')
# im1 = Image.open('beksinski1.jpg')
# print("\n\n\n PO zapisie 1: \n\n")
# statystyki(im1)
#
# im1.save('beksinski2.jpg', 'JPEG')
# im2 = Image.open('beksinski2.jpg')
# print(" \n\n\n Po zapisie 2: \n\n ")
# statystyki(im2)
#
#
# im2.save('beksinski3.jpg', 'JPEG')
# im3 = Image.open('beksinski3.jpg')
# print("\n\n\n Po zapisie 3: \n\n ")
# statystyki(im3)

# PO zapisie 1:
#
# extrema[(0, 255), (0, 255), (0, 255)]
# count[156816, 156816, 156816]
# mean[92.21274614835221, 71.49184394449546, 51.752875982042646]
# rms[110.31828968154556, 86.28685689334972, 65.31080495213301]
# median[94, 67, 47]
# stddev[60.55521848726959, 48.314986515048545, 39.83893913099187]
#
# Po zapisie 2:
#
# extrema[(0, 255), (0, 255), (0, 255)]
# count[156816, 156816, 156816]
# mean[92.2355626976839, 71.50015304560759, 51.78574890317314]
# rms[110.29189226705178, 86.29037104384356, 65.33557119659511]
# median[94, 67, 47]
# stddev[60.47232816494313, 48.308966552172144, 39.83683062346765]
#
# Po zapisie 3:
#
# extrema[(0, 255), (0, 255), (0, 255)]
# count[156816, 156816, 156816]
# mean[92.25099479644935, 71.50290786654423, 51.812289562289564]
# rms[110.2870062730796, 86.29006915983213, 65.35281826765352]
# median[94, 67, 47]
# stddev[60.4398685616024, 48.304349723778486, 39.8306101615128]
#


# Średnia (mean) delikatnie rośnie oznacza to, że wartości pikseli minimalnie się zmieniają po każdej kompresji.
# RMS i stddev lekko maleją obraz traci szczegóły i staje się delikatnie bardziej “wygładzony” przez kompresję JPG.
# Mediana i count pozostają takie same ogólny rozkład jasności i liczba pikseli się nie zmienia.
# Extrema (0–255) również bez zmian nadal występują czyste czernie i biele, ale wartości pośrednie się zmieniają.



#################################ZAD3a#####################################
# r, g, b = im.split()
#
# print("tryb kanału r: ", r.mode)
# print("tryb kanału g: ", g.mode)
# print("tryb kanału b: ", b.mode)
#
# r.save("im_r.jpg")
# g.save("im_g.jpg")
# b.save("im_b.jpg")
#
# print("Zapisano obrazy: im_r.jpg, im_g.jpg, im_b.jpg")
#
#


##################################ZAD3b#####################################
# im_r = Image.open('im_r.jpg')
# im_g = Image.open('im_g.jpg')
# im_b = Image.open('im_b.jpg')
#
# im1 = Image.merge('RGB', (im_r, im_g, im_b))
#
# diff1 = ImageChops.difference(im, im1)
# diff1.show()
#
#
# plt.figure(figsize=(16, 8))
#
# plt.subplot(1, 3, 1)
# plt.imshow(im)
# plt.title("Oryginalny obraz (im)")
# plt.axis('off')
#
# plt.subplot(1, 3, 2)
# plt.imshow(im1)
# plt.title("Scalony obraz (im1)")
# plt.axis('off')
#
# plt.subplot(1, 3, 3)
# plt.imshow(np.array(diff1), cmap='gray')
# plt.title("Różnica (diff1)")
# plt.axis('off')
#
# plt.tight_layout()
# plt.savefig("fig1.png")
# # Jeśli cały proces przebiegł poprawnie (czyli kanały zostały dobrze rozdzielone i scalone z powrotem),
# #  obraz diff1 będzie czarny – to znaczy, że nie ma żadnych różnic.


###########################################ZAD4a######################################################
# from PIL import Image, ImageOps
# import random
#
# def mieszaj_kanaly(obraz: Image.Image):
#     r, g, b = obraz.split()
#
#
#     nr = ImageOps.invert(r)
#     ng = ImageOps.invert(g)
#     nb = ImageOps.invert(b)
#
#     pool = [("r", r), ("g", g), ("b", b), ("nr", nr), ("ng", ng), ("nb", nb)]
#     chosen = [random.choice(pool) for _ in range(3)]
#
#     labels = [x[0] for x in chosen]
#     ch_R, ch_G, ch_B = (x[1] for x in chosen)
#
#
#     im_mix = Image.merge("RGB", (ch_R, ch_G, ch_B))
#     return im_mix, labels
#
# im = Image.open("beksinski.jpg")
# mix, picked = mieszaj_kanaly(im)
# print("Wylosowane kanały (R,G,B):", picked)
# mix.save("mix.png")


###########################4b###########################
# def rozpoznaj_mix(obraz, mix):
#     if obraz.mode != "RGB" or mix.mode != "RGB":
#         raise ValueError("Oba obrazy muszą być w trybie RGB")
#
#     r, g, b = obraz.split()
#     kanal = {'R': r, 'G': g, 'B': b}
#
#     kombinacje = [
#         ('R','G','B'),
#         ('R','B','G'),
#         ('G','R','B'),
#         ('G','B','R'),
#         ('B','R','G'),
#         ('B','G','R')
#     ]
#
#     for kombinacja in kombinacje:
#         test = Image.merge('RGB', (kanal[kombinacja[0]], kanal[kombinacja[1]], kanal[kombinacja[2]]))
#
#         if not ImageChops.difference(test, mix).getbbox():
#             return f"mix powstał przez zmianę kanałów na kolejność: {kombinacja}"
#
#     return "Nie pasuje do żadnej prostej zamiany kanałów RGB."
#
#
# im_4 = Image.open("beksinski.jpg")
# mix = Image.open("mix.png")
#
# wynik = rozpoznaj_mix(im_4, mix)
# print(wynik)



###############################ZAD5##############################
# bo beksinski1.png nie jest w trybie RGB.