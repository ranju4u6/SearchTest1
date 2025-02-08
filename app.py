from flask import Flask, request, jsonify

from services.elastic_service import ElasticService

app = Flask(__name__)
elastic_service = ElasticService()


#     elastic_service = ElasticService()
#     e_products = elastic_service.search("Electronics")
#     print(e_products)

@app.route("/prod_with_categ", methods=["GET"])
def get_products_with_categories():
    print("ok.. received")
    category = request.args.get("category")
    print(category)
    e_products = elastic_service.search(category)
    print(e_products)
    return jsonify(e_products), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
