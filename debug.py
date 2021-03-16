from datetime import datetime

pattern = r"^([01]\d|2[0-3])\:([0-5]\d)-([01]\d|2[0-3])\:([0-5]\d)$"
format = '%H:%M'


def has_overlap(c, o):
    for one_time_c in c:
        c_start = datetime.strptime(one_time_c[0], format)
        c_end = datetime.strptime(one_time_c[1], format)
        courier_matching_time = one_time_c
        for one_time_o in o:
            o_start = datetime.strptime(one_time_o[0], format)
            o_end = datetime.strptime(one_time_o[1], format)
            order_matching_time = one_time_o
            latest_start = max(c_start, o_start)
            earliest_end = min(c_end, o_end)
            match = latest_start < earliest_end
            return match



result = has_overlap([("09:00", "17:00")], [("16:00", "18:00")])
print(result)