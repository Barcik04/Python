# Tworzenie Series z listy
s1 = pd.Series([1, 2, 3, 4, 5])

# Tworzenie Series z tablicy NumPy
s2 = pd.Series(np.array([10, 20, 30, 40, 50]))

# Tworzenie Series ze słownika
s3 = pd.Series({'a': 100, 'b': 200, 'c': 300})

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
