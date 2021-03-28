from app import db, ma
from datetime import datetime
import re
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from itertools import count


##### MODELS #####

class Courier(db.Model):
    courier_id = db.Column(db.Integer, primary_key=True, nullable=False)
    courier_type = db.Column(db.String(100), nullable=False)
    regions = db.Column(db.PickleType, nullable=False)
    working_hours = db.Column(db.PickleType, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Courier, self).__init__(*args, **kwargs)

    orders = db.relationship('Order', backref='courier', lazy=True)

    def __repr__(self):
        courier = dict()
        courier['courier_id'] = self.courier_id
        courier['courier_type'] = self.courier_type
        courier['regions'] = self.regions
        courier['working_hours'] = self.working_hours
        return str(courier)


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    region = db.Column(db.Integer, nullable=False)
    delivery_hours = db.Column(db.PickleType, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)

    # дополнительные колонки, которые появляются от взаимодействия с курьером
    courier_id = db.Column(db.Integer, db.ForeignKey('courier.courier_id'), nullable=True)
    assign_time = db.Column(db.DateTime, nullable=True)
    complete_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        order = dict()
        order['order_id'] = self.order_id
        order['weight'] = self.weight
        order['region'] = self.region
        order['delivery_hours'] = self.delivery_hours
        return str(order)


db.create_all()







