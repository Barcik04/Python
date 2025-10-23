from PIL import Image
import numpy as np

def rgb_to_cmyk(rgb_array):
    # Przekształć wartości RGB na zakres [0, 1]
    rgb = rgb_array.astype(float) / 255
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]

    # Oblicz kanał Kk (black)
    k = 1 - np.max(rgb, axis=2)

    # Uniknij dzielenia przez zero
    c = (1 - r - k) / (1 - k + 1e-8)
    m = (1 - g - k) / (1 - k + 1e-8)
    y = (1 - b - k) / (1 - k + 1e-8)

    # Zastąp NaN (dla czystej czerni) zerami
    c[np.isnan(c)] = 0
    m[np.isnan(m)] = 0
    y[np.isnan(y)] = 0

    # Przekształć na zakres [0, 255]
    cmyk = np.stack((c, m, y, k), axis=2) * 255
    return cmyk.astype(np.uint8)



