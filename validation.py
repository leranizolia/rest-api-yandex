import re
from view import transform_into_dict
from datetime import datetime

pattern_assign = r"^([01]\d|2[0-3])\:([0-5]\d)-([01]\d|2[0-3])\:([0-5]\d)$"
format = '%H:%M'

# проверка полей курьера на соответствие требованиям


def validate_courier(data):
    validated = True
    wrong_couriers = []
    wrong_couriers_ind = []
    for ind, courier in enumerate(data):
        if courier.get('courier_id', 'missed id') == 'missed id' or not isinstance(courier['courier_id'], int) \
                or courier['courier_id'] <= 0:
            wrong_couriers_ind.append(ind)
            validated = False
        if courier.get('courier_type', 'missed type') == 'missed type' or not isinstance(courier['courier_type'], str)\
                or courier['courier_type'] not in ['foot', 'bike', 'car']:
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if ind not in wrong_couriers_ind:
                wrong_couriers.append(courier['courier_id'])
            wrong_couriers_ind.append(ind)
        if courier.get('regions', 'missed regions') == 'missed regions' or not isinstance(courier['regions'], list)\
                or len(courier['regions']) == 0\
                or not all(isinstance(a, int) for a in courier['regions']) \
                or not all(a > 0 for a in courier['regions']):
            wrong_couriers_ind.append(ind)
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if not (courier.get('courier_id', 'missed id') == 'missed id' or not isinstance(courier['courier_id'], int)
                    or courier['courier_id'] <= 0):
                wrong_couriers.append(courier['courier_id'])
        if courier.get('working_hours', 'missed working hours') == 'missed working hours'\
                or not isinstance(courier['working_hours'], list)\
                or len(courier['working_hours']) == 0\
                or not all(re.match(pattern_assign, a) is not None for a in courier['working_hours'])\
                or not all(datetime.strptime(a.split('-')[0], format) < datetime.strptime(a.split('-')[1], format) for a in courier['working_hours']):
            wrong_couriers_ind.append(ind)
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if not (courier.get('courier_id', 'missed id') == 'missed id' or not isinstance(courier['courier_id'], int)
                    or courier['courier_id'] <= 0):
                wrong_couriers.append(courier['courier_id'])

    wrong_couriers_ind = list(set(wrong_couriers_ind))
    wrong_couriers = list(set(wrong_couriers))

    if validated:
        return data, validated
    else:
        return [courier for courier in data if courier not in [data[x] for x in wrong_couriers_ind]], validated,\
               transform_into_dict(wrong_couriers)


def validate_order(data):
    validated = True
    wrong_orders = []
    wrong_orders_ind = []
    for ind, order in enumerate(data):
        if order.get('order_id', 'missed id') == 'missed id' or not isinstance(order['order_id'], int) \
                or order['order_id'] <= 0:
            wrong_orders_ind.append(ind)
            validated = False
        if order.get('weight', 'missed weight') == 'missed weight' or not (isinstance(order['weight'], float) or isinstance(order['weight'], int))\
                or not (0.01 <= order['weight'] <= 50):
            validated = False
            # если заказ не относится к категории, у которой проблема с id
            if ind not in wrong_orders_ind:
                wrong_orders.append(order['order_id'])
            wrong_orders_ind.append(ind)
        if order.get('region', 'missed region') == 'missed region' or not isinstance(order['region'], int) \
                or order['region'] <= 0:
            wrong_orders_ind.append(ind)
            validated = False
            # если заказ не относится к категории, у которой проблема с id
            if not (order.get('order_id', 'missed id') == 'missed id' or not isinstance(order['order_id'], int)
                    or order['order_id'] <= 0):
                wrong_orders.append(order['order_id'])
        if order.get('delivery_hours', 'missed delivery hours') == 'missed delivery hours'\
                or not isinstance(order['delivery_hours'], list)\
                or len(order['delivery_hours']) == 0\
                or not all(re.match(pattern_assign, a) is not None for a in order['delivery_hours'])\
                or not all(datetime.strptime(a.split('-')[0], format) < datetime.strptime(a.split('-')[1], format) for a in order['delivery_hours']):
            wrong_orders_ind.append(ind)
            validated = False
            # если заказ не относится к категории, у которой проблема с id
            if not (order.get('order_id', 'missed id') == 'missed id' or not isinstance(order['order_id'], int)
                    or order['order_id'] <= 0):
                wrong_orders.append(order['order_id'])

    wrong_orders_ind = list(set(wrong_orders_ind))
    wrong_orders = list(set(wrong_orders))

    if validated:
        return data, validated
    else:
        return [order for order in data if order not in [data[x] for x in wrong_orders_ind]], validated,\
               transform_into_dict(wrong_orders)



