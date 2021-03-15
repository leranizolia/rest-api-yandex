import requests
from flask import request, jsonify


#def test_login():
#    result = requests.get('http://localhost:5000')
#    assert 200 == result.status_code


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

