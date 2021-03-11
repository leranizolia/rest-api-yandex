##### SCHEMES #####


def validate_id(data):
    if not data or data < 0:
        raise ValidationError


def validate_type(data):
    if not data or data not in ['foot', 'bike', 'car']:
        raise ValidationError


def validate_regions(data):
    if not data or data not in [count(start=1)]:
        raise ValidationError

def validate_date(data):
    pattern = r"^([01]\d | 2[0-3])\:([0 - 5]\d) - ([01]\d | 2[0-3])\:([0 - 5]\d)$"
    a=0
    for i in data:
        #вот здесь надо проверить регулярку
        if re.match(pattern, i) is not None:
            a+=0
        else:
            a+=1
    return a


def validate_hours(data):
    if not data or validate_date(data)!=0:
        raise ValidationError


class CourierSchema(Schema):
    courier_id = fields.Integer(required=True, validate=validate_id)
    courier_type = fields.String(required=True, validate=validate_type)
    regions = fields.List(required=True, validate=validate_regions)
    working_hours = fields.List(REQUIRED=True, validate=validate_hours)

class OrderSchema(Schema):
    order_id = fields.Integer(required=True, validate=validate_id)
    courier_type = fields.String(required=True, validate=validate_type)
    regions = fields.List(required=True, validate=validate_regions)
    working_hours = fields.List(REQUIRED=True, validate=validate_hours)
