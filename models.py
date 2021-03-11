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
    courier_type = db.Column(db.String(10), nullable=False)
    regions = db.Column(db.PickleType, nullable=False)
    working_hours = db.Column(db.PickleType, nullable=False)
    orders = db.relationship('Order', backref='courier', lazy=True)

    def __init__(self, *args, **kwargs):
        super(Courier, self).__init__(*args, **kwargs)

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
    courier_id = db.Column(db.Integer, db.ForeignKey('courier.courier_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)

    def __repr__(self):
        order = dict()
        order['order_id'] = self.order_id
        order['weight'] = self.weight
        order['region'] = self.region
        order['delivery_hours'] = self.delivery_hours
        return str(order)


db.create_all()

##### SCHEMES #####


class CouriersSchema(ma.Schema):
    class Meta:
        # fields = {'courier_id', 'courier_type', 'regions', 'working_hours'}
        fields = {'courier_id'}


# надо сделать как-то более оптимально - вариацию полей для каждого задания
class CourierSchema(ma.Schema):
    class Meta:
        fields = {'courier_id', 'courier_type', 'regions', 'working_hours'}
        # fields = {'courier_id'}


class OrderSchema(ma.Schema):
    class Meta:
        fields = {'order_id', 'weight', 'region', 'delivery_hours'}


courier_schema = CourierSchema(strict=True)
couriers_schema = CouriersSchema(many=True, sctrict=True)


order_schema = OrderSchema(strict=True)
orders_schema = OrderSchema(many=True, strict=True)





