
import enum

class Speed(enum.Enum):
    speedsingle  = "Single Speed"
    speed6 = "6 Speed"
    speed7 = "7 Speed"
    speed12 = "12 Speed"
    speed18 = "18 Speed"
    speed21 = "21 Speed"
    speed24 = "24 Speed"
    

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class Size(enum.Enum):
    size12 = '12T'
    size14 = '14T'
    size16 = "16T"
    size18 = "18T"
    size20 = "20T"
    size24 = "24T"
    size26 = "26T"
    size275 = "27.5T"
    size29 = "29T"
    freesize = "Free Size"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class OrderStatus(enum.Enum):
   
    shipped = "Shipped"
    delivered = "Delivered"
    cancelled = "Cancelled"
    returned = "Returned"
    initiated = "Initiated"
    confirmed = "Confirmed"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

