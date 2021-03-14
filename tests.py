import requests
from flask import request, jsonify


#def test_login():
#    result = requests.get('http://localhost:5000')
#    assert 200 == result.status_code


def test_upload_couriers():

    data = {
        "data": [
            {
                "courier_id": 37,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            },
            {
                "courier_id": 36,
                "courier_type": "bike",
                "regions": [22],
                "working_hours": ["09:00-18:00"]
            },
            {
                "courier_id": 37,
                "courier_type": "car",
                "regions": [12, 22, 23, 33],
                "working_hours": []
            }
        ]
    }

    result = requests.post('http://127.0.0.1:5000/couriers', json=data, headers={'Content-Type': 'application/json'})
    print(result)
    # assert 201 == result.status_code


