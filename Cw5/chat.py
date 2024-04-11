# class Movie:
#     def __init__(self, title, director, year):
#         self.title = title
#         self.director = director
#         self.year = year
#
#     def __str__(self):
#         return f'title: {self.title},  director: {self.director},   year: {self.year}'
#
# class Catalog:
#     def __init__(self):
#         self.movies = []
#
#     def add_movies(self, movie):
#         self.movies.append(movie)
#
#     def show_movies(self):
#         for movie in self.movies:
#             print(movie)
#
#     def find_movie_by_year(self, year):
#         found_movies = [movie for movie in self.movies if movie.year == year]
#         for movie in found_movies:
#             print(movie)
#
# catalog = Catalog()
#
#
# catalog.add_movies(Movie("Inception", "Christopher Nolan", 2010))
# catalog.add_movies(Movie("The Matrix", "Lana and Lilly Wachowski", 1999))
# catalog.add_movies(Movie("Interstellar", "Christopher Nolan", 2014))
#
# print('\nmovies in catalog: ')
# catalog.show_movies()
#
#
# print('\nmovies from 2010: ')
# catalog.find_movie_by_year(2010)









# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.price = price
#         self.name = name
#
#     def __str__(self):
#         return f'product name: {self.name} with price: {self.price}\t'
#
# class Order:
#     def __init__(self, order_id, customer):
#         self.order_id = order_id
#         self.products = []
#         self.customer = customer
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def calculate_total(self):
#         return sum(product.price for product in self.products)
#
#     def __str__(self):
#         products_str = ', '.join(str(product) for product in self.products)
#         return f'order ID: {self.order_id}, customer name: {self.customer},  products: {products_str}, price sum: {self.calculate_total()}'
#
# class Shop:
#     def __init__(self):
#         self.orders = []
#
#     def add_order(self, order):
#         self.orders.append(order)
#
#     def show_orders(self):
#         for order in self.orders:
#             print(order)
#
#     def show_order(self, order_id):
#         order = next((order for order in self.orders if order_id == order.order_id), None)
#         if order:
#             print(order)
#         else:
#             print("Order Not Found")
#
#
# product1 = Product(1, "Laptop", 1200)
# product2 = Product(2, "Mouse", 35)
# product3 = Product(3, "Keyboard", 75)
#
#
# order1 = Order(101, "Alice")
# order1.add_product(product1)
# order1.add_product(product2)
# order2 = Order(102, "Bob")
# order2.add_product(product3)
#
#
# shop = Shop()
# shop.add_order(order1)
# shop.add_order(order2)
# shop.show_orders()
#
# shop.show_order(101)




# class Item:
#     def __init__(self, item_id, name, quantity):
#         self.item_id = item_id
#         self.name = name
#         self.quantity = quantity
#
#     def __str__(self):
#         return f'item ID: {self.item_id},  name: {self.name},  quantity: {self.quantity}\t'
#
# class Warehouse:
#     def __init__(self):
#         self.items = {}
#
#     def add_item(self, item):
#         if item in self.items:
#             self.items[item.item_id].quantity += item.quantity
#         else:
#             self.items[item.item_id] = item
#
#     def show_items(self):
#         for item in self.items.values():
#             print(item)
#
# item = Item(101, 'Screw', 10)
# warehouse = Warehouse()
# warehouse.add_item(item)
#
# warehouse.show_items()
