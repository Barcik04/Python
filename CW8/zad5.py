import numpy as np

# Data from the image
students = np.arange(1, 41)
heights = np.array([153, 154, 154, 155, 158, 159, 160, 161, 163, 164, 165, 165, 165, 166, 167, 167, 167, 170, 170, 170,
                    170, 171, 173, 174, 174, 174, 175, 175, 176, 177, 178, 178, 178, 179, 179, 179, 179, 180, 183, 185])
shoe_sizes = np.array([5, 6, 6, 6, 5, 7, 6, 5, 8, 7, 7, 7, 6, 9.5, 9, 10, 13, 10.5, 9.5, 9.5, 8.5, 9, 10, 8, 10, 9, 12, 11, 9, 10, 11, 11, 12, 10.5, 11.5, 11, 11, 10, 10.5, 13])

srednia_sizes = np.mean(shoe_sizes)
print(srednia_sizes)
print("\n")

max_rozmiar_buta_jaki = np.max(shoe_sizes) #13
max_rozmiar_buta_id = np.where(shoe_sizes == max_rozmiar_buta_jaki)[0] #[16,39]
max_rozmiar_buta_values = heights[max_rozmiar_buta_id] #[167, 185]
print(max_rozmiar_buta_values)
print("\n")
avg_height_max_shoe_size = np.mean(max_rozmiar_buta_values) #176
print(avg_height_max_shoe_size)
print("\n")
min_height_of_max_shoe_size = np.min(max_rozmiar_buta_values) #167
print(min_height_of_max_shoe_size)
print("\n")

unique_shoe_sizes = np.unique(shoe_sizes) #[ 5.   6.   7.   8.   8.5  9.   9.5 10.  10.5 11.  11.5 12.  13. ]
for i in unique_shoe_sizes:
    indices = np.argwhere(shoe_sizes == i).flatten()
    avarage_height = np.mean(heights[indices])
    print(avarage_height)
print("\n")

arg_on_shoe_size_10 = np.argwhere(shoe_sizes == 10).flatten() #[15 22 24 29 37]
heights_shoe_size_10 = heights[arg_on_shoe_size_10] #[167 173 174 177 180]
max_height_shoe_size_10 = np.max(heights_shoe_size_10)
min_height_shoe_size_10 = np.min(heights_shoe_size_10)
print(max_height_shoe_size_10, min_height_shoe_size_10)
print("\n")
