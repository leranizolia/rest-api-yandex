import re

pattern = r"^([01]\d|2[0-3])\:([0-5]\d)-([01]\d|2[0-3])\:([0-5]\d)$"


def transform_into_dict(ids):
    list_of_dicts_with_id = []
    for i in ids:
        list_of_dicts_with_id.append({"id": i})

    return list_of_dicts_with_id


def validate_courier(data):
    validated = True
    wrong_couriers = []
    wrong_couriers_ind = []
    for ind, courier in enumerate(data):
        #print(courier)
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
                or not all(isinstance(a, int) for a in courier['regions']):
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
    print(wrong_couriers)

    if validated:
        #print(courier)
        return data, data
    else:
        #print(data)
        return [courier for courier in data if courier not in [data[x] for x in wrong_couriers_ind]], validated,\
               transform_into_dict(wrong_couriers)


data = {
    "data": [
        {
            "courier_id": 1,
            "courier_type": "foot",
            "regions": [1, 12, 22],
            "working_hours": ["11:35-14:05", "09:00-11:00"]
        },
        {
            "courier_id": 2,
            "courier_type": "bike",
            "regions": [22],
            "working_hours": ["09:00-18:00"]
        },
        {
            "courier_id": 3,
            "courier_type": "car",
            "regions": [12, 22, 23, 33],
            "working_hours": []
        }
    ]
}


a = validate_courier(data['data'])[2]

print(a)
