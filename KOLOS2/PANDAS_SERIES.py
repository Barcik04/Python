# Tworzenie Series z listy
s1 = pd.Series([1, 2, 3, 4, 5])

# Tworzenie Series z tablicy NumPy
s2 = pd.Series(np.array([10, 20, 30, 40, 50]))

# Tworzenie Series ze słownika
s3 = pd.Series({'a': 100, 'b': 200, 'c': 300})

series1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
series2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])


        # Wyświetlanie wartości Series
        print(s1.values)
        
        # Wyświetlanie indeksu Series
        print(s1.index)
        
        # Dostęp do wartości przez indeks
        print(s1[0])    # Pierwsza wartość
        print(s3['a'])  # Wartość o etykiecie 'a'
        
        # Zmiana wartości przez indeks
        s1[0] = 10
        print(s1)
        
        # Filtrowanie wartości
        print(s1[s1 > 2])
        print(s3[s3 > 150])



        # Dodawanie, odejmowanie, mnożenie, dzielenie
        print(s1 + 5)
        print(s1 - 5)
        print(s1 * 2)
        print(s1 / 2)
        
        # Operacje między dwoma Series
        print(s1 + s2)
        print(s1 - s2)
        print(s1 * s2)
        print(s1 / s2)


        # Sumowanie, średnia, mediana, odchylenie standardowe
        print(s1.sum())
        print(s1.mean())
        print(s1.median())
        print(s1.std())
        
        # Min, max, idxmin, idxmax
        print(s1.min())
        print(s1.max())
        print(s1.idxmin())
        print(s1.idxmax())
        
        # Cumulative sum, cumulative product
        print(s1.cumsum())
        print(s1.cumprod())

        # Przekonwertowanie Series do listy
        print(s1.tolist())
        
        # Przekonwertowanie Series do słownika
        print(s3.to_dict())
        
        # Sortowanie wartości
        print(s1.sort_values())
        
        # Sortowanie indeksu
        print(s3.sort_index())
        
        # Unikalne wartości
        print(s1.unique())
        
        # Wartości powtarzające się
        print(s1.duplicated())
        print(s1.drop_duplicates())
        
        # Wartości zliczanie
        print(s1.value_counts())


# Zmiana indeksu
s4 = s1.copy()
s4.index = ['a', 'b', 'c', 'd', 'e']
print(s4)

# Resetowanie indeksu
print(s4.reset_index(drop=True))

# Ustawienie indeksu
s5 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(s5)

# Tworzenie Series z brakującymi wartościami
s6 = pd.Series([1, 2, np.nan, 4, 5])

# Sprawdzanie brakujących wartości
print(s6.isna())
print(s6.notna())

# Usuwanie brakujących wartości
print(s6.dropna())

# Wypełnianie brakujących wartości
print(s6.fillna(0))
print(s6.fillna(method='ffill'))  # Forward fill
print(s6.fillna(method='bfill'))  # Backward fill


# Tworzenie Series z danymi tekstowymi
s7 = pd.Series(['apple', 'banana', 'cherry', np.nan, 'date'])

# Sprawdzanie długości ciągów
print(s7.str.len())

# Konwersja na wielkie/małe litery
print(s7.str.upper())
print(s7.str.lower())

# Sprawdzanie zawartości
print(s7.str.contains('a'))

# Zastępowanie ciągów
print(s7.str.replace('a', 'A'))

# Usuwanie białych znaków
print(s7.str.strip())

# Podział ciągów
print(s7.str.split('a'))


data2 = data.stack() tworzy serie z pliku csv
