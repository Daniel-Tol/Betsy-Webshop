from models import *

# test data

users = [{
    "username":"hwarn0",
    "password":"DZLpeJIRZx",
    "email_address":"hwarn0@shop-pro.jp",
    "first_name":"Harlen",
    "last_name":"Warn",
    "street_address":"7 Dottie Alley",
    "postal_code": "4356",
    "city":"Al Udayn",
    "country":"Yemen"
},
{
    "username":"brodear1",
    "password":"PgMh4Ck7k",
    "email_address":"brodear1@census.gov",
    "first_name":"Bogey",
    "last_name":"Rodear",
    "street_address":"9 Lien Drive",
    "postal_code":"2109",
    "city":"Morong",
    "country":"Philippines"
},
{
    "username":"vfreestone2",
    "password":"hpGDyDena",
    "email_address":"vfreestone2@ehow.com",
    "first_name":"Viviana",
    "last_name":"Freestone",
    "street_address":"2787 Division Circle",
    "postal_code":"582 83",
    "city":"Klášter",
    "country":"Czech Republic"
},
{
    "username":"wleefe3",
    "password":"8Q7FKqm4mN",
    "email_address":"wleefe3@sciencedaily.com",
    "first_name":"Walden",
    "last_name":"Leefe",
    "street_address":"01 Northwestern Way",
    "postal_code":"40212",
    "city":"Walakeri",
    "country":"Indonesia"
},
{
    "username":"gtassel4",
    "password":"EABvgbo0uImx",
    "email_address":"gtassel4@newyorker.com",
    "first_name":"Glori",
    "last_name":"Tassel",
    "street_address":"009 Summer Ridge Lane",
    "postal_code":"701 48",
    "city":"Örebro",
    "country":"Sweden"
}]

payment_options = [{
    "type": "iDeal",
    "card": "NL09INGB1540572579",
    "user": 2
},{
    "type": "VISA",
    "card": "4024007143593928",
    "user": 2
},{
    "type": "Mastercard",
    "card": "5100526199160492",
    "user": 4
},{
    "type": "iDeal",
    "card": "NL98RABO3971204384",
    "user": 5
}]

products = [{
    "name": "moonstone earrings",
    "description": "A pair of moonstone beautiful briolette / drop & dangle earrings.",
    "price": 30,
    "quantity": 12,
    "owner": 1
},
{
    "name": "very beautiful frog",
    "description": "Ceramic frog with beautiful glaze colors.",
    "price": 7.50,
    "quantity": 6,
    "owner": 3
},{
    "name": "minimalist wall calendar planner",
    "description": "The A3 size (297 x 420 mm) wall calendar runs from January 2023 through December 2023.",
    "price": 11.50,
    "quantity": 20,
    "owner": 5
},{
    "name": "4 in a row - luxury acrylic board game",
    "description": "Includes Game and 42 pieces - Lucite Acrylic.",
    "price": 160,
    "quantity": 3,
    "owner": 4
},{
    "name": "silver twist hoop earrings",
    "description": "Our newly made twist hoop earrings give you a more classy and luxurious look.",
    "price": 7.50,
    "quantity": 6,
    "owner": 1
}]

tags = [{"name": "jewelry"},
        {"name": "moonstone"},
        {"name": "figurines"},
        {"name": "ceramic"},
        {"name": "frog"},
        {"name": "calendar"},
        {"name": "minimalist"},
        {"name": "boardgame"},
        {"name": "acrylic"},
        {"name": "silver"},
        ]

producttags = [{"product": 1,"tag": 1},
               {"product": 1,"tag": 2},
               {"product": 2,"tag": 3},
               {"product": 2,"tag": 4},
               {"product": 2,"tag": 5},
               {"product": 3,"tag": 6},
               {"product": 3,"tag": 7},
               {"product": 4,"tag": 8},
               {"product": 4,"tag": 9},
               {"product": 5,"tag": 10},
               {"product": 5,"tag": 1},
               ]

transactions = [{"buyer": 2,"seller": 3,"product": 2,"quantity": 1}]

# execute

def populate_test_data():
    db.create_tables([User, PaymentOption, Product, Tag, ProductTag, TransactionLink])
    User.insert_many(users).execute()
    PaymentOption.insert_many(payment_options).execute()
    Product.insert_many(products).execute()
    Tag.insert_many(tags).execute()
    ProductTag.insert_many(producttags).execute()
    TransactionLink.insert_many(transactions).execute()

populate_test_data()