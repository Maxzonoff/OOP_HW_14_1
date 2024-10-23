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
