from app import app, db, ma
from models import Courier, courier_schema, couriers_schema
from flask import request, jsonify
from validation import validate_courier, validate_order
from flask_restful import abort
import re


@app.route('/courier', methods=['POST'])
def add_courier():
    courier_id = request.json['courier_id']
    courier_type = request.json['courier_type']
    regions = request.json['regions']
    working_hours = request.json['working_hours']

    new_courier = Courier(courier_id, courier_type, regions, working_hours)

    db.session.add(new_courier)
    db.session.commit()

    return courier_schema.jsonify(new_courier)

# Upload couriers in the system


@app.route('/couriers', methods=['POST'])
def add_couriers():
    data = request.json['data']
    new_couriers = []
    for courier in validate_courier(data)[0]:
        courier_id = courier['courier_id']
        courier_type = courier['courier_type']
        regions = courier['regions']
        working_hours = courier['working_hours']

        new_courier = Courier(courier_id, courier_type, regions, working_hours)
        db.session.add(new_courier)

        new_couriers.append(new_courier)
    # можно ли коммит вот здесь делать?
    db.session.commit()

    if validate_courier(data)[1]:
        return "HTTP 201 Created\n", {"couriers": couriers_schema.jsonify(new_couriers)}, 201
    else:
        return "HTTP 400 Bad Request\n", {"validation_error": jsonify(validate_courier(data)[2])}, 400

# Update info about courier


pattern = r"^([01]\d|2[0-3])\:([0-5]\d)-([01]\d|2[0-3])\:([0-5]\d)$"


@app.route('/couriers/<courier_id>', methods=['PUT'])
def update_courier(courier_id):
    courier = Courier.query.get(courier_id)
    # надо ли это тоже делать?
    if not courier:
        abort(404, messsage="Courier isn't registered in the system, cannot update")

    if request.json['courier_type']:
        if request.json['courier_type'] not in ['foot', 'bike', 'car']:
            return "HTTP 400 Bad Request\n", 400
        else:
            courier.courier_type = request.json['courier_type']
    if request.json['regions']:
        if not all(a > 0 for a in request.json['regions']):
            return "HTTP 400 Bad Request\n", 400
        else:
            courier.regions = request.json['regions']
    if request.json['working_hours']:
        if re.match(pattern, courier['working_hours']) is None:
            return "HTTP 400 Bad Request\n", 400
        else:
            courier.courier_type = request.json['working_hours']

    db.session.commit()

    return "HTTP 200 OK\n", courier_schema.jsonify(courier), 200


@app.route('/orders', methods=['POST'])
def add_orders():
    data = request.json['data']
    new_orders = []
    for order in validate_order(data)[0]:
        order_id = order['order_id']
        weight = order['weight']
        region = order['region']
        delivery_hours = order['delivery_hours']

        new_order = Courier(order_id, weight, region, delivery_hours)
        db.session.add(new_order)

        new_orders.append(new_order)
    # можно ли коммит вот здесь делать?
    db.session.commit()

    if validate_order(data)[1]:
        return "HTTP 201 Created\n", {"orders": couriers_schema.jsonify(new_orders)}, 201
    else:
        return "HTTP 400 Bad Request\n", {"validation_error": jsonify(validate_order(data)[2])}, 400



