class Mobile:
    model_name = 'S8'
    max_heat = 100

    def __init__(self, color, price, heat):
        self.color = color
        self.price = price
        self.heat = heat

    def getmaxheat_1():
        return Mobile.max_heat

    @staticmethod
    def getmaxheat_2():
        return Mobile.max_heat

    @classmethod
    def getmaxheat_3(cls):
        return cls.max_heat

    @classmethod
    def getmodel(cls):
        return cls.model_name

    @classmethod
    def updatemaxheat(cls,num):
        cls.max_heat = num

    @staticmethod
    def fromstring(stringinit):
        return Mobile(stringinit.split()[0],
                      stringinit.split()[1],
                      stringinit.split()[2])

    @staticmethod
    def fromlist(lst1):
        return Mobile(lst1[0],lst1[1],lst1[2])

    @staticmethod
    def getvendor():
        return 'Samsung Android'

    def isOverheated(self):
        if self.heat > self.max_heat:
            return True
        else:
            return False
    @classmethod
    def isOverheated_cls(cls,phone):
        if phone.heat > cls.max_heat:
            return True
        else:
            return False


sam = Mobile('black', 1000, 90)
print(Mobile.isOverheated_cls(sam))
sam.heat = 101
print(sam.isOverheated())
