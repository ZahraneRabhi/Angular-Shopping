from flask import Flask, jsonify, request
from time import sleep

app = Flask(__name__)

cart = []

@app.route("/api/products")
def get_products():
    products = [
        { "id": 1, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 1", "imageName": "product1.jpg", "category": "category-1", "price": 50, "discount": 0 },
        { "id": 2, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 2", "imageName": "product2.jpg", "category": "category-2", "price": 10, "discount": 0 },
        { "id": 3, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 3", "imageName": "product3.jpg", "category": "category-3", "price": 70, "discount": 0 },
        { "id": 4, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 4", "imageName": "product4.jpg", "category": "category-1", "price": 20, "discount": 0.1 },
        { "id": 5, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 5", "imageName": "product5.jpg", "category": "category-2", "price": 180, "discount": 0.2 },
        { "id": 6, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 6", "imageName": "product6.jpg", "category": "category-3", "price": 220, "discount": 0 },
        { "id": 7, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 7", "imageName": "product7.jpg", "category": "category-1", "price": 130, "discount": 0.1 },
        { "id": 8, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 8", "imageName": "product8.jpg", "category": "category-2", "price": 160, "discount": 0.1 },
        { "id": 9, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 9", "imageName": "product9.jpg", "category": "category-3", "price": 90, "discount": 0 },
        { "id": 10, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 10", "imageName": "product10.jpg", "category": "category-1", "price": 110, "discount": 0 },
        { "id": 11, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 11", "imageName": "product11.jpg", "category": "category-2", "price": 170, "discount": 0 },
        { "id": 12, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 12", "imageName": "product12.jpg", "category": "category-3", "price": 230, "discount": 0 },
        { "id": 13, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 13", "imageName": "product13.jpg", "category": "category-1", "price": 140, "discount": 0 },
        { "id": 14, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 14", "imageName": "product14.jpg", "category": "category-2", "price": 190, "discount": 0.3 },
        { "id": 15, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 15", "imageName": "product15.jpg", "category": "category-3", "price": 240, "discount": 0 },
        { "id": 16, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "name": "Product 16", "imageName": "product16.jpg", "category": "category-1", "price": 125, "discount": 0 }
    ]
    return jsonify(products)

@app.route("/api/cart", methods=["POST"])
def update_cart():
    global cart
    cart = request.json
    sleep(0.02) # 0.2 sec delay 
    return "", 201

@app.route("/api/cart", methods=["GET"])
def get_cart():
    return jsonify(cart)

if __name__ == "__main__":
    app.run(port=8081)
