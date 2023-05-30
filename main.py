__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *

# functions

def search(term):
    term_lower = term.lower()
    query = Product.select().where(Product.name.contains(term_lower) | Product.description.contains(term_lower))
    for product in query: 
        print("Product: " + str.title(product.name) + ", Quantity: " + str(product.quantity) + ", Price: " + str(product.price) + ", Description: " + str(product.description))


def list_user_products(user_id):
    query = Product.select().join(User).where(User.id == user_id)
    for product in query: 
        print("Product: " + str.title(product.name) + ", Quantity: " + str(product.quantity) + ", Price: " + str(product.price) + ", Description: " + str(product.description))


def list_products_per_tag(tag_id):
    query = Product.select().join(ProductTag).join(Tag).where(Tag.id == tag_id)
    for product in query: 
        print("Product: " + str.title(product.name) + ", Quantity: " + str(product.quantity) + ", Price: " + str(product.price) + ", Description: " + str(product.description))


def add_product_to_catalog(user_id, product):
    Product.create(
        name = product["name"],
        description = product["description"],
        price = product["price"],
        quantity = product["quantity"],
        owner = user_id
    )


def update_stock(product_id, new_quantity):
    Product.update(quantity = new_quantity).where(Product.id == product_id).execute()


def purchase_product(product_id, buyer_id, quantity):
    TransactionLink.create(
        buyer = buyer_id,
        seller = User.select().join(Product).where(Product.id == product_id),
        product = product_id,
        quantity = quantity
    )
    old_quantity = Product.get(Product.id == product_id).quantity
    if old_quantity <= quantity:
        Product.delete().where(Product.id == product_id).execute()
    else:
        new_quantity = old_quantity - quantity
        Product.update(quantity = new_quantity).where(Product.id == product_id).execute()


def remove_product(product_id):
    Product.delete().where(Product.id == product_id).execute()


# execute
# here you can uncomment functions to execute the function

product = {
    "name": "elephant family of 3 watercolour art print",
    "description": "Paper: Epson Heavy Weight High Quality Paper - Made in Japan",
    "price": 12.30,
    "quantity": 43,
}

# search("beautiful")
# list_user_products(1)
# list_products_per_tag(1)
# add_product_to_catalog(5,product)
# update_stock(2,3)
# purchase_product(2,4,1)
# remove_product(3)