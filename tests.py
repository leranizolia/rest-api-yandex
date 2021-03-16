import requests
from flask import request, jsonify


#def test_login():
#    result = requests.get('http://localhost:5000')
#    assert 200 == result.status_code

### TESTS FOR IMPORT COURIERS ###

def test_upload_couriers_valid():

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
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 201 == result.status_code


def test_upload_couriers_invalid_data_01():

    data = {
        "data_wrong": [
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
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# пустой json


def test_upload_couriers_invalid_data_02():

    data = {
        "data":
            []
            }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с индексами: список с непровалидированными индексами должен быть пустой

def test_upload_couriers_invalid_id_01():

    data = {
        "data": [
            {
                "courier_id": [],
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 6,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 'id3',
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": -100,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с courier_type

def test_upload_couriers_invalid_courier_type_01():

    data = {
        "data": [
            {
                "courier_id": 10,
                "courier_type": "feet",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 8,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 9,
                "courier_type": ["car"],
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 8,
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с courier_type и id

def test_upload_couriers_invalid_courier_type_02():

    data = {
        "data": [
            {
                "courier_id": -100,
                "courier_type": "feet",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 9,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 9,
                "courier_type": ["car"],
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 8,
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# проблема с regions


def test_upload_couriers_invalid_regions_01():

    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 12,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 9,
                "courier_type": "car",
                "regions": [-12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 8,
                "regions": [12, 'Moscow', 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 100,
                "regions": 'Moscow',
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с regions и id


def test_upload_couriers_invalid_regions_02():

    data = {
        "data": [
            {
                "courier_id": [1],
                "courier_type": "foot",
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 13,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 9,
                "courier_type": "car",
                "regions": [-12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_type": "car",
                "regions": [12, 'Moscow', 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 100,
                "courier_type": "foot",
                "regions": 'Moscow',
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# проблема с regions и type


def test_upload_couriers_invalid_regions_03():

    data = {
        "data": [
            {
                "courier_id": 14,
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 15,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 9,
                "courier_type": ["car"],
                "regions": [-12, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 16,
                "courier_type": "bikes",
                "regions": [12, 'Moscow', 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 17,
                "regions": 'Moscow',
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# проблема с regions и type и id


def test_upload_couriers_invalid_regions_04():

    data = {
        "data": [
            {
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 23,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 'nine',
                "courier_type": ["car"],
                "regions": [0.01, 22, 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": '',
                "courier_type": "bikes",
                "regions": [12, 'Moscow', 23, 33],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 17,
                "regions": 'Moscow',
                "working_hours": ["09:00-18:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с working_hours


def test_upload_couriers_invalid_working_hours_01():
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
            },
            {
                "courier_id": 2,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["30:00-18:00"]
            },
            {
                "courier_id": 3,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["18:00-09:00"]
            },
            {
                "courier_id": 22,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-10:00"]
            },
            {
                "courier_id": 4,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": "09:00-10:00"
            },
            {
                "courier_id": 21,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": []
            },


        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с working_hours и id


def test_upload_couriers_invalid_working_hours_02():
    data = {
        "data": [
            {
                "courier_id": '1',
                "courier_type": "foot",
                "regions": [1, 12, 22],
            },
            {
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["30:00-18:00"]
            },
            {
                "courier_id": -3,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["18:00-09:00"]
            },
            {
                "courier_id": 24,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-10:00"]
            },
            {
                "courier_id": 4,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": "09:00-10:00"
            },
            {
                "courier_id": [7],
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": []
            },


        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с working_hours и type


def test_upload_couriers_invalid_working_hours_03():
    data = {
        "data": [
            {
                "courier_id": 1,
                "regions": [1, 12, 22],
            },
            {
                "courier_id": 2,
                "courier_type": ["bike"],
                "regions": [22],
                "working_hours": ["30:00-18:00"]
            },
            {
                "courier_id": 3,
                "courier_type": "car8",
                "regions": [12, 22, 23, 33],
                "working_hours": ["18:00-09:00"]
            },
            {
                "courier_id": 25,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-10:00"]
            },
            {
                "courier_id": 4,
                "courier_type": " ",
                "regions": [12, 22, 23, 33],
                "working_hours": "09:00-10:00"
            },
            {
                "courier_id": 7,
                "regions": [12, 22, 23, 33],
                "working_hours": []
            },

        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с working_hours и regions


def test_upload_couriers_invalid_working_hours_04():
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
            },
            {
                "courier_id": 2,
                "courier_type": "bike",
                "regions": [22, 'Moscow'],
                "working_hours": ["30:00-18:00"]
            },
            {
                "courier_id": 3,
                "courier_type": "car",
                "regions": [0, 22, 23, 33],
                "working_hours": ["18:00-09:00"]
            },
            {
                "courier_id": 27,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-10:00"]
            },
            {
                "courier_id": 4,
                "courier_type": "foot",
                "regions": [12, 22, 23, 33.9],
                "working_hours": "09:00-10:00"
            },
            {
                "courier_id": 7,
                "courier_type": "foot",
                "regions": [],
                "working_hours": []
            },

        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# проблема с working_hours и regions и type


def test_upload_couriers_invalid_working_hours_05():
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": ["bike"],
            },
            {
                "courier_id": 2,
                "courier_type": "bikes",
                "regions": [22, 'Moscow'],
                "working_hours": ["30:00-18:00"]
            },
            {
                "courier_id": 3,
                "courier_type": 10,
                "regions": [0, 22, 23, 33],
                "working_hours": ["18:00-09:00"]
            },
            {
                "courier_id": 28,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-10:00"]
            },
            {
                "courier_id": 4,
                "courier_type": " ",
                "regions": [],
                "working_hours": "09:00-10:00"
            },
            {
                "courier_id": 7
            },

        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с working_hours и regions и type и id


def test_upload_couriers_invalid_working_hours_06():
    data = {
        "data": [
            {

            },
            {
                "courier_id": '2',
                "courier_type": "bikes",
                "regions": [22, 'Moscow'],
                "working_hours": ["30:00-18:00"]
            },
            {
                "courier_id": 3.9,
                "courier_type": 10,
                "regions": [0, 22, 23, 33],
                "working_hours": ["18:00-09:00"]
            },
            {
                "courier_id": 29,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": ["09:00-10:00"]
            },
            {
                "courier_type": " ",
                "regions": [],
                "working_hours": "09:00-10:00"
            },
            {
                "courier_id": 7
            },

        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# проблема с working_hours и regions и type и id


def test_upload_couriers_invalid_working_hours_07():
    data = {
        "data": [
            {

            },
            {

            },
            {

            },
            {

            },
            {

            },
            {

            },

        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


### TESTS FOR IMPORT ORDERS ###


def test_upload_orders_valid():

    data = {
        "data": [
            {
                "order_id": 4,
                "weight": 10.55,
                "region": 12,
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": 2,
                "weight": 43,
                "region": 22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 40,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 201 == result.status_code

# тест на невалидные формат входных данных


def test_upload_orders_invalid_data_01():

    data = {
        "data_wrong": [
            {
                "order_id": 4,
                "weight": 10.55,
                "region": 12,
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": 2,
                "weight": 43,
                "region": 22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 40,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_upload_orders_invalid_data_02():

    data = {
        "data_wrong": ''
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на невалидные id


def test_upload_orders_invalid_id():

    data = {
        "data": [
            {
                "order_id": '4',
                "weight": 10.55,
                "region": 12,
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": 2.3,
                "weight": 43,
                "region": 22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "weight": 40,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": 5,
                "weight": 40,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": -5,
                "weight": 40,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на невалидный weight


def test_upload_orders_invalid_weight_01():

    data = {
        "data": [
            {
                "order_id": 4,
                "weight": -10.55,
                "region": 12,
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": 2,
                "region": 22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 'light',
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": 5,
                "weight": 100,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": 7,
                "weight": 40,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на невалидный weight и id


def test_upload_orders_invalid_weight_02():

    data = {
        "data": [
            {
                "weight": -10.55,
                "region": 12,
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": -2,
                "region": 22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": '3',
                "weight": 'light',
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": 5,
                "weight": 100,
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": 7.5,
                "weight": '40',
                "region": 33,
                "delivery_hours": ["09:00-10:00"]
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на невалидный регион


def test_upload_orders_invalid_region_01():

    data = {
        "data": [
            {
                "order_id": 4,
                "weight": 10.55,
                "region": '12',
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": 2,
                "weight": 43,
                "region": -22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 40,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": 5,
                "weight": 43,
                "region": 22.5,
                "delivery_hours": ["09:00-15:00"]
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест на невалидный region и id


def test_upload_orders_invalid_region_03():

    data = {
        "data": [
            {
                "weight": 10.55,
                "region": '12',
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": '2',
                "weight": 43,
                "region": -22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 0.5,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": -5,
                "weight": 10,
                "region": 22.5,
                "delivery_hours": ["09:00-15:00"]
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест на невалидный region и id и weight


def test_upload_orders_invalid_region_04():

    data = {
        "data": [
            {
                "region": '12',
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": '2',
                "weight": -43,
                "region": -22,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 0.005,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": -5,
                "weight": '10',
                "region": 22.5,
                "delivery_hours": ["09:00-15:00"]
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тecт на невалидные delivery_hours


def test_upload_orders_invalid_delivery_hours_01():

    data = {
        "data": [
            {
                "order_id": 4,
                "weight": 10.55,
                "region": 12,
                "delivery_hours": "11:35-14:05"
            },
            {
                "order_id": 2,
                "weight": 43,
                "region": 22,
                "delivery_hours": ["18:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 40,
                "region": 33,
                "delivery_hours": ["30:00-10:00"]
            },
            {
                "order_id": 5,
                "weight": 40,
                "region": 33,
                "delivery_hours": []
            },
            {
                "order_id": 6,
                "weight": 10.55,
                "region": 12,
                "delivery_hours": ["11:35-14:05", 'morning']
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест на невалидные delivery_hours и id

def test_upload_orders_invalid_delivery_hours_02():

    data = {
        "data": [
            {
                "weight": 10.55,
                "region": 12,
                "delivery_hours": "11:35-14:05"
            },
            {
                "order_id": 2,
                "weight": 43,
                "region": 22,
                "delivery_hours": ["18:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 40,
                "region": 33,
                "delivery_hours": ["30:00-10:00"]
            },
            {
                "order_id": '5',
                "weight": 40,
                "region": 33,
                "delivery_hours": []
            },
            {
                "order_id": 6.01,
                "weight": 10.55,
                "region": 12,
                "delivery_hours": ["11:35-14:05", 'morning']
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на невалидные delivery_hours и weight


def test_upload_orders_invalid_delivery_hours_03():

    data = {
        "data": [
            {
                "order_id": 4,
                "weight": '10.55',
                "region": 12,
                "delivery_hours": "11:35-14:05"
            },
            {
                "order_id": 2,
                "region": 22,
                "delivery_hours": ["18:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 100,
                "region": 33,
                "delivery_hours": ["30:00-10:00"]
            },
            {
                "order_id": 5,
                "weight": -0.5,
                "region": 33,
                "delivery_hours": []
            },
            {
                "order_id": 6,
                "weight": 'heavy',
                "region": 12,
                "delivery_hours": ["11:35-14:05", 'morning']
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на невалидные delivery_hours и weight и id


def test_upload_orders_invalid_delivery_hours_04():

    data = {
        "data": [
            {
                "weight": '10.55',
                "region": 12,
                "delivery_hours": "11:35-14:05"
            },
            {
                "order_id": 2,
                "region": 22,
                "delivery_hours": ["18:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 100,
                "region": 33,
                "delivery_hours": ["30:00-10:00"]
            },
            {
                "order_id": 5.9,
                "weight": -0.5,
                "region": 33,
                "delivery_hours": []
            },
            {
                "order_id": '',
                "weight": 'heavy',
                "region": 12,
                "delivery_hours": ["11:35-14:05", 'morning']
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на невалидные delivery_hours и weight и region


def test_upload_orders_invalid_delivery_hours_06():

    data = {
        "data": [
            {
                "order_id": 4,
                "weight": '10.55',
                "region": '12',
                "delivery_hours": "11:35-14:05"
            },
            {
                "order_id": 2,
                "delivery_hours": ["18:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 100,
                "region": 33.9,
                "delivery_hours": ["30:00-10:00"]
            },
            {
                "order_id": 5,
                "weight": -0.5,
                "region": [33, 22],
                "delivery_hours": []
            },
            {
                "order_id": 6,
                "weight": 'heavy',
                "region": -12,
                "delivery_hours": ["11:35-14:05", 'morning']
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест на невалидные delivery_hours и weight и region и id


def test_upload_orders_invalid_delivery_hours_07():

    data = {
        "data": [
            {
                "weight": '10.55',
                "region": '12',
                "delivery_hours": "11:35-14:05"
            },
            {
                "order_id": 2,
                "delivery_hours": ["18:00-15:00"]
            },
            {
                "order_id": 3,
                "weight": 100,
                "region": 33.9,
                "delivery_hours": ["30:00-10:00"]
            },
            {
                "order_id": '5',
                "weight": -0.5,
                "region": [33, 22],
                "delivery_hours": []
            },
            {
                "order_id": 6.9,
                "weight": 'heavy',
                "region": -12,
                "delivery_hours": ["11:35-14:05", 'morning']
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест на невалидные delivery_hours и weight и region и id


def test_upload_orders_invalid_delivery_hours_08():

    data = {
        "data": [
            {
            },
            {
            },
            {
            },
            {
            },
            {
            },
        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


