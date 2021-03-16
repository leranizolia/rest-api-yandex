from app import app, db, ma
from models import Courier, Order
from flask import request, jsonify
import re
from datetime import datetime, timezone
from flask import Response
import json


def transform_into_dict(ids):
    list_of_dicts_with_id = []
    for i in ids:
        list_of_dicts_with_id.append({"id": i})

    return list_of_dicts_with_id


from validation import validate_courier, validate_order


def has_overlap(c, o):
    for one_time_c in c:
        c_start = datetime.strptime(one_time_c[0], format)
        c_end = datetime.strptime(one_time_c[1], format)
        courier_matching_time = one_time_c
        for one_time_o in o:
            o_start = datetime.strptime(one_time_o[0], format)
            o_end = datetime.strptime(one_time_o[1], format)
            order_matching_time = one_time_o
            latest_start = max(c_start, o_start)
            earliest_end = min(c_end, o_end)
            match = latest_start < earliest_end
            return match


# Upload couriers in the system


@app.route('/couriers', methods=['POST'])
def add_couriers():
    try:
        data = request.json['data']
    # если вход неправильно формата
    except:
        response = app.response_class(response="HTTP 400 Bad Request\n" + "Please check the input data format",
                                      status=400,
                                      )
        return response
    if len(data) == 0:
        response = app.response_class(response="HTTP 400 Bad Request\n" + "Please check the input data format",
                                      status=400,
                                      )
        return response

    new_couriers_id = []
    data = validate_courier(data)
    for courier in data[0]:
        courier_id = courier['courier_id']
        courier_type = courier['courier_type']
        regions = courier['regions']
        working_hours = courier['working_hours']

        new_courier = Courier(courier_id=courier_id, courier_type=courier_type, regions=regions, working_hours=working_hours)
        db.session.add(new_courier)

        new_couriers_id.append(new_courier.courier_id)

    db.session.commit()

    if data[1]:
        data = {"couriers": transform_into_dict(new_couriers_id)}
        response = app.response_class(response="HTTP 201 Created\n" + json.dumps(data),
                                      status=201,
                                      mimetype="application/json"
                                      )
    else:
        data = {"validation_error": {"couriers": data[2]}}
        response = app.response_class(response="HTTP 400 Bad Request\n" + json.dumps(data),
                                      status=400,
                                      mimetype="application/json"
                                      )
    return response

# Update info about courier


pattern = r"^([01]\d|2[0-3])\:([0-5]\d)-([01]\d|2[0-3])\:([0-5]\d)$"
format = '%H:%M'


@app.route('/couriers/<courier_id>', methods=['PATCH'])
def update_courier(courier_id):
    update = False
    courier = Courier.query.get(courier_id)
    # если курьера нет в системе
    if courier is None:
        response = app.response_class(response="HTTP 404 Not found\n" + "Please check the id of courier",
                                      status=404)
        return response
    try:
        result = request.json['courier_type']
        if not isinstance(result, str) or result not in ['foot', 'bike', 'car']:
            response = app.response_class(response="HTTP 400 Bad Request\n", status=400)
            return response
        else:
            courier.courier_type = result
            update = True
    except KeyError:
        pass
    try:
        result = request.json['regions']
        if (not isinstance(result, list)) or len(result) == 0 or not all(isinstance(a, int) for a in result) or not all(a > 0 for a in result):
            response = app.response_class(response="HTTP 400 Bad Request\n", status=400)
            return response
        else:
            courier.regions = result
            update = True
    except KeyError:
        pass
    try:
        result = request.json['working_hours']
        if not isinstance(result, list) or (len(result) == 0)\
                or not all(re.match(pattern, a) is not None for a in result)\
                or not all(datetime.strptime(a.split('-')[0], format) < datetime.strptime(a.split('-')[1], format) for a in result):
            response = app.response_class(response="HTTP 400 Bad Request\n", status=400)
            return response
        else:
            courier.working_hours = result
            update = True
    except KeyError:
        #если пользователь запросил изменить  несуществующее поле
        pass

    if update:
        weight_possible = 0
        if courier.courier_type == 'foot':
            weight_possible = 10
        elif courier.courier_type == 'bike':
            weight_possible = 15
        elif courier.courier_type == 'car':
            weight_possible = 50

        working_hours = courier.working_hours
        start_hours_c = []
        end_hours_c = []
        courier_hours = []
        for period in working_hours:
            start_hours_c.append(period.split('-')[0])
            end_hours_c.append(period.split('-')[1])
            courier_hours.append((period.split('-')[0], period.split('-')[1]))
    # проверка на соответствие заказов курьера его новым параметрам
        orders_has = Order.query.filter(Order.courier_id == courier_id)
        for order in orders_has:
            delivery_hours = order.delivery_hours
            start_hours_o = []
            end_hours_o = []
            order_hours = []
            for period in delivery_hours:
                start_hours_o.append(period.split('-')[0])
                end_hours_o.append(period.split('-')[1])
                order_hours.append((period.split('-')[0], period.split('-')[1]))
            # сбрасываем заказы, которые не соответствуют обновленным параметрам курьера
            if not ((float("{0:.2f}".format(order.weight)) <= weight_possible) and (order.region in courier.regions)
                    and has_overlap(courier_hours, order_hours)):
                order.courier_id = None
                order.assign_time = None

        db.session.commit()

        data = {"courier_id": courier.courier_id, "courier_type": courier.courier_type, "regions": courier.regions,
                "working_hours": courier.working_hours}
        response = app.response_class(response="HTTP 200 OK\n" + json.dumps(data), status=200, mimetype="application/json")
        return response
    else:
        response = app.response_class(response="HTTP 400 Bad Request\n",
                                      status=400)
        return response


