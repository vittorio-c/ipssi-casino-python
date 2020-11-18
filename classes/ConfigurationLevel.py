import math

class ConfigurationLevel :
    """ Contient les informations d'un niveau """

    number = None
    nb_try = None
    interval = None
    gain = {}

    def __init__(self, number, nb_try, interval, gain = []) :
        self.number = number
        self.nb_try = nb_try
        self.interval = interval
        #self.gain = gain

    def generateArrayGain(self, mise) :
        self.gain["1"] = {}
        self.gain["2"] = {}
        self.gain["3"] = {}

        self.gain["1"]["1"] = math.ceil(mise * 2)
        self.gain["1"]["2"] = math.ceil(mise)
        self.gain["1"]["3"] = math.ceil(mise / 2)

        self.gain["2"]["1"] = math.ceil(mise * 3)
        self.gain["2"]["2"] = math.ceil(mise * 2)
        self.gain["2"]["3"] = math.ceil(mise)
        self.gain["2"]["4"] = math.ceil(mise / 2)
        self.gain["2"]["5"] = math.ceil(mise / 3)

        self.gain["3"]["1"] = math.ceil(mise * 4)
        self.gain["3"]["2"] = math.ceil(mise * 3)
        self.gain["3"]["3"] = math.ceil(mise * 2)
        self.gain["3"]["4"] = math.ceil(mise)
        self.gain["3"]["5"] = math.ceil(mise / 2)
        self.gain["3"]["6"] = math.ceil(mise / 3)
        self.gain["3"]["7"] = math.ceil(mise / 4)