from flask import Blueprint, jsonify

#Blueprint -> organizes the routes into differents files
blueprint = Blueprint('product', __name__, url_prefix='/api/products')

#Creates the root route '/' with method get
@blueprint.route('/', methods=['GET'])
def list_products():
    products = [
        {'id': 1, 'name': 'Vela de lavanda'}
    ]
    #returns a product in the json format
    return jsonify(products)