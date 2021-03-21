import requests


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


# TESTS FOR IMPORT ORDERS


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

# тест на невалидный формат входных данных


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

# ТЕСТЫ ДЛЯ UPDATE COURIER

# Тест из файла с заданием


def test_update_courier_valid():

    data = {
                "regions": [11, 33, 2, 10]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/2', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


# Тест с апдейтами нескольких полей


def test_update_courier_valid_2_fields():

    data = {
                "regions": [11, 33, 2],
                "courier_type": "bike"
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/2', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_update_courier_valid_3_fields():

    data = {
                "regions": [11, 33, 2, 7],
                "courier_type": "bike",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/2', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code

# Тест с попыткой изменить поле несуществующего курьера


def test_update_courier_invalid_courier_id():

    data = {
                "regions": [11, 33, 2, 7],
                "courier_type": "bike",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1000', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 404 == result.status_code

# Тест с невалидным форматом входа


def test_update_courier_invalid_input_format_01():

    data = {
                "courier_id": 100
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_input_format_02():

    data = {
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест с невалидным полем regions для изменения


def test_update_courier_invalid_courier_regions_01():

    data = {
                "regions": [11, 33, 2, "Moscow"],
                "courier_type": "bike",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_courier_regions_02():

    data = {
                "regions": "Moscow",
                "courier_type": "bike",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_courier_regions_03():

    data = {
                "regions": [],
                "courier_type": "bike",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_courier_regions_04():

    data = {
                "regions": [0, 1, 2, 3],
                "courier_type": "bike",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест с невалидным полем courier_type для изменения


def test_update_courier_invalid_courier_type_01():

    data = {
                "regions": [11, 33, 2],
                "courier_type": "bikes",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_courier_type_02():

    data = {
                "regions": [11, 33, 2],
                "courier_type": " ",
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_courier_type_03():

    data = {
                "regions": [11, 33, 2],
                "courier_type": 100,
                "working_hours": ["09:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест с невалидным полем courier_type для изменения


def test_update_courier_invalid_working_hours_01():

    data = {
                "regions": [11, 33, 2],
                "courier_type": "bike",
                "working_hours": ["18:00-17:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_working_hours_02():

    data = {
                "regions": [11, 33, 2],
                "courier_type": "bike",
                "working_hours": ["18:00-30:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_working_hours_03():

    data = {
                "regions": [11, 33, 2],
                "courier_type": "bike",
                "working_hours": "10:00-18:00"
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_update_courier_invalid_working_hours_04():

    data = {
                "regions": [11, 33, 2],
                "courier_type": "bike",
                "working_hours": []
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/1', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# ТЕСТЫ ДЛЯ ASSIGN COURIER

def test_upload_orders_suitable_for_courier_2():

    data = {
        "data": [
            {
                "order_id": 10,
                "weight": 10.55,
                "region": 2,
                "delivery_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "order_id": 11,
                "weight": 43,
                "region": 10,
                "delivery_hours": ["09:00-15:00"]
            },
            {
                "order_id": 12,
                "weight": 8.95,
                "region": 13,
                "delivery_hours": ["09:00-10:00"]
            },
            {
                "order_id": 13,
                "weight": 5,
                "region": 10,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 14,
                "weight": 11,
                "region": 10,
                "delivery_hours": ["10:00-15:00"]
            }

        ]
    }

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 201 == result.status_code

# Тест из файла с заданием

# случай, когда есть заказы, которые соответствуют параметрам курьера


def test_assign_order_valid_01():

    data = {
                "courier_id": 2
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code

# случай, когда нет заказов, соответствующих параметрам курьера


def test_assign_order_valid_02():

    data = {
                "courier_id": 4
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)

# Тест на неправильный формат входных данных


def test_assign_order_invalid_input_01():

    data = {
                "id": 2
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_assign_order_invalid_input_02():

    data = {}

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на несуществующего курьера или ошибку в написаний id


def test_assign_order_invalid_id_01():

    data = {
                "courier_id": 1234567
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_assign_order_invalid_id_02():

    data = {
                "courier_id": 'second'
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Теперь добавим в базу побольше курьеров и заказов для тестов


def test_upload_couriers_valid_100():

    from data_couriers import data

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 201 == result.status_code


def test_upload_orders_valid_100():

    from data_orders import data

    result = requests.post('http://127.0.0.1:5000/orders', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 201 == result.status_code

# Теперь подберем заказы курьерам с помощью assign


def test_assign_order_valid_101():

    data = {
                "courier_id": 101
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_102():

    data = {
                "courier_id": 102
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_103():

    data = {
                "courier_id": 103
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_104():

    data = {
                "courier_id": 104
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_105():

    data = {
                "courier_id": 105
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_106():

    data = {
                "courier_id": 106
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_107():

    data = {
                "courier_id": 107
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_108():

    data = {
                "courier_id": 108
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_109():

    data = {
                "courier_id": 109
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_110():

    data = {
                "courier_id": 110
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_111():

    data = {
                "courier_id": 111
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_112():

    data = {
                "courier_id": 112
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_113():

    data = {
                "courier_id": 113
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_114():

    data = {
                "courier_id": 114
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_115():

    data = {
                "courier_id": 115
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code

# Тесты для complete

# Тесты на невалидных курьеров


def test_complete_order_invalid_courier_id_01():

    data = {
                "courier_id": 200,
                "order_id": 101,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_complete_order_invalid_courier_id_02():

    data = {
                "courier_id": 'second',
                "order_id": 101,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_complete_order_invalid_courier_id_03():

    data = {
                "order_id": 101,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тесты на невалидные заказы


def test_complete_order_invalid_order_id_01():

    data = {
                "courier_id": 101,
                "order_id": 200,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_complete_order_invalid_order_id_02():

    data = {
                "courier_id": 101,
                "order_id": 200,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_complete_order_invalid_order_id_03():

    data = {
                "courier_id": 101,
                "order_id": 'second',
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


def test_complete_order_invalid_order_id_04():

    data = {
                "courier_id": 101,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code

# Тест на случай когда у заказа другой курьер


def test_complete_order_invalid_order_id_05():

    data = {
                "courier_id": 101,
                "order_id": 103,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест на случай когда у заказа нет курьера


def test_complete_order_invalid_order_id_06():

    data = {
                "courier_id": 101,
                "order_id": 104,
                "complete_time": "2021-01-10T10:33:01.42Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 400 == result.status_code


# Тест на валидный запрос complete

def test_complete_order_valid():

    data = {
                "courier_id": 101,
                "order_id": 102,
                "complete_time": "2021-03-21T10:46:52.25Z"
            }

    result = requests.post('http://127.0.0.1:5000/orders/complete', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code

# Теперь проверим как работает assign с выполненными заказами

# По правилам в списке заказов курьера 101 не должно быть 102 заказа, т к он его выполнил


def test_assign_order_valid_101_new():

    data = {
                "courier_id": 101
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code

# Теперь проверим апдейт для назначенных заказов

# Сначала посмотрим какие заказы у курьера


def test_assign_order_valid_108_again():

    data = {
                "courier_id": 108
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_update_courier_valid_for_108_update_type():

    data = {
                "courier_type": "foot"
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/108', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_108_new():

    data = {
                "courier_id": 108
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_update_courier_valid_for_108_update_regions():

    data = {
                "regions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/108', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_108_new_new():

    data = {
                "courier_id": 108
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_update_courier_valid_for_108_update_working_hours():

    data = {
                "working_hours": ["07:00-21:00"]
            }

    result = requests.patch('http://127.0.0.1:5000/couriers/108', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code


def test_assign_order_valid_108_new_new_new():

    data = {
                "courier_id": 108
            }

    result = requests.post('http://127.0.0.1:5000/orders/assign', json=data, headers={'Content-Type': 'application/json'})
    print(result.text)
    assert 200 == result.status_code




