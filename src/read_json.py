import json


class Product:
    """Класс для товара"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для категории"""

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = []
        for product in products:
            self.products.append(Product(**product))


def read_json(path):
    """Функция для чтения JSON файла и создания объектов классов"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for category_data in data:
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=category_data["products"],
        )
        categories.append(category)

    return categories


categories = read_json("../data/products.json")

for category in categories:
    print(f"Категория: {category.name}, Описание: {category.description}")
    for product in category.products:
        print(
            f" Товар: {product.name},"
            f" Описание: {product.description},"
            f" Цена: {product.price}, "
            f" Количество: {product.quantity}"
        )
