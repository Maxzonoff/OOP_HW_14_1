import pytest

from src.products import Category, Product


@pytest.fixture
def product():
    return Product("name", "description", 20.0, 1)


@pytest.fixture
def products(product):
    return [product, product, product]


@pytest.fixture
def category(products):
    return Category("name", "description", products)


def test_product_init(product):
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 20.0
    assert product.quantity == 1


def test_category_init(category, products):
    assert category.name == "name"
    assert category.description == "description"
    assert category.products == products


def test_category_count_inc(products):
    Category.category_count = 10
    Category("name", "description", products)
    assert Category.category_count == 11
    Category("name", "description", products)
    assert Category.category_count == 12


def test_product_count_inc(products):
    Category.product_count = 10
    Category("name", "description", products)
    assert Category.product_count == 13
    Category("name", "description", products[:2])
    assert Category.product_count == 15


def test_product_initialization():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_category_initialization():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category.products) == 3


def test_category_count():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    assert Category.category_count == 1


def test_product_count():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    assert Category.product_count == 3


def test_multiple_categories():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    assert Category.category_count == 2
    assert Category.product_count == 4


def test_product_invalid_initialization():
    with pytest.raises(TypeError):
        Product("iPhone", "Latest model")  # Пропущены price и quantity


# Тест для проверки работы с пустыми данными
def test_empty_category():
    category = Category("Empty Category", "No products here", [])
    assert category.name == "Empty Category"
    assert category.description == "No products here"
    assert len(category.products) == 0