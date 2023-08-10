import json


class Booking:
    def __init__(self, **kwargs):
        self.firstname = "John" if "firstname" not in kwargs.keys() else kwargs["firstname"]
        self.lastname = "Smith" if "lastname" not in kwargs.keys() else kwargs["lastname"]
        self.totalprice = 937 if 'totalprice' not in kwargs.keys() else kwargs['totalprice']
        self.depositpaid = True if "depositpaid" not in kwargs.keys() else kwargs["depositpaid"]
        self.bookingdates = {"checkin": "2013-02-23", "checkout": "2014-10-23"} \
            if "bookingdates" not in kwargs.keys() else kwargs["bookingdates"]

    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)

    def get_dict(self):
        return self.__dict__