# Upload orders into the system

@app.route('/orders', methods=['POST'])
def add_orders():
    try:
        data = request.json['data']
    # если вход неправильно формата
    except:
        response = app.response_class(response="HTTP 400 Bad Request\n" + "Please check the input data format",
                                      status=400)
        return response
    if len(data) == 0:
        response = app.response_class(response="HTTP 400 Bad Request\n" + "Please check the input data format",
                                      status=400)
        return response
    new_orders_id = []
    data = validate_order(data)
    for order in data[0]:
        order_id = order['order_id']
        weight = order['weight']
        region = order['region']
        delivery_hours = order['delivery_hours']

        new_order = Order(order_id=order_id, weight=weight, region=region, delivery_hours=delivery_hours)
        db.session.add(new_order)

        new_orders_id.append(new_order.order_id)

    db.session.commit()

    if data[1]:
        data = {"orders": transform_into_dict(new_orders_id)}
        response = app.response_class(response="HTTP 201 Created\n" + json.dumps(data),
                                      status=201,
                                      mimetype="application/json"
                                      )
    else:
        data = {"validation_error": {"orders": data[2]}}
        response = app.response_class(response="HTTP 400 Bad Request\n" + json.dumps(data),
                                      status=400,
                                      mimetype="application/json"
                                      )
    return response

# для пересечения времени
#def has_overlap(c_start, c_end, o_start, o_end):
#    latest_start = max(c_start, o_start)
#   earliest_end = min(c_end, o_end)
#   return latest_start <= earliest_end


@app.route('/orders/assign', methods=['POST'])
def assign():
    try:
        courier_id = request.json['courier_id']
    # если вход неправильно формата
    except:
        response = app.response_class(response="HTTP 400 Bad Request\n" + "Please check the input data format",
                                      status=400)
        return response
    courier = Courier.query.get(courier_id)
    # если курьера нет в системе
    if courier is None:
        response = app.response_class(response="HTTP 400 Bad Request\n", status=400)
        return response
    courier_id_pk = courier_id
    # Порог для веса заказа в зависимости от типа курьера
    courier_type = courier.courier_type
    weight_possible = 0
    if courier_type == 'foot':
        weight_possible = 10
    elif courier_type == 'bike':
        weight_possible = 15
    elif courier_type == 'car':
        weight_possible = 50

    regions = courier.regions
    working_hours = courier.working_hours
    start_hours_c = []
    end_hours_c = []
    courier_hours = []
    for period in working_hours:
        start_hours_c.append(period.split('-')[0])
        end_hours_c.append(period.split('-')[1])
        # проверить правильно ли tuple передала
        courier_hours.append((period.split('-')[0], period.split('-')[1]))

    orders_id_assign = []

    all_orders = Order.query.all()
    for order in all_orders:
        order_id = order.order_id
        weight = order.weight
        region = order.region
        complete_time = order.complete_time
        assign_time = order.assign_time
        delivery_hours = order.delivery_hours
        start_hours_o = []
        end_hours_o = []
        order_hours = []
        for period in delivery_hours:
            start_hours_o.append(period.split('-')[0])
            end_hours_o.append(period.split('-')[1])
            order_hours.append((period.split('-')[0], period.split('-')[1]))
        courier_id_fk = order.courier_id
        # если у заказа нет курьера
        # надо ещё передать список старых not complete заказов
        if (courier_id_fk is None) or (courier_id_fk == courier_id_pk):
            # проверяем на соответствие параметрам курьера
            if (float("{0:.2f}".format(weight)) <= weight_possible) and (region in regions)\
                    and has_overlap(courier_hours, order_hours):
                # если курьер мэтчится с заказом, то надо:
                # 1) присвоить заказ,
                # 2) assign time,
                # 3) добавить в список заказов курьера
                order.courier_id = courier_id_pk
                assign_time_new = datetime.utcnow()
                orders_id_assign.append(order_id)
                # проверяем случай если курьер уже доставил ранее выданные заказы
                # заказы, которые курьер уже доставил
                if complete_time is not None:
                    orders_id_assign.remove(order_id)
                    # ставим assign time для новых заказов (в задании не сказано, что делать со старыми заказами
                    # с assign_time
                    # предположим, что assign_time для них не меняется (логично)
                #if assign_time is None:
                    # для оставшихся невыполненных заказов нужно поменять assign время
                order.assign_time = assign_time_new

    db.session.commit()

    if len(orders_id_assign) == 0:
        data = {"orders": []}
        response = app.response_class(response=json.dumps(data), mimetype="application/json")
        return response
    else:
        data = {"orders": transform_into_dict(orders_id_assign), "assign_time": str(assign_time_new.isoformat("T") + "Z")}
        response = app.response_class(response="HTTP 200 OK\n" + json.dumps(data), status=200,
                                      mimetype="application/json")
        return response


@app.route('/orders/complete', methods=['POST'])
# делаю дефолт для complete_time, чтобы в assign не вылезла ошибка при вызове complete
def complete():
    courier_id = request.json['courier_id']
    order_id = request.json['order_id']
    order = Order.query.get(order_id)
    order_id = order.order_id
    assign_time = order.assign_time
    complete_time = request.json['complete_time']

    db.session.commit()

    if not order_id or courier_id != order.courier_id or not assign_time:
        return "HTTP 400 Bad Request\n", 400
    else:
        order.complete_time = complete_time
        return "HTTP 200 OK\n", jsonify({"id": order_id}), 200


















