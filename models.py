from peewee import *

db = SqliteDatabase("betsy_webshop.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField(min_length=6)
    email_address = CharField(unique=True)
    first_name = CharField()
    last_name = CharField()
    street_address = CharField()
    postal_code = CharField()
    city = CharField()
    country = CharField()

class PaymentOption(BaseModel):
    type = CharField()
    card = CharField()
    user = ForeignKeyField(User, backref="payment_options")

class Product(BaseModel):
    name = CharField()
    description = TextField()
    price = DecimalField(decimal_places=2, auto_round=True)
    quantity = IntegerField()
    owner = ForeignKeyField(User, backref="products")

class Tag(BaseModel):
    name = CharField(unique=True, max_length=20)

class ProductTag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)

class TransactionLink(BaseModel):
    buyer = ForeignKeyField(User, backref="purchases")
    seller = ForeignKeyField(User, backref="sales")
    product = ForeignKeyField(Product, backref="transactions")
    quantity = IntegerField()