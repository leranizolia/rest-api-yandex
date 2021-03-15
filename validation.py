### в предположении, что отсутвие ключа или несоответствие его значения требованиям приводят к одной ошибке
### что значит неописанные поля - пробел или пропуск?
import re
from view import transform_into_dict

pattern = r"^([01]\d|2[0-3])\:([0-5]\d)-([01]\d|2[0-3])\:([0-5]\d)$"

# проверка полей курьера на соответствие требованиям


def validate_courier(data):
    validated = True
    wrong_couriers = []
    wrong_couriers_ind = []
    for ind, courier in enumerate(data):
        if courier.get('courier_id', 'missed id') == 'missed id' or courier['courier_id'] == str(' ') \
                or courier['courier_id'] <= 0\
                or not isinstance(courier['courier_id'], int):
            wrong_couriers_ind.append(ind)
            validated = False
        if courier.get('courier_type', 'missed type') == 'missed type' or courier['courier_type'] not in ['foot', 'bike', 'car']:
            wrong_couriers_ind.append(ind)
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if ind not in wrong_couriers_ind:
                wrong_couriers.append(courier['courier_id'])
        if courier.get('regions', 'missed regions') == 'missed regions' or not all(a > 0 for a in courier['regions']) \
                or not all(isinstance(a, int) for a in courier['regions']) or courier['regions'] == []:
            wrong_couriers_ind.append(ind)
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if courier.get('courier_id', 'missed id') != 'missed id' and courier['courier_id'] != str(' ')\
                    or courier['courier_id'] <= 0 or type(courier['courier_id']) != 'int':
                wrong_couriers.append(courier['courier_id'])
        if courier.get('working_hours', 'missed working hours') == 'missed working hours'\
                or not all(re.match(pattern, a) is not None for a in courier['working_hours']) or courier['working_hours']==[]:
            wrong_couriers_ind.append(ind)
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if courier.get('courier_id', 'missed id') != 'missed id' and courier['courier_id'] != str(' ')\
                    or courier['courier_id'] <= 0 or type(courier['courier_id']) != 'int':
                wrong_couriers.append(courier['courier_id'])

    wrong_couriers_ind = list(set(wrong_couriers_ind))
    wrong_couriers = list(set(wrong_couriers))

    if validated:
        return data, data
    else:
        return [courier for courier in data if courier not in [data[x] for x in wrong_couriers_ind]], validated,\
               transform_into_dict(wrong_couriers)


def validate_order(data):
    validated = True
    wrong_orders = []
    wrong_orders_ind = []
    for ind, order in enumerate(data):
        if order.get('order_id', 'missed id') == 'missed id' or order['order_id'] == str(' ') or order['order_id'] <= 0\
                or type(order['order_id']) != 'int':
            wrong_orders_ind.append(ind)
            validated = False
        if order.get('weight', 'missed weight') == 'missed weight' or not (0.01 <= order['weight'] <= 50):
            wrong_orders_ind.append(ind)
            validated = False
            # если заказ не относится к категории, у которой проблема с id
            if ind not in wrong_orders_ind:
                wrong_orders.append(order['order_id'])
        if order.get('region', 'missed region') == 'missed region' or not all(a > 0 for a in order['region']) \
                or not all(type(a) == 'int' for a in order['region']):
            wrong_orders_ind.append(ind)
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if order.get('order_id', 'missed id') != 'missed id' and order['order_id'] != str(' ')\
                    or order['order_id'] <= 0 or type(order['order_id']) != 'int':
                wrong_orders.append(order['courier_id'])
        if order.get('delivery_hours', 'missed delivery hours') == 'missed delivery hours' \
                or re.match(pattern, order['delivery_hours']) is None:
            wrong_orders_ind.append(ind)
            validated = False
            # если курьер не относится к категории, у которой проблема с id
            if order.get('order_id', 'missed id') != 'missed id' and order['courier_id'] != str(' ')\
                    or order['order_id'] <= 0 or type(order['order_id']) != 'int':
                wrong_orders.append(order['courier_id'])

    wrong_orders_ind = set(wrong_orders_ind)
    wrong_orders = set(wrong_orders)

    if validated:
        return data, validated
    else:
        return [order for order in data if order not in data[wrong_orders_ind]], validated,\
               transform_into_dict(wrong_orders)

